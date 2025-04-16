from flask import Flask, render_template, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

# Load model and tokenizer
model_name = 'FriedGil/distillBERT-misinformation-classifier'
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model.eval()

# Setup Google API
SERVICE_ACCOUNT_FILE = 'serious-energy-432707-a3-1c58b80fdb6f.json'
SCOPES = ['https://www.googleapis.com/auth/cse']
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('customsearch', 'v1', credentials=credentials)

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"D:\Misinformation Classifier Project\tesseract.exe"

def google_search(query, cse_id, num_results=3):
    try:
        res = service.cse().list(q=query, cx=cse_id, num=num_results).execute()
        links = [item['link'] for item in res.get('items', [])]
        return links
    except Exception as e:
        return []

@app.route('/')
def home():
    return render_template('webpage.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        data = request.json
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'}), 400

        text = data['text']
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

        with torch.no_grad():
            outputs = model(**inputs)
            prediction = torch.argmax(outputs.logits, dim=1)

        result = "True" if prediction.item() == 1 else "False"

        if result == "True":
            links = google_search(text, '068275577b6e24d6b')
            return jsonify(result=result, links=links)
        else:
            return jsonify(result=result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']

    try:
        image = Image.open(io.BytesIO(file.read()))
        text = pytesseract.image_to_string(image)
        return jsonify({'text': text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
