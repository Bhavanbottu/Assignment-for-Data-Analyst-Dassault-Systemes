from flask import Flask, render_template, request
import csv
import json

app = Flask(__name__, template_folder='.')

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

# Function to store user data in a CSV file
def store_user_data_csv(name, gender, blood_group):
    with open('user_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, gender, blood_group])

# Function to store user data in a JSON file
def store_user_data_json(name, gender, blood_group):
    user_data = {'Name': name, 'Gender': gender, 'Blood Group': blood_group}
    with open('user_data.json', 'a') as file:
        json.dump(user_data, file)
        file.write('\n')

# Define route for web form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        gender = request.form["gender"]
        blood_group_type = request.form["blood_group"]
        
        predicted_condition = predict_condition(name, gender, blood_group_type)
        
        # Store user data
        store_user_data_csv(name, gender, blood_group_type)
        store_user_data_json(name, gender, blood_group_type)
        
        return render_template("result.html", name=name, predicted_condition=predicted_condition)
    
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
