from app import ma
from marshmallow import fields, validate

class PredictionSchema(ma.Schema):
    Pregnancies = fields.Integer(required=True)
    Glucose = fields.Float(required=True)
    BloodPressure = fields.Float(required=True)
    SkinThickness = fields.Float(required=True)
    Insulin = fields.Float(required=True)
    BMI = fields.Float(required=True)
    DiabetesPedigreeFunction = fields.Float(required=True)
    Age = fields.Integer(required=True)
