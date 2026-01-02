# LeNet MNIST Digit Recognizer

A **web application** for recognizing handwritten digits (0-9) using the **LeNet convolutional neural network** trained on the **MNIST dataset**.  
The backend is powered by **Flask** and the frontend uses **Streamlit** for real-time predictions.

---

## Features

- Upload handwritten digit images (PNG, JPG, JPEG)  
- Predict digits with high **accuracy (~98%)**  
- Shows **confidence** as a progress bar  
- Real-time **image preview** in frontend  
- Built with **Python, TensorFlow/Keras, Flask, and Streamlit**

---

## Project Structure



lenet-mnist-digit-recognizer/
│
├── LeNet_MNIST_model.h5 # Trained LeNet CNN model
├── Model_Code.ipynb # Flask API server
├── Web_App.py # Streamlit frontend
├── requirements.txt # Python dependencies
└── README.md


---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/lenet-mnist-digit-recognizer.git
cd lenet-mnist-digit-recognizer


Create and activate virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt

Run the Flask API
python app.py


API endpoint: http://localhost:5000/predict

Method: POST

File parameter: file (image)

Run the Streamlit Frontend
streamlit run Web_App.py


Upload a handwritten digit image

Click Predict to see the predicted digit and confidence

The progress bar shows model’s confidence percentage

API Usage Example
import requests
from PIL import Image
import io

img = Image.open("digit.png").convert("L")
img_bytes = io.BytesIO()
img.save(img_bytes, format="PNG")
img_bytes.seek(0)

files = {'file': img_bytes}
response = requests.post("http://localhost:5000/predict", files=files)
print(response.json())


Example Response:

{
  "predicted_digit": 7,
  "confidence": 0.9987
}

Model Details

Architecture: LeNet CNN

Dataset: MNIST

Input shape: 32x32 grayscale

Output: 10 classes (digits 0-9)

Activation: tanh for hidden layers, softmax for output

Optimizer: Adam

Loss: sparse_categorical_crossentropy

Test Accuracy: ~98.2%