from sqlalchemy import Column, Integer, DateTime, Date, Time, Text, ForeignKey, Enum, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base
import enum

class RequestStatus(str, enum.Enum):
    PENDING = "pending"
    SUBMITTED = "submitted"
    FIRST_LEVEL_APPROVED = "firstLevelApproved"
    IN_PROGRESS = "inProgress"
    SECOND_LEVEL_APPROVED = "secondLevelApproved"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class Request(Base):
    __tablename__ = "requests"
    
    requestID = Column(Integer, primary_key=True, autoincrement=True)
    employeeID = Column(Integer, ForeignKey('employees.employeeID'), nullable=False)
    requestDate = Column(Date, nullable=False)
    previousStart = Column(Time)
    previousEnd = Column(Time)
    startAt = Column(Time, nullable=False)
    endAt = Column(Time, nullable=False)
    status = Column(Enum(RequestStatus), default=RequestStatus.PENDING)
    comment = Column(Text)
    createdBy = Column(Integer, ForeignKey('employees.employeeID'))
    validatedN1At = Column(DateTime)
    validatedN2At = Column(DateTime)
    createdAt = Column(DateTime, default=func.current_timestamp())
    updatedAt = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    __table_args__ = (
        CheckConstraint('endAt > startAt', name='check_hours'),
        CheckConstraint('previousEnd > previousStart', name='check_previous_hours'),
    )
    
    # Relations
    employee = relationship("Employee", foreign_keys=[employeeID], back_populates="requests")
    creator = relationship("Employee", foreign_keys=[createdBy])
    workflows = relationship("Workflow", back_populates="request")
    request_employees = relationship("RequestEmployee", back_populates="request")
