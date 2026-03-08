# One Piece Final Chapter Predictor

## 1. Project Objective
The goal of this project is to build a data-driven forecasting tool that predicts the release date of the final chapter of the manga *One Piece*. Users can input a hypothetical final chapter number, and the system will output an estimated release date based on historical publication trends.

## 2. Data Source
- **Target Site:** Jajanken - One Piece Shonen Jump Data
- **Data Points:** Chapter numbers, Weekly Shonen Jump issue dates, magazine rankings, and hiatus frequency.

## 3. System Architecture
The project utilizes a fully automated, serverless pipeline:
- **Ingestion (Scraping):** A Python script using BeautifulSoup (or Playwright) to extract the latest chapter data from Jajanken.
- **Automation (Trigger):** GitHub Actions runs the scraper on a weekly CRON schedule (following the release of new Shonen Jump issues).
- **Modeling (Analysis):**
  - A Python-based Polynomial Regression model trained on historical release dates vs. chapter numbers.
  - The model accounts for the slowing cadence of releases (Oda’s breaks) over time.
- **Storage:** The processed data and model coefficients are stored as `.json` or `.csv` files within the GitHub repository.
- **Deployment (Frontend):** A static web interface hosted on Vercel or GitHub Pages that allows users to query the model.

## 4. Technical Stack
- **Language:** Python 3.x
- **Libraries:** `requests`, `beautifulsoup4`, `pandas`, `scikit-learn`, `numpy`
- **Automation:** GitHub Actions
- **Frontend:** HTML/JavaScript (to consume pre-computed model coefficients)

## 5. Development Roadmap
- [x] **Phase 1:** Develop and test the Jajanken scraper.
- [x] **Phase 2:** Perform Exploratory Data Analysis (EDA) on release intervals.
- [x] **Phase 3:** Build and validate the Polynomial Regression model.
- [x] **Phase 4:** Set up the GitHub Action automation.
- [ ] **Phase 5:** Build the web-based "Predictor" UI.

> **Note:** Ignore the `polynomial_regression.ipynb`, `polynomial_regression.py`, and `service_account.json` files for now.