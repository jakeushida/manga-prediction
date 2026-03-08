# One Piece Final Chapter Predictor

A data-driven web application that predicts the release date of future *One Piece* manga chapters based on over 25 years of historical publication data. The model underlying this predictor automatically updates every week with the latest release information.

🌍 **[Try the Predictor Here!](https://jakeushida.github.io/manga-prediction/)**

## Overview

This project consists of a Python data pipeline and a static web frontend:

- A web scraper fetches the latest chapter release dates from Jajanken.
- A Degree 2 Polynomial Regression model is trained on this data to capture the slowing release pace.
- A GitHub Actions workflow automates the scraping and training steps every Sunday, outputting the model's coefficients.
- A static frontend reads these coefficients to dynamically process user input and output predicted dates.

## Directory Structure

```text
├── .github/workflows/ 
│   └── update_predictor.yml  # GitHub Action that runs the scraper & model weekly
├── index.html                # Main webpage structure
├── style.css                 # Webpage styling
├── script.js                 # Frontend logic that applies the regression formula
├── scraper.py                # Python script to scrape data from Jajanken
├── chapter_data.csv          # Raw historical chapter data (auto-updated)
├── eda.ipynb                 # Jupyter Notebook containing Exploratory Data Analysis
├── model.py                  # Python script to train the polynomial regression model
├── model_parameters.json     # Serialized model coefficients (auto-updated)
└── requirements.txt          # Python dependencies for the backend scripts
```

## Running Locally

If you'd like to test the frontend locally:
1. Clone the repository.
2. Run a local web server (e.g., `python -m http.server`).
3. Visit `http://localhost:8000` in your browser.
