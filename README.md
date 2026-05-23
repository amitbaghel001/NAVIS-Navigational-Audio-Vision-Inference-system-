# 🌟 NAVIS AI — Assistive Vision & Navigation System

> AI-powered assistive navigation system for visually impaired users using computer vision, depth estimation, voice interaction, and real-time scene understanding.

<p align="center">
  <img src="https://img.shields.io/badge/Computer%20Vision-AI-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Depth%20Estimation-MiDaS-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Voice%20Assistant-Offline-red?style=for-the-badge"/>
</p>

---

# 🚀 Overview

NAVIS AI is an intelligent multimodal assistive system designed to help visually impaired individuals navigate their surroundings independently and safely.

The system combines:
- Real-time object detection
- Depth estimation
- Voice interaction
- Scene understanding
- Smart auditory feedback

to create an AI-powered navigation companion capable of understanding and describing the environment in real time.

---

# 🌍 Problem Statement

Visually impaired individuals often face challenges in:
- Detecting nearby obstacles
- Understanding surrounding environments
- Navigating unfamiliar spaces safely
- Accessing contextual real-time information

NAVIS AI was built to bridge this accessibility gap through intelligent AI-assisted environmental awareness.

---

# 🌟 Core Features

## 👁️ Real-Time Object Detection
- Detects multiple real-world objects using YOLOv8
- Provides live obstacle awareness
- Tracks dynamic environmental changes

---

## 📏 Depth & Distance Estimation
- Uses MiDaS depth estimation
- Calculates approximate obstacle distances
- Helps improve navigation safety

---

## 🧠 Smart Scene Understanding
- Generates periodic scene summaries
- Identifies newly appearing or missing objects
- Reduces unnecessary auditory clutter

---

## 🎤 Intelligent Voice Assistant
- Hands-free voice interaction
- Voice-triggered commands
- Audio-based environmental feedback

Sample Commands:
- "Describe the scene"
- "System status"
- "Start calibration"

---

## 👤 Personalized Face Recognition
- Recognizes familiar individuals
- Provides contextual auditory alerts
- Enhances social awareness

---

## 🚨 Emergency & GPS Support
- Emergency assistance capability
- Location-aware navigation support
- Safety-oriented workflow integration

---

# 🧠 AI Technologies Used

- YOLOv8
- OpenCV
- MiDaS Depth Estimation
- Speech Recognition
- Audio Synthesis
- Real-time Video Processing
- Computer Vision Pipelines

---

# 🏗️ System Architecture

```text
Camera Feed
      ↓
Object Detection (YOLOv8)
      ↓
Depth Estimation (MiDaS)
      ↓
Scene Understanding Engine
      ↓
Voice Feedback System
      ↓
User Interaction Layer
```

---

# 🛠️ Tech Stack

## Core Technologies
- Python
- OpenCV
- PyTorch
- YOLOv8
- MiDaS
- PyQt5

## AI / ML
- Object Detection
- Depth Estimation
- Scene Understanding
- Voice Interaction

---

# 📂 Project Structure

```bash
NAVIS-AI/
│
├── src/
│   ├── main.py
│   ├── core/
│   ├── ui/
│   └── utils/
│
├── tests/
├── test_basic.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/amitbaghel001/NAVIS-AI.git
cd NAVIS-AI
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the System

```bash
python src/main.py
```

On first execution, required AI models may automatically download.

---

# 🎮 Controls

| Key | Function |
|-----|----------|
| S | Generate scene summary |
| V | Start voice interaction |
| C | Manual calibration |
| M | System status |
| Q | Quit application |

---

# 📸 Screenshots

> Add screenshots here:
- Live Detection Interface
- Depth Estimation View
- GUI Dashboard
- Voice Interaction Window

Example:

```md
![NAVIS Dashboard](./screenshots/dashboard.png)
```

---

# 🌟 Future Improvements

- Edge-device optimization
- Wearable hardware integration
- Multilingual voice assistant
- Real-time GPS navigation
- RAG-powered environmental assistance
- Mobile application deployment

---

# 👨‍💻 Author

## Amit Baghel

AI/ML Developer passionate about building intelligent systems, accessibility-focused AI products, and real-world automation solutions.

- LinkedIn: https://linkedin.com/in/amit0baghel
- GitHub: https://github.com/amitbaghel001

---

# ❤️ Impact Vision

> “Empowering visually impaired individuals to navigate the world with greater independence, awareness, and confidence.”

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
