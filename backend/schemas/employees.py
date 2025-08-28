from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from ..models.employees import ContractType

class EmployeeBase(BaseModel):
    employeeNumber: str
    lastName: str
    firstName: str
    serviceID: int
    contractType: ContractType = ContractType.CDI
    contact: Optional[str] = None
    birthdate: Optional[date] = None

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    employeeNumber: Optional[str] = None
    lastName: Optional[str] = None
    firstName: Optional[str] = None
    serviceID: Optional[int] = None
    contractType: Optional[ContractType] = None
    contact: Optional[str] = None
    birthdate: Optional[date] = None

class EmployeeResponse(EmployeeBase):
    employeeID: int
    createdAt: datetime
    updatedAt: datetime
    
    class Config:
        from_attributes = True