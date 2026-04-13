# 🐒 Monkey Guard System (AI-Based Intrusion Detection)

## Overview

The **Monkey Guard System** is an AI-powered real-time detection and deterrence system designed to prevent monkey intrusions in residential areas, farms, hostels, and public spaces.

The system uses **computer vision and deep learning (YOLOv5)** deployed on a **Raspberry Pi** to detect monkeys from live video feeds and automatically trigger an alarm system to deter them.

This project focuses on providing a **low-cost, scalable, and autonomous wildlife monitoring solution** to reduce human-wildlife conflict.

---

# Project Objectives

- Develop an automated monkey detection system using AI  
- Enable real-time monitoring using Raspberry Pi and camera module  
- Trigger an alarm system to deter monkey intrusions  
- Provide an affordable and scalable security solution  
- Minimize property damage and improve human safety  

---

# System Architecture

![System Architecture](docs/system_architecture.png)

The system consists of the following components:

* **Camera Module** – Captures real-time video feed  
* **Raspberry Pi 4** – Processes frames and runs AI model  
* **YOLOv5 Model** – Detects monkeys in real time  
* **Detection Logic** – Confirms intrusion based on time threshold  
* **Alarm System** – Activates siren for deterrence  

---

# Working Principle

1. Camera continuously captures live video  
2. Frames are processed using the YOLOv5 model  
3. If a monkey is detected continuously for **5 seconds**, intrusion is confirmed  
4. Alarm system is triggered for **25 seconds**  
5. System resets once the monkey leaves the frame  

---

# System Specifications

| Feature              | Specification                     |
|---------------------|----------------------------------|
| Processing Unit     | Raspberry Pi 4                   |
| Detection Model     | YOLOv5                           |
| Input               | Live Camera Feed                 |
| Detection Type      | Real-Time Object Detection       |
| Alarm Duration      | 25 seconds                       |
| Confirmation Time   | 5 seconds                        |
| Deployment          | Edge Device (Standalone System)  |

---

# AI Model Details

- **Model Used:** YOLOv5  
- **Framework:** PyTorch  
- **Dataset:**
  - COCO Dataset (base training)
  - Custom Monkey Dataset (~5000 images)  
- **Classes Detected:** Monkey (various poses and group scenarios)  

---

# Hardware Components

- Raspberry Pi 4  
- Camera Module  
- Buzzer / Speaker (Alarm System)  
- Power Supply (Battery / Optional Solar)  

---

# Software Stack

- Python  
- OpenCV  
- PyTorch  
- YOLOv5  
- NumPy  

---


# Detection Algorithm

The system uses a **time-based confirmation mechanism**:

- Detection must persist for **5 continuous seconds**
- Reduces false positives from noise or temporary objects
- Ensures reliable intrusion detection

---

# Alarm System

- Triggered after confirmed detection  
- Runs for **25 seconds**  
- Stops early if the monkey exits the frame  
- Uses high-frequency sound for deterrence  

---

# Simulation & Testing

- Tested in real-world environments:
  - Farms  
  - Residential areas  
  - Open spaces  

- Metrics Evaluated:
  - Detection Accuracy  
  - False Alarm Rate  
  - Response Time  

---

# Limitations

- Performance depends on lighting conditions  
- Limited by Raspberry Pi processing power  
- Requires retraining for different environments  

---

# Future Improvements

The following features are planned but not yet implemented:

- Mobile App Integration (real-time alerts)  
- Thermal Imaging (night detection)  
- Automated Water Sprinkler System  
- Multi-camera support  
- Solar-powered deployment  

---

# Applications

- Agricultural fields  
- Residential areas  
- Hostels and campuses  
- Wildlife monitoring zones  

---

# Author

**Naren**  
ECE Student  

### Interests:
- AI & Machine Learning  
- Embedded Systems  
- Computer Vision  
- Digital System Design  

---

# License

This project is licensed under the MIT License.