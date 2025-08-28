from sqlalchemy.orm import Session
from ..models.services import Service
from ..schemas.services import ServiceCreate, ServiceUpdate
from typing import List, Optional

class ServiceService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_service(self, service: ServiceCreate) -> Service:
        db_service = Service(**service.dict())
        self.db.add(db_service)
        self.db.commit()
        self.db.refresh(db_service)
        return db_service
    
    def get_service(self, service_id: int) -> Optional[Service]:
        return self.db.query(Service).filter(Service.serviceID == service_id).first()
    
    def get_services(self, skip: int = 0, limit: int = 100) -> List[Service]:
        return self.db.query(Service).offset(skip).limit(limit).all()
    
    def update_service(self, service_id: int, service: ServiceUpdate) -> Optional[Service]:
        db_service = self.get_service(service_id)
        if db_service:
            for key, value in service.dict(exclude_unset=True).items():
                setattr(db_service, key, value)
            self.db.commit()
            self.db.refresh(db_service)
        return db_service
    
    def delete_service(self, service_id: int) -> bool:
        db_service = self.get_service(service_id)
        if db_service:
            self.db.delete(db_service)
            self.db.commit()
            return True
        return False
