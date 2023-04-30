from flask import Flask, jsonify, request

from FraudDetector import FraudDetector

app = Flask(__name__)


@app.route('/train', methods=['POST'])
def upload_csv_and_join():
    # Get CSV file from request
    csv_file = request.files['csv_file']
    target = request.json['target']
    global fd
    fd = FraudDetector(csv_file, ['customer', 'gender', 'category', 'amount'], target)
    response = {
        'accuracy': fd.getAccuracy()
    }
    return jsonify(response)


@app.route('/predict_features', methods=['POST'])
def check_strings():
    # Get strings from request
    features = request.json['features']
    is_valid = all(len(s) > 0 for s in features)
    global fd
    response = fd.getPrediction(features[0], features[1], features[2], features[3])
    response = {
        'prediction': response
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
