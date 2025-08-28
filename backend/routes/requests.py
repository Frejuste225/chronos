from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.requests import RequestCreate, RequestUpdate, RequestResponse
from ..services.request_service import RequestService
from ..dependencies import get_current_user
from ..models.accounts import Account

router = APIRouter(prefix="/requests", tags=["requests"])

@router.post("/", response_model=RequestResponse)
def create_request(
    request: RequestCreate,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = RequestService(db)
    return service.create_request(request, current_user.employeeID)

@router.get("/", response_model=List[RequestResponse])
def read_requests(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = RequestService(db)
    return service.get_requests(skip=skip, limit=limit)

@router.get("/my-requests", response_model=List[RequestResponse])
def read_my_requests(
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = RequestService(db)
    return service.get_requests_by_employee(current_user.employeeID)

@router.get("/pending", response_model=List[RequestResponse])
def read_pending_requests(
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = RequestService(db)
    return service.get_pending_requests()

@router.get("/{request_id}", response_model=RequestResponse)
def read_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = RequestService(db)
    request = service.get_request(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    return request

@router.put("/{request_id}", response_model=RequestResponse)
def update_request(
    request_id: int,
    request: RequestUpdate,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = RequestService(db)
    updated_request = service.update_request(request_id, request)
    if not updated_request:
        raise HTTPException(status_code=404, detail="Request not found")
    return updated_request

@router.post("/{request_id}/approve/{level}")
def approve_request(
    request_id: int,
    level: int,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    if level not in [1, 2]:
        raise HTTPException(status_code=400, detail="Invalid approval level")
    
    service = RequestService(db)
    approved_request = service.approve_request(request_id, level)
    if not approved_request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    return {"message": f"Request approved at level {level}"}

@router.post("/{request_id}/reject")
def reject_request(
    request_id: int,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = RequestService(db)
    rejected_request = service.reject_request(request_id)
    if not rejected_request:
        raise HTTPException(status_code=404, detail="Request not found")
    
    return {"message": "Request rejected"}