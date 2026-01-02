# LeNet MNIST Digit Recognizer

A web application for recognizing handwritten digits (0-9) using the LeNet convolutional neural network trained on the MNIST dataset. The backend is powered by Flask and the frontend uses Streamlit for real-time predictions.

## Features
- Upload handwritten digit images (PNG, JPG, JPEG)  
- Predict digits with high accuracy (~98%)  
- Shows confidence as a progress bar  
- Real-time image preview in frontend  
- Built with Python, TensorFlow/Keras, Flask, and Streamlit

## Project Structure

LeNet_MNIST_model.h5          # Trained LeNet CNN model  

Model_Code.ipynb               # Notebook / Flask API server code  

Web_App.py                     # Streamlit frontend  

README.md                      # Project documentation  

## Installation
1. Clone the repository  

git clone https://github.com/hamza-amjad10/LENET-MNIST-DIGIT-RECOGNIZER.git
cd LENET-MNIST-DIGIT-RECOGNIZER
Create and activate virtual environment

bash
Copy code
python -m venv venv
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
Install dependencies



Run the Streamlit Frontend

streamlit run Web_App.py

Upload a handwritten digit image

Click Predict to see the predicted digit and confidence

The progress bar shows the model’s confidence percentage

API Usage Example
python
Copy code
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

json
Copy code
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

## Author
Hamza Amjad  
AI, Machine Learning, NLP & Deep Learning Enthusiast
