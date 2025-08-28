from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Delegation(Base):
    __tablename__ = "delegations"
    
    delegationID = Column(Integer, primary_key=True, autoincrement=True)
    delegatedBy = Column(Integer, ForeignKey('employees.employeeID'), nullable=False)
    delegatedTo = Column(Integer, ForeignKey('employees.employeeID'), nullable=False)
    startAt = Column(Date, nullable=False)
    endAt = Column(Date, nullable=False)
    
    # Relations
    delegator = relationship("Employee", foreign_keys=[delegatedBy], back_populates="delegations_given")
    delegate = relationship("Employee", foreign_keys=[delegatedTo], back_populates="delegations_received")