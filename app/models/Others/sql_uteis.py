from app import db
from sqlalchemy import Float,Column,Integer,String,ForeignKey,DateTime,Time,Boolean,Date
from werkzeug.security import check_password_hash as CPH
from werkzeug.security import generate_password_hash as GPH


class auxDB():
    id      = Column(Integer,primary_key=True)

    def save(self):
        try:
            if not self.id:
                db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            raise
        
    
    def delete(self):
        db.session.rollback()
        db.session.delete(self)
        db.session.commit()

    def check_password(self,password):
        return CPH(self.password, password)

    def set_password(self,password):
        self.password = GPH(password,method="sha256")
        return self.password
    
    def __repr__(self):
        return f"<{self.__tablename__} {self.id}>"
    