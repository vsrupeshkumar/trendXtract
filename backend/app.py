from flask import Flask, request, render_template
from model import load_and_analyze
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'backend/data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    topics = None
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            topics = load_and_analyze(filepath)
    return render_template('index.html', topics=topics)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

