from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.employees import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from ..services.employee_service import EmployeeService
from ..dependencies import get_current_user
from ..models.accounts import Account

router = APIRouter(prefix="/employees", tags=["employees"])

@router.post("/", response_model=EmployeeResponse)
def create_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = EmployeeService(db)
    return service.create_employee(employee)

@router.get("/", response_model=List[EmployeeResponse])
def read_employees(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = EmployeeService(db)
    return service.get_employees(skip=skip, limit=limit)

@router.get("/{employee_id}", response_model=EmployeeResponse)
def read_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = EmployeeService(db)
    employee = service.get_employee(employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee

@router.put("/{employee_id}", response_model=EmployeeResponse)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = EmployeeService(db)
    updated_employee = service.update_employee(employee_id, employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: Account = Depends(get_current_user)
):
    service = EmployeeService(db)
    if not service.delete_employee(employee_id):
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}
