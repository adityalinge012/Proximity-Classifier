import pandas as pd

# Load dataset
data = pd.read_csv("dataset/touch_proximity_dataset.csv")

# Display first 5 rows
print(data.head())

# Display dataset information
print(data.info())

# Check missing values
print(data.isnull().sum())