from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.services import ServiceCreate, ServiceUpdate, ServiceResponse
from ..services.service_service import ServiceService
from ..dependencies import get_current_user
from ..models.accounts import Account

router = APIRouter(prefix="/services", tags=["services"])

@router.post("/", response_model=ServiceResponse)
def create_service(
    service: ServiceCreate,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service_service = ServiceService(db)
    return service_service.create_service(service)

@router.get("/", response_model=List[ServiceResponse])
def read_services(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service_service = ServiceService(db)
    return service_service.get_services(skip=skip, limit=limit)

@router.get("/{service_id}", response_model=ServiceResponse)
def read_service(
    service_id: int,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service_service = ServiceService(db)
    service = service_service.get_service(service_id)
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.put("/{service_id}", response_model=ServiceResponse)
def update_service(
    service_id: int,
    service: ServiceUpdate,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service_service = ServiceService(db)
    updated_service = service_service.update_service(service_id, service)
    if not updated_service:
        raise HTTPException(status_code=404, detail="Service not found")
    return updated_service

@router.delete("/{service_id}")
def delete_service(
    service_id: int,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service_service = ServiceService(db)
    if not service_service.delete_service(service_id):
        raise HTTPException(status_code=404, detail="Service not found")
    return {"message": "Service deleted successfully"}