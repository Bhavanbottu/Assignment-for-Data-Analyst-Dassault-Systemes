from flask import Flask, render_template, request
import os
import pandas as pd
app = Flask(__name__, template_folder='.')

# Load the healthcare data
data = pd.read_csv("healthcare_dataset.csv")

# Placeholder function to predict medical condition
def predict_condition(name, gender, blood_group_type):
    # Placeholder logic
    # Replace this with actual logic based on insights from correlation
    if blood_group_type == 'A' and gender == 'Male':
        return 'Heart Disease'
    elif blood_group_type == 'B' and gender == 'Female':
        return 'Diabetes'
    else:
        return 'Other Condition'

# Define route for web form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        gender = request.form["gender"]
        blood_group_type = request.form["blood_group"]
        
        predicted_condition = predict_condition(name, gender, blood_group_type)
        return render_template("form.html", name=name, predicted_condition=predicted_condition)
    
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
