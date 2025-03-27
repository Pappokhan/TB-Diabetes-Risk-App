from flask import Blueprint, request, jsonify, render_template
from app.schemas import PredictionSchema
from app.models import Prediction
from app import db
from app.utils import predict_diabetes

main = Blueprint('main', __name__)
schema = PredictionSchema()

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/api/v1/predict', methods=['POST'])
def predict_api():
    json_data = request.get_json()
    errors = schema.validate(json_data)
    if errors:
        return jsonify({'errors': errors}), 400

    prediction, probability = predict_diabetes(json_data)

    # Log to DB
    record = Prediction(
        data=str(json_data),
        prediction=prediction,
        probability=probability
    )
    db.session.add(record)
    db.session.commit()

    return jsonify({
        'prediction': prediction,
        'probability': round(probability, 4),
        'message': 'Likely Diabetic' if prediction else 'Likely Non-Diabetic'
    })