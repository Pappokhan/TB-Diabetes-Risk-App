from app import db

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    prediction = db.Column(db.Integer)
    probability = db.Column(db.Float)
