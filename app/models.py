from app import db
from datetime import datetime

class Flights(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    airline_code = db.Column(db.String(20), index=True, unique=True, nullable=False)
    flight_number = db.Column(db.String(20), nullable=False)
    departure_port = db.Column(db.String(5), nullable=False)
    arrival_port = db.Column(db.String(5), nullable=False)
    departure_time = db.Column(db.DateTime) 
    arrival_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Flights {}>'.format(self.name)

