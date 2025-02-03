from app import db
from datetime import datetime
import sqlalchemy as sa

class Tasks(db.Model):
    __tablename__ = "tasks"
    id = sa.Column(sa.Integer, primary_key=True)
    task = sa.Column(sa.Text, nullable=False)
    creation_date = sa.Column(sa.DateTime, default=datetime.now())
    completed = sa.Column(sa.Boolean, default=False)
    owner = sa.Column(sa.Integer, sa.ForeignKey('users.id'), nullable=False)