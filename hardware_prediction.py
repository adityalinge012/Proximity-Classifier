import serial
import time
import pandas as pd
import keyboard
from train_model import model

# Connect Arduino
arduino = serial.Serial("COM3", 9600, timeout=2)

time.sleep(2)

arduino.reset_input_buffer()

print("TOUCH PROXIMITY CLASSIFIER")
print("Press S to START")
print("Press Q to EXIT")

running = False

try:
    while True:

        if keyboard.is_pressed("q"):
            print("Program stopped.")
            break

        if keyboard.is_pressed("s"):
            running = True
            print("Sensor reading started!")
            time.sleep(0.3)

        if running:

            reading = arduino.readline().decode(
                "utf-8", errors="ignore"
            ).strip()

            try:
                distance = float(reading)

                if distance < 0:
                    continue

                input_data = pd.DataFrame({
                    "distance_cm": [distance]
                })

                prediction = model.predict(input_data)[0]

                print("Distance:", round(distance, 2), "cm")
                print("Classification:", prediction)
                print("------------------------")

            except ValueError:
                pass

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    arduino.close()