import uuid
from datetime import datetime

from models import db


class Image(db.model):
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    parent_id = db.Column(db.String())
    caption = db.Column(db.String())
    url = db.Column(db.String(), default=False)
    finished = db.Column(db.Boolean())
    created_at = db.Column(db.DateTime(), default=lambda: str(datetime.now()))

