
from models.user import User as UserModel
from schemas.user import User


class UserService:
    def __init__(self, db):
        self.db = db
    
    def create_user(self, user:User):
        
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return new_user