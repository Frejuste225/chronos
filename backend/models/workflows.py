from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Workflow(Base):
    __tablename__ = "workflows"
    
    workflowID = Column(Integer, primary_key=True, autoincrement=True)
    requestID = Column(Integer, ForeignKey('requests.requestID'), nullable=False)
    validator = Column(Integer, ForeignKey('employees.employeeID'), nullable=False)
    delegate = Column(Integer, ForeignKey('employees.employeeID'))
    assignDate = Column(DateTime, nullable=False)
    validationDate = Column(DateTime)
    status = Column(Integer, nullable=False)
    
    # Relations
    request = relationship("Request", back_populates="workflows")
    validator_employee = relationship("Employee", foreign_keys=[validator])
    delegate_employee = relationship("Employee", foreign_keys=[delegate])
