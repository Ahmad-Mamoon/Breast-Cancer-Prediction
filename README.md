# Breast Cancer Prediction Project

## Overview
This project aims to develop a predictive model for breast cancer diagnosis using the Breast Cancer Wisconsin (Diagnostic) Data Set obtained from Kaggle. The dataset contains features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass, and the task is to classify whether the mass is benign or malignant.

The model is trained using logistic regression and is deployed with Streamlit to provide an intuitive and interactive web interface for users to interact with the predictive model.

## Dataset
The dataset used in this project is sourced from [Kaggle's Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data). It comprises various features computed from digitized images of breast mass FNAs, along with the corresponding diagnosis (benign or malignant).

![Screenshot](/assets/image.png)

## Installation
To run the project locally, follow these steps:
1. Clone this repository:
    `git clone https://github.com/your-username/breast-cancer-prediction.git`
2. Install the required dependencies:
   `pip install -r requirements.txt`
4. Run the Streamlit app:
    `streamlit run app.py`


## Usage
Once the Streamlit app is running, open your web browser and navigate to the provided local URL. You can then interact with the app by inputting features related to breast mass characteristics and obtaining real-time predictions regarding the likelihood of malignancy.

## Acknowledgements
- The dataset used in this project is sourced from Kaggle's Breast Cancer Wisconsin (Diagnostic) Data Set.
- Special thanks to the Streamlit team for providing an intuitive framework for building interactive web applications.
