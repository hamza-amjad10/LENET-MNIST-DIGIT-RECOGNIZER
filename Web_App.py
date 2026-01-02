import streamlit as st
import requests
from PIL import Image
import io

st.title("MNIST Digit Prediction")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("L")  # Convert to grayscale
    image.thumbnail((150, 150))                     # Small preview
    st.image(image, caption="Uploaded Image Preview", use_container_width=False)
    
    if st.button("Predict"):
        try:
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            files = {'file': img_bytes}

            api_url = "https://823eb11ed452.ngrok-free.app/predict"  # Add Flask API URL here
            response = requests.post(api_url, files=files)
            
            if response.status_code == 200:
                data = response.json()
                digit = data.get("predicted_digit")
                confidence = data.get("confidence")
                
                if digit is not None and confidence is not None:
                    st.success(f"Predicted Digit: {digit}")
                    st.write(f"Confidence Level: {int(confidence*100)}%")
                    st.progress(int(confidence*100))
                else:
                    st.error("No prediction or confidence returned from API.")
            else:
                st.error(f"Prediction failed. Status code: {response.status_code}")
        
        except Exception as e:
            st.error(f"Error connecting to API: {e}")
