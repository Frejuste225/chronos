from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base
import enum

class ContractType(str, enum.Enum):
    CDI = "CDI"
    CDD = "CDD"
    INTERIM = "Interim"
    STAGE = "Stage"
    ALTERNANCE = "Alternance"
    MOO = "MOO"

class Employee(Base):
    __tablename__ = "employees"
    
    employeeID = Column(Integer, primary_key=True, autoincrement=True)
    employeeNumber = Column(String(20), unique=True, nullable=False)
    lastName = Column(String(20), nullable=False)
    firstName = Column(String(30), nullable=False)
    serviceID = Column(Integer, ForeignKey('services.serviceID'), nullable=False)
    contractType = Column(Enum(ContractType), default=ContractType.CDI)
    contact = Column(String(20))
    birthdate = Column(Date)
    createdAt = Column(DateTime, default=func.current_timestamp())
    updatedAt = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    # Relations
    service = relationship("Service", back_populates="employees")
    account = relationship("Account", back_populates="employee", uselist=False)
    requests = relationship("Request", back_populates="employee")
    delegations_given = relationship("Delegation", foreign_keys="Delegation.delegatedBy", back_populates="delegator")
    delegations_received = relationship("Delegation", foreign_keys="Delegation.delegatedTo", back_populates="delegate")