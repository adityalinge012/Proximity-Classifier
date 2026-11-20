
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Load dataset
data = pd.read_csv("dataset/touch_proximity_dataset.csv")

# Load trained Decision Tree model
model = joblib.load("proximity_model.pkl")

# Create two graphs
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Graph 1: Dataset visualization
colors = {
    "Near": "red",
    "Medium": "orange",
    "Far": "green"
}

for class_name, color in colors.items():
    subset = data[data["class"] == class_name]

    axes[0].scatter(
        subset["distance_cm"],
        [class_name] * len(subset),
        color=color,
        label=class_name,
        alpha=0.5
    )

axes[0].set_title("Touch / Proximity Dataset")
axes[0].set_xlabel("Distance (cm)")
axes[0].set_ylabel("Class")
axes[0].legend()
axes[0].grid(True)

# Graph 2: Trained Decision Tree
plot_tree(
    model,
    feature_names=["Distance (cm)"],
    class_names=model.classes_,
    filled=True,
    rounded=True,
    ax=axes[1]
)

axes[1].set_title("Trained Decision Tree Model")

plt.tight_layout()
plt.show()
