
# LC50 Prediction using QSAR Models

## Overview

This project aims to develop a predictive model for estimating the LC50 value (the concentration of a compound that causes 50% lethality of fish in a test batch over 96 hours) using Quantitative Structure–Activity Relationship (QSAR) models. The project leverages machine learning techniques to create an ensemble model combining Random Forest, Support Vector Regression (SVR), and Gradient Boosting Regressor (GBR) models. The model is deployed as a web service on Microsoft Azure, with an API for interaction and a user interface for inputting data and displaying predictions.

## Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## System Architecture

The system architecture consists of the following main components:

1. **Data Collection and Preprocessing**
2. **Model Training**
3. **Model Deployment**
4. **User Interface**
5. **Logging and Monitoring**

### 1. Data Collection and Preprocessing
- **Data Sources**: ECOTOX Database, ECHA
- **Preprocessing Steps**: Cleaning and formatting data, feature engineering, splitting data into training and testing sets

### 2. Model Training
- **Machine Learning Models**: Random Forest Regressor, Support Vector Regressor (SVR), Gradient Boosting Regressor (GBR)
- **Ensemble Model**: Combines predictions from the three individual models
- **Tools and Libraries**: scikit-learn, pandas, pickle

### 3. Model Deployment
- **Deployment Platform**: Microsoft Azure Web Services
- **Deployment Process**: Flask API, hosted on Azure

### 4. User Interface
- **Front-end**: HTML forms for input, display predicted LC50 values
- **Back-end**: Flask framework, integrates with trained models

### 5. Logging and Monitoring
- **Logging**: Python logging library
- **Monitoring**: Azure’s monitoring tools for real-time log streaming and diagnostics

## Features

- Predict LC50 values using QSAR models
- Ensemble model combining Random Forest, SVR, and GBR
- User-friendly web interface for data input and result display
- API for interaction with the model
- Deployed as a scalable and reliable web service on Azure

## Requirements

- Python 3.8+
- Flask
- pandas
- scikit-learn
- pickle
- Microsoft Azure account

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/LC50-Prediction.git
   cd LC50-Prediction
   ```

2. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Download the trained models and place them in the `models` directory.

## Usage

1. Run the Flask app:
   ```sh
   python app.py
   ```

2. Open your browser and go to `http://127.0.0.1:5000` to access the web interface.

3. Input the molecular descriptors and submit the form to get the predicted LC50 value.

## API Endpoints

- **GET /**:
  - Renders the input form (index page)
- **POST /predict**:
  - Accepts form data and returns the predicted LC50 value

## Deployment

### Azure Configuration

1. Create a web app service in Azure.
2. Configure the deployment source (e.g., GitHub repository).
3. Set up environment variables and app settings.
4. Deploy the application.
5. Monitor the deployment logs and ensure the app is running correctly.

### Continuous Deployment

Link your GitHub repository to Azure for automated deployments. Ensure environment variables and necessary settings are configured in the Azure portal.

## Contributing

1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```sh
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```sh
   git push origin feature/your-feature-name
   ```
5. Open a pull request.


## Acknowledgements

- Thanks to the developers of the scikit-learn and Flask libraries.
- Data sources: ECOTOX Database (US Environmental Protection Agency), ECHA.
- Deployment support from Microsoft Azure.

---

Feel free to customize the sections further based on your specific project details and requirements.
