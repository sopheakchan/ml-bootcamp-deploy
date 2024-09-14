from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import joblib

app = Flask(__name__)
model = joblib.load('random_forest_model.pkl')

@app.route('/homepage')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

# Update this route to serve files directly from the flower directory
@app.route('/flower/<path:filename>')
def serve_flower(filename):
    return send_from_directory('flower', filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4984) # start port 4980 
