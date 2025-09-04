Misinformation Detection with BERT + Flask + OCR

This project is a Fake News / Misinformation Detection Web App built with BERT Transformers, Flask, Google Search API, and OCR (Tesseract).

It allows users to:
	•	Enter text manually or upload an image containing text.
	•	The app extracts text (using Tesseract OCR) if an image is uploaded.
	•	Detects whether the news/text is True or False using a fine-tuned BERT model.
	•	If the text is classified as True, it fetches and displays 3 relevant verified links from Google.

⸻

🚀 Features
	•	🧠 BERT Transformer Model – Detects misinformation.
	•	🌐 Google Custom Search API – Provides verified links for true information.
	•	📸 OCR Support (Tesseract) – Extracts text automatically from uploaded images.
	•	🌍 Web Interface (Flask) – Simple and interactive UI.

⸻

🛠 Tech Stack
	•	Python (Flask, PyTorch, Transformers)
	•	BERT (distillBERT-misinformation-classifier)
	•	Google API (Custom Search Engine)
	•	OCR (Tesseract + Pillow)
	•	Frontend: HTML, CSS, JavaScript

⸻

📂 Project Structure

📦 Misinformation-Detector
├── app.py                 # Flask backend
├── templates/
│   └── webpage.html       # Frontend HTML
├── static/
│   ├── styles.css         # CSS for styling
│   └── script.js          # JS for API requests
├── serious-energy-432707-a3-1c58b80fdb6f.json   # Google API credentials
└── README.md              # Project documentation


⸻

⚙ Installation & Setup
	1.	Clone the repo

git clone https://github.com/your-username/misinformation-detector.git
cd misinformation-detector

	2.	Install dependencies

pip install flask torch transformers google-api-python-client google-auth pytesseract pillow

	3.	Install Tesseract OCR

	•	Download Tesseract for Windows
	•	Place it in D:\Misinformation Classifier Project\tesseract.exe
	•	Or update the path in app.py:

pytesseract.pytesseract.tesseract_cmd = r"D:\Misinformation Classifier Project\tesseract.exe"

	4.	Run the Flask app

python app.py

	5.	Open in browser
Go to 👉 http://127.0.0.1:5000/

⸻

🖼 Screenshots

🔹 Enter text or upload image
🔹 Get prediction (True/False)
🔹 See verified links for true news

⸻

🔮 Future Improvements
	•	Deploy on Heroku / Render / AWS
	•	Add multi-language OCR support
	•	Improve model accuracy with more training
	•	Store results in a database

⸻

📜 License

This project is open-source and free to use under the MIT License.
