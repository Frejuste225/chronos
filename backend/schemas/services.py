from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ServiceBase(BaseModel):
    serviceCode: str
    serviceName: str
    parentServiceID: Optional[int] = None
    description: Optional[str] = None
    manager: Optional[str] = None

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    serviceCode: Optional[str] = None
    serviceName: Optional[str] = None
    parentServiceID: Optional[int] = None
    description: Optional[str] = None
    manager: Optional[str] = None

class ServiceResponse(ServiceBase):
    serviceID: int
    createdAt: datetime
    updatedAt: datetime
    
    class Config:
        from_attributes = True