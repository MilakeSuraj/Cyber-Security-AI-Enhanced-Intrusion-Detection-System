from flask import Flask, render_template, request
import numpy as np
from joblib import load

app = Flask(__name__)
# Load the model trained with 4 features
model = load("random_forest_model_4_features.joblib")

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect the 4 specific feature values from the form
        feature_values = []
        feature_names = [
            'Flow Duration',
            'Total Fwd Packets',
            'Total Backward Packets',
            'Total Length of Fwd Packets'
        ]

        # Assuming your HTML form fields are named 'flow_duration', 'total_fwd_packets', etc.
        # It's crucial that these names match your HTML form's input 'name' attributes.
        
        # Example: Using names 'feature1', 'feature2', 'feature3', 'feature4' as in your original HTML logic
        # You'll need to decide on a consistent naming convention for the HTML fields.
        # For this example, I'll use simple feature1, feature2, etc. as you had before,
        # but map them to the selected features.
        
        # Make sure these names match the 'name' attributes in your HTML form
        html_input_names = [
            "flow_duration",
            "total_fwd_packets",
            "total_backward_packets",
            "total_length_fwd_packets"
        ]

        for name in html_input_names:
            try:
                feature_values.append(float(request.form[name]))
            except KeyError:
                return f"Error: Missing form field '{name}'. Please provide all 4 feature inputs.", 400
            except ValueError:
                return f"Error: Invalid input for '{name}'. Please enter a valid number.", 400

        input_data = np.array([feature_values])
        prediction = model.predict(input_data)[0]
        return render_template("index.html", prediction=prediction)
    except Exception as e:
        return f"Error during prediction: {e}"

if __name__ == "__main__":
    app.run(debug=True)