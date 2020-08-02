import uuid
from datetime import datetime

from models import db


class Image(db.Model):
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    parent_id = db.Column(db.String(), db.ForeignKey('image.id'), nullable=True)
    caption = db.Column(db.String())
    url = db.Column(db.String())
    finished = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), default=lambda: datetime.now().strftime("%Y-%m-%d, %H:%M:%S"))
    derivatives = db.relationship('Image', backref='parent', lazy='joined', remote_side=[id])

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f"<Image id={self.id} caption={self.caption} url={self.url}>"

