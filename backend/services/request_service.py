from sqlalchemy.orm import Session
from ..models.requests import Request, RequestStatus
from ..schemas.requests import RequestCreate, RequestUpdate
from typing import List, Optional

class RequestService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_request(self, request: RequestCreate, created_by: int) -> Request:
        request_data = request.dict()
        request_data['createdBy'] = created_by
        db_request = Request(**request_data)
        self.db.add(db_request)
        self.db.commit()
        self.db.refresh(db_request)
        return db_request
    
    def get_request(self, request_id: int) -> Optional[Request]:
        return self.db.query(Request).filter(Request.requestID == request_id).first()
    
    def get_requests(self, skip: int = 0, limit: int = 100) -> List[Request]:
        return self.db.query(Request).offset(skip).limit(limit).all()
    
    def get_requests_by_employee(self, employee_id: int) -> List[Request]:
        return self.db.query(Request).filter(Request.employeeID == employee_id).all()
    
    def get_pending_requests(self) -> List[Request]:
        return self.db.query(Request).filter(Request.status == RequestStatus.PENDING).all()
    
    def update_request(self, request_id: int, request: RequestUpdate) -> Optional[Request]:
        db_request = self.get_request(request_id)
        if db_request:
            for key, value in request.dict(exclude_unset=True).items():
                setattr(db_request, key, value)
            self.db.commit()
            self.db.refresh(db_request)
        return db_request
    
    def approve_request(self, request_id: int, level: int) -> Optional[Request]:
        db_request = self.get_request(request_id)
        if db_request:
            if level == 1:
                db_request.status = RequestStatus.FIRST_LEVEL_APPROVED
                db_request.validatedN1At = datetime.utcnow()
            elif level == 2:
                db_request.status = RequestStatus.SECOND_LEVEL_APPROVED
                db_request.validatedN2At = datetime.utcnow()
            self.db.commit()
            self.db.refresh(db_request)
        return db_request
    
    def reject_request(self, request_id: int) -> Optional[Request]:
        db_request = self.get_request(request_id)
        if db_request:
            db_request.status = RequestStatus.REJECTED
            self.db.commit()
            self.db.refresh(db_request)
        return db_request