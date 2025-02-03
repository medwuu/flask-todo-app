import hashlib
from app import db, login_manager
from flask_login import UserMixin
import sqlalchemy as sa


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String(50), nullable=False)
    name = sa.Column(sa.String(50), nullable=False)
    password = sa.Column(sa.String(64), nullable=False)

    def __repr__(self):
        return f"<User {self.name} (id {self.id})>"

    def hashPassword(self, raw_password):
        self.password = hashlib.sha256(raw_password.encode('ASCII')).hexdigest()

    def checkPassword(self, raw_password):
        return self.password == hashlib.sha256(raw_password.encode('ASCII')).hexdigest()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))