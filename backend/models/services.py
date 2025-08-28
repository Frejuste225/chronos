from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class Service(Base):
    __tablename__ = "services"
    
    serviceID = Column(Integer, primary_key=True, autoincrement=True)
    serviceCode = Column(String(10), unique=True, nullable=False)
    serviceName = Column(String(100), nullable=False)
    parentServiceID = Column(Integer, ForeignKey('services.serviceID'), nullable=True)
    description = Column(Text)
    manager = Column(String(100))
    createdAt = Column(DateTime, default=func.current_timestamp())
    updatedAt = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    # Relations
    parent_service = relationship("Service", remote_side=[serviceID])
    child_services = relationship("Service")
    employees = relationship("Employee", back_populates="service")