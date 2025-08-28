from sqlalchemy.orm import Session
from ..models.employees import Employee
from ..schemas.employees import EmployeeCreate, EmployeeUpdate
from typing import List, Optional

class EmployeeService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_employee(self, employee: EmployeeCreate) -> Employee:
        db_employee = Employee(**employee.dict())
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee
    
    def get_employee(self, employee_id: int) -> Optional[Employee]:
        return self.db.query(Employee).filter(Employee.employeeID == employee_id).first()
    
    def get_employees(self, skip: int = 0, limit: int = 100) -> List[Employee]:
        return self.db.query(Employee).offset(skip).limit(limit).all()
    
    def update_employee(self, employee_id: int, employee: EmployeeUpdate) -> Optional[Employee]:
        db_employee = self.get_employee(employee_id)
        if db_employee:
            for key, value in employee.dict(exclude_unset=True).items():
                setattr(db_employee, key, value)
            self.db.commit()
            self.db.refresh(db_employee)
        return db_employee
    
    def delete_employee(self, employee_id: int) -> bool:
        db_employee = self.get_employee(employee_id)
        if db_employee:
            self.db.delete(db_employee)
            self.db.commit()
            return True
        return False