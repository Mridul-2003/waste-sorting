from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__,static_folder="static")

# Sample waste items with corresponding image filenames
waste_items = [
    {"item": "Plastic Bottle", "image": "plastic_bottle.jpeg", "label": "Recyclable"},
    {"item": "Paper", "image": "paper.jpeg", "label": "Recyclable"},
    # {"item": "Aluminum Can", "image": "aluminum_can.jpg", "label": "Recyclable"},
    # {"item": "Glass", "image": "glass.jpg", "label": "Recyclable"},
    {"item": "Organic Waste", "image": "organic_waste.png", "label": "Non-Recyclable"}
]

# Mock machine learning model function (replace with your actual model)
def model_predict(item_to_classify):
    # Replace this with your model's prediction logic
    # For this example, we'll assume a simple rule-based model
    recyclable_items = ["Plastic Bottle", "Paper", "Organic Waste"]
    
    if item_to_classify in recyclable_items:
        return "Recyclable"
    else:
        return "Non-Recyclable"

# Route to start the game
@app.route("/")
def index():
    # Randomly select a waste item for the user to classify
    item_info = random.choice(waste_items)
    item_to_classify = item_info["item"]
    item_image = item_info["image"]
    true_label = item_info["label"]
    return render_template("classify.html", item_to_classify=item_to_classify, item_image=item_image, true_label=true_label)

# Route to handle user input and calculate the score
@app.route("/classify", methods=["POST"])
def classify():
    user_choice = request.form["user_choice"]
    item_to_classify = request.form["item_to_classify"]
    
    # Get the model prediction for the item
    model_prediction = model_predict(item_to_classify)
    
    # Check if the user's choice matches the model prediction
    if user_choice == model_prediction:
        score = 1  # Correct classification
    else:
        score = 0  # Incorrect classification
    
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(debug=True)
