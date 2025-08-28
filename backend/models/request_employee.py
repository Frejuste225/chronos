from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class RequestEmployee(Base):
    __tablename__ = "requestEmployee"
    
    ID = Column(Integer, primary_key=True, autoincrement=True)
    employeeID = Column(Integer, ForeignKey('employees.employeeID'), nullable=False)
    requestID = Column(Integer, ForeignKey('requests.requestID'), nullable=False)
    totalHours = Column(Float, nullable=False)
    
    # Relations
    employee = relationship("Employee")
    request = relationship("Request", back_populates="request_employees")