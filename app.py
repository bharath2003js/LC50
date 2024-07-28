from flask import Flask, request, render_template
import pandas as pd
import pickle
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

# Load models
with open('models/rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)
    logger.info("Random Forest model loaded.")

with open('models/svr_model.pkl', 'rb') as f:
    svr_model = pickle.load(f)
    logger.info("SVR model loaded.")

with open('models/gbr_model.pkl', 'rb') as f:
    gbr_model = pickle.load(f)
    logger.info("Gradient Boosting Regressor model loaded.")


@app.route('/')
def index():
    logger.info("Rendering index page.")
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        logger.info("Prediction request received.")

        # Get form data
        data = {
            'descriptor1': float(request.form['descriptor1']),
            'descriptor2': float(request.form['descriptor2']),
            'descriptor3': float(request.form['descriptor3']),
            'descriptor4': float(request.form['descriptor4']),
            'descriptor5': float(request.form['descriptor5']),
            'descriptor6': float(request.form['descriptor6'])
        }
        logger.info(f"Form data received: {data}")

        # Convert to DataFrame
        input_data = pd.DataFrame(data, index=[0])
        logger.info(f"Input data converted to DataFrame: {input_data}")

        # Make predictions
        rf_pred = rf_model.predict(input_data)
        svr_pred = svr_model.predict(input_data)
        gbr_pred = gbr_model.predict(input_data)
        logger.info(f"Predictions made - RF: {rf_pred}, SVR: {svr_pred}, GBR: {gbr_pred}")

        # Ensemble prediction
        ensemble_pred = (rf_pred + svr_pred + gbr_pred) / 3
        logger.info(f"Ensemble prediction: {ensemble_pred}")

        # Render the result template with the prediction
        return render_template('result.html', prediction=ensemble_pred[0])

    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)
