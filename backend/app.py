from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Allow requests from React frontend

# Example trending AI topics
fake_topics = [
    {"topic": "LLM Fine-Tuning", "growth": 66},
    {"topic": "Open-Source Models", "growth": 59},
    {"topic": "Synthetic Data", "growth": 52},
    {"topic": "Multimodal AI", "growth": 84},
    {"topic": "AGI Safety", "growth": 77},
    {"topic": "Self-supervised Learning", "growth": 61},
    {"topic": "AI Hardware Acceleration", "growth": 69},
    {"topic": "Foundation Models", "growth": 75},
    {"topic": "AI for Robotics", "growth": 64},
]

@app.route("/api/trends", methods=["GET"])
def get_trends():
    # Return shuffled trending topics
    return jsonify({
        "trending_topics": random.sample(fake_topics, k=5)
    })

if __name__ == "__main__":
    app.run(debug=True)
