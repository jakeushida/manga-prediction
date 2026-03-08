# One Piece Final Chapter Predictor

A web application that predicts the release date of future *One Piece* manga chapters based on a polynomial regression model trained on past chapter release dates. The model underlying this predictor automatically updates every week with the latest release information.

**[Try the Predictor Here!](https://jakeushida.github.io/manga-prediction/)**

## Overview

This project consists of a Python data pipeline and a static web frontend:

- A web scraper fetches the latest chapter release dates from Jajanken.
- A Degree 2 Polynomial Regression model is trained on this data.
- A GitHub Actions workflow automates the scraping and training steps every week, outputting the model's parameters.
- A static frontend reads these parameters to dynamically process user input and output predicted dates.

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
├── model_parameters.json     # Stores intercept, coefficients, and base date
└── requirements.txt          # Python dependencies for the backend scripts
```
