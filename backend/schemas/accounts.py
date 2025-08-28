from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from ..models.accounts import ProfileType

class AccountBase(BaseModel):
    employeeID: int
    username: str
    profile: ProfileType = ProfileType.VALIDATOR
    isActive: bool = True

class AccountCreate(AccountBase):
    password: str

class AccountUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    profile: Optional[ProfileType] = None
    isActive: Optional[bool] = None

class AccountResponse(AccountBase):
    accountID: int
    lastLogin: Optional[datetime] = None
    createdAt: datetime
    updatedAt: datetime
    
    class Config:
        from_attributes = True
