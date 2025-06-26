from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import pandas as pd
from model import analyze_uploaded_file

app = Flask(__name__)
CORS(app)  # ✅ Allows frontend (React) to connect to Flask

# Route for your Flask HTML page (if you want to keep it)
@app.route('/')
def index():
    return render_template('index.html')

# Route for file uploads (from HTML form if needed)
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filepath = os.path.join('data', file.filename)
        file.save(filepath)
        result = analyze_uploaded_file(filepath)
        return render_template('index.html', result=result)

# ✅ NEW: API endpoint for React frontend
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    # 🔁 Replace with your actual logic if needed
    result = f"Emerging trend in: {text[:50]}..."

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

