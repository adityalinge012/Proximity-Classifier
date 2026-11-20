import pandas as pd
import joblib
from load_dataset import data

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from split_dataset import (
    X,
    y,
    X_train,
    X_test, 
    y_train, 
    y_test
)



# Create Decision Tree model
model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Save trained model
joblib.dump(model, "proximity_model.pkl")

print("Decision Tree Model Trained Successfully!")