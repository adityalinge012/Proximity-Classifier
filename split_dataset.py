import pandas as pd
from sklearn.model_selection import train_test_split
from load_dataset import data

# Input feature
X = data[["distance_cm"]]

# Output target
y = data["class"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training data:", len(X_train))
print("Testing data:", len(X_test))