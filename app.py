from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model and scaler
try:
    model = pickle.load(open('heart_disease_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except FileNotFoundError as e:
    print(f"Error: {e}. Ensure 'heart_disease_model.pkl' and 'scaler.pkl' are in the project directory.")
    exit(1)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/input', methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        user_info = {
            'name': request.form['name'],
            'email': request.form['email']
        }
        return render_template('input.html', user_info=user_info)
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]
        
        # Scale the input data
        features_scaled = scaler.transform([features])
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        result = "The person has heart disease" if prediction == 1 else "The person does not have heart disease"
        
        # Get user info from form
        user_info = {
            'name': request.form['name'],
            'email': request.form['email']
        }
        
        return render_template('output.html', prediction=result, user_info=user_info)
    
    except ValueError as e:
        # Handle invalid input (e.g., non-numeric values)
        error_message = "Invalid input. Please ensure all fields are filled with valid numbers."
        user_info = {
            'name': request.form.get('name', ''),
            'email': request.form.get('email', '')
        }
        return render_template('input.html', user_info=user_info, error_message=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)