from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime, time
from ..models.requests import RequestStatus

class RequestBase(BaseModel):
    employeeID: int
    requestDate: date
    previousStart: Optional[time] = None
    previousEnd: Optional[time] = None
    startAt: time
    endAt: time = Field(..., description="Must be greater than startAt")
    comment: Optional[str] = None

class RequestCreate(RequestBase):
    pass

class RequestUpdate(BaseModel):
    requestDate: Optional[date] = None
    previousStart: Optional[time] = None
    previousEnd: Optional[time] = None
    startAt: Optional[time] = None
    endAt: Optional[time] = None
    status: Optional[RequestStatus] = None
    comment: Optional[str] = None

class RequestResponse(RequestBase):
    requestID: int
    status: RequestStatus
    createdBy: Optional[int] = None
    validatedN1At: Optional[datetime] = None
    validatedN2At: Optional[datetime] = None
    createdAt: datetime
    updatedAt: datetime
    
    class Config:
        from_attributes = True