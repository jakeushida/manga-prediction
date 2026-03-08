import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import json

df = pd.read_csv('chapter_data.csv')

# Convert chapter column from text to numbers
# 'coerce' turns any text that isn't a number into NaN
df['chapter'] = pd.to_numeric(df['chapter'], errors='coerce')

# Convert date column into a proper Datetime object
df['date'] = pd.to_datetime(df['date'])

# Drop any rows where chapter became NaN
df = df.dropna(subset='chapter')

# Keep only rows where chapter number is greater than 0
df = df[df['chapter'] > 0]

# Get integers representing days since first release
df['Days since first release'] = (df['date'] - df['date'].min()).dt.days

X = df[['chapter']]
y = df['Days since first release']

# Transform chapter number into their polynomial versions 
poly_transformer = PolynomialFeatures(degree=2)
X_poly = poly_transformer.fit_transform(X)

# Build the model
model = LinearRegression()
model.fit(X_poly, y)

# Extract intercept & coefficients
intercept = model.intercept_
coefficients = model.coef_.tolist()

# Get first release date 
base_date = df['date'].min().strftime('%Y-%m-%d')

model_data = {
    "intercept": intercept,
    "coefficients": coefficients,
    "base_date": base_date
}

with open("model_parameters.json", "w") as f:
    json.dump(model_data, f)