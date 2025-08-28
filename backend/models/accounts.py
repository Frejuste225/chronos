from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base
import enum

class ProfileType(str, enum.Enum):
    VALIDATOR = "Validator"
    SUPERVISOR = "Supervisor"
    ADMINISTRATOR = "Administrator"
    COORDINATOR = "Coordinator"

class Account(Base):
    __tablename__ = "accounts"
    
    accountID = Column(Integer, primary_key=True, autoincrement=True)
    employeeID = Column(Integer, ForeignKey('employees.employeeID'), unique=True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    profile = Column(Enum(ProfileType), default=ProfileType.VALIDATOR)
    isActive = Column(Boolean, default=True)
    lastLogin = Column(DateTime)
    resetToken = Column(String(100))
    resetTokenExpiry = Column(DateTime)
    createdAt = Column(DateTime, default=func.current_timestamp())
    updatedAt = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    # Relations
    employee = relationship("Employee", back_populates="account")