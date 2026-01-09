# Real-Time Drowsiness Detection Application

# Introduction :
Driver drowsiness is one of the most underestimated causes of road accidents. Unlike speeding or drunk driving, fatigue develops gradually and often goes unnoticed by the driver. This project focuses on detecting early signs of drowsiness using computer vision techniques and providing timely alerts to reduce the risk of accidents.

The Real-Time Drowsiness Detection App continuously analyzes facial cues and eye behavior through a live camera feed to identify fatigue in real time.

# Motivation :
During long drives or night shifts, drivers may experience reduced alertness due to lack of sleep, stress, or medical conditions. Traditional safety measures do not actively monitor a driver’s condition. This project was built to explore how computer vision and lightweight machine learning techniques can be used to improve road safety without relying on expensive hardware or intrusive sensors.

# System Overview :
The application processes a real-time video stream and performs the following steps:
1. Detects the driver’s face and eyes using Haar Cascade classifiers.
2. Extracts facial landmarks around the eyes.
3. Computes the Eye Aspect Ratio (EAR) to determine whether the eyes are open or closed.
4. Monitors eye closure duration to identify signs of drowsiness.
5. Triggers an alert when the EAR remains below a defined threshold for a specific time period.

This approach allows the system to respond quickly while remaining computationally efficient.

# Key Features :
Real-time face and eye detection using a webcam
Eye Aspect Ratio (EAR) based fatigue analysis
Immediate alerts to warn the driver
Lightweight and efficient processing
Privacy focused design with no data storage

# Technologies Used :
* Python - Core programming language

* OpenCV - Image processing and real-time video analysis

* Haar Cascades - Face and eye detection

* Eye Aspect Ratio (EAR) - Drowsiness detection logic

* Machine Learning concepts - Feature analysis and thresholding

# Privacy Considerations :
User privacy was a key design consideration in this project. All processing is done locally and in real time. No images, videos, or personal data are stored or transmitted, ensuring complete user confidentiality.

# Results :
The system is capable of reliably detecting prolonged eye closure and issuing alerts in real time. It performs well under normal lighting conditions and demonstrates how simple yet effective computer vision techniques can be applied to real world safety problems.

# Limitations :
Performance may degrade under poor lighting conditions
Does not account for head pose or yawning detection
Requires a stable camera position

# Future Improvements :
Integration of head pose and yawn detection
Support for low light environments
Mobile application deployment
Improved alert mechanisms (audio + vibration)

# Timeline :
September 2024 - December 2025



