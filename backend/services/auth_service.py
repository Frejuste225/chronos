from sqlalchemy.orm import Session
from ..models.accounts import Account
from ..models.employees import Employee
from ..utils.security import verify_password
from typing import Optional

class AuthService:
    def __init__(self, db: Session):
        self.db = db
    
    def authenticate_user(self, username: str, password: str) -> Optional[Account]:
        account = self.db.query(Account).filter(Account.username == username).first()
        if not account:
            return None
        if not verify_password(password, account.password):
            return None
        return account
    
    def get_user_by_username(self, username: str) -> Optional[Account]:
        return self.db.query(Account).filter(Account.username == username).first()
