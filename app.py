from flask import Flask, render_template, request, jsonify
import random
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from PIL import Image
import numpy as np

app = Flask(__name__,static_folder="static", static_url_path="/static")

# Load your machine learning model (cnn.h5) here
try:
    model = load_model("cnn.h5")
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading model:", str(e))

# Sample waste items with corresponding image filenames
waste_items = [
    {"item": "Plastic Bottle", "image": "plastic_bottle.jpeg", "label": "Recyclable"},
    {"item": "Paper", "image": "paper.jpeg", "label": "Recyclable"},
    {"item": "Organic Waste", "image": "organic_waste.png", "label": "Organic"},
    {"item": "Organic Waste 1", "image": "images.jpeg", "label": "Organic"},
    {"item": "Plastic Gamla", "image": "plastic_gamla.jpeg", "label": "Recyclable"},
     {"item": "Soil", "image": "Soil.jpeg", "label": "Organic"}
]

# Function to preprocess an image for model prediction
def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((224, 224))  # Resize image to match your model's input size
    image = np.array(image) / 255.0  # Normalize pixel values
    image = image.reshape((1, 224, 224, 3))  # Reshape for model input (adjust dimensions as needed)
    return image

# Function to make predictions using the loaded model
def model_predict(image_path):
    preprocessed_image = preprocess_image(image_path)
    prediction = model.predict(preprocessed_image)
    threshold = 0.5

    if prediction[0][0] >= threshold:
        return "Organic"
    elif prediction[0][0]<=threshold:
        return "Recyclable"

    
    # Assuming your model returns a probability for each class
    # You can set a threshold to decide the class (e.g., 0.5 for binary classification)
    # threshold = 0.89
    
    # if prediction[0][0] > threshold:
    #     return "Recyclable"
    # else:
    #     return "Organic"

# Route to start the game
@app.route("/")
def main():
    return render_template('index.html')
@app.route('/play')
def play():
    # Randomly select a waste item for the user to classify
    item_info = random.choice(waste_items)
    item_to_classify = item_info["item"]
    item_image = item_info["image"]
    true_label = item_info["label"]
    return render_template("classify.html", item_to_classify=item_to_classify, item_image=item_image, true_label=true_label)

@app.route("/classify", methods=["POST"])
def classify():
    user_choice = request.form["user_choice"]
    item_to_classify = request.form["item_to_classify"]
    
    # Use the model to predict the item's label based on the image
    image_path = f"static/{item_to_classify.lower().replace(' ', '_')}.jpeg"  # Adjust the image path accordingly
    model_prediction = model_predict(image_path)
    
    # Initialize the score
    score = 0
    
    # Check if the user's choice matches the model prediction
    if user_choice == model_prediction:
        score = 1  # Correct classification
    else:
        score=0
    
    # Randomly select a new waste item for the next round
    item_info = random.choice(waste_items)
    item_to_classify = item_info["item"]
    item_image = item_info["image"]
    true_label = item_info["label"]
    
    return jsonify({"score": score, "next_item_to_classify": item_to_classify, "next_item_image": item_image, "true_label": true_label})


if __name__ == "__main__":
    app.run(debug=True)
