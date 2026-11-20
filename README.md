# AI-Based Touch / Proximity Classifier

An Arduino and Machine Learning-based project that detects the distance of nearby objects using an ultrasonic sensor and classifies them into three categories: **Near, Medium, and Far**.

The project uses a Decision Tree Classification algorithm to predict the proximity category based on distance measurements.

## Project Overview

The system uses an HC-SR04 ultrasonic sensor connected to an Arduino Nano to measure the distance of nearby objects.

The collected distance values are processed using a trained Machine Learning model, which predicts whether an object is Near, Medium, or Far.

## Features

- Real-time distance measurement using an ultrasonic sensor.
- Object proximity classification into Near, Medium, and Far.
- Machine Learning prediction using Decision Tree Classifier.
- Dataset loading and preprocessing.
- Model training and evaluation.
- Graphical visualization of the dataset and trained Decision Tree.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Arduino Nano | Hardware controller |
| HC-SR04 | Distance measurement |
| Scikit-learn | Machine Learning model |
| Pandas | Dataset handling |
| NumPy | Numerical operations |
| Matplotlib | Data and model visualization |
| PySerial | Arduino-Python communication |
| Joblib | Saving and loading the trained model |

## Machine Learning Algorithm

**Decision Tree Classifier**

The Decision Tree algorithm learns classification rules from distance measurements and predicts the corresponding proximity category.

Input Feature:
- `distance_cm`

Output Classes:
- Near
- Medium
- Far

## Hardware Requirements

- Arduino Nano (CH340)
- HC-SR04 Ultrasonic Sensor
- Jumper Wires
- USB Cable

## Circuit Connections

| HC-SR04 Pin | Arduino Nano |
|---|---|
| VCC | 5V |
| GND | GND |
| TRIG | D9 |
| ECHO | D10 |

## Project Structure

```text
Touch_Proximity_Classifier/
│
├── dataset/
│   └── touch_proximity_dataset.csv
│
├── load_dataset.py
├── split_dataset.py
├── train_model.py
├── evaluate_model.py
├── predict.py
├── hardware_prediction.py
├── visualize_live.py
│
├── proximity_model.pkl
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd Touch_Proximity_Classifier
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

Windows:

```bash
.venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install -r requirements.txt
```

## How to Run

Run the following files in order:

**Step 1: Load Dataset**

```bash
python load_dataset.py
```

**Step 2: Split Dataset**

```bash
python split_dataset.py
```

**Step 3: Train Machine Learning Model**

```bash
python train_model.py
```

**Step 4: Evaluate Model**

```bash
python evaluate_model.py
```

**Step 5: Visualize Dataset and Decision Tree**

```bash
python visualize_live.py
```

**Step 6: Run Hardware-Based Prediction**

```bash
python hardware_prediction.py
```

Make sure to select the correct Arduino COM port in the Python code before running hardware prediction.

## Project Workflow

1. Ultrasonic sensor measures the distance of an object.
2. Arduino reads the sensor measurement.
3. Distance data is sent to Python through serial communication.
4. The trained Decision Tree model processes the distance value.
5. The model predicts the proximity category.
6. The result is displayed to the user.

## Applications

- Smart object detection systems.
- Proximity-based automation.
- Contactless distance monitoring.
- Basic obstacle detection systems.
- Educational IoT and Machine Learning applications.

## Future Scope

- Collect real-world sensor data for model training.
- Improve classification accuracy with more sensor readings.
- Explore additional Machine Learning algorithms such as KNN.
- Develop a graphical user interface for live monitoring.
- Integrate the system with IoT-based applications.

## Author

**Aditya Mohan Linge**

B.Tech – Computer Science and Engineering (AI & ML)

---

*This project is developed for educational purposes to demonstrate the integration of Arduino, Python, and Machine Learning.*
