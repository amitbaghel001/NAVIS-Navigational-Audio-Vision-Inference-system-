# 🌟 NAVIS AI —Navigational Audio & Vision Inference System

> An advanced multimodal AI navigation and auditory assistance system for visually impaired individuals.

<p align="center">
  <img src="https://img.shields.io/badge/Python-AI-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/YOLOv8-Object%20Detection-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Voice-AI%20Assistant-red?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-black?style=for-the-badge"/>
</p>

---

NAVIS AI acts as a reliable smart co-pilot for visually impaired individuals, transforming real-world scenes into rich auditory descriptions and intelligent voice interactions in real-time.

The system combines:
- 👁️ Real-time object detection
- 📏 Depth estimation
- 🎤 Voice interaction
- 🧠 Scene understanding
- 🚨 Safety-focused navigation assistance

to create an intelligent accessibility-focused AI system.

---

# 🧭 Architecture Overview

<p align="center">
  <img src="./screenshots/architecture.png" width="900"/>
</p>

<p align="center">
  <i>High-level workflow architecture of NAVIS AI</i>
</p>

---

# 🚀 Key Features

## 👁️ Real-time Object Detection
Identifies surrounding obstacles and objects using **YOLOv8**, enabling continuous environmental awareness and safer navigation.

---

## 📏 Depth & Distance Estimation
Accurately estimates obstacle distance using depth estimation models to help users understand nearby surroundings spatially.

---

## 🧠 Smart Scene Analyzer
Periodically summarizes the environment by:
- Tracking newly appearing objects
- Detecting missing objects
- Reducing repetitive auditory clutter

---

## 👤 Personalized Face Recognition
Recognizes familiar individuals dynamically, helping users identify nearby friends and family members.

---

## 🎤 Intelligent Voice Assistant
Interact seamlessly using voice commands for:
- Scene descriptions
- Calibration
- Status monitoring
- Navigation assistance

Fully hands-free and accessibility-oriented.

---

## 🚨 Emergency & GPS Support
Includes foundational support for:
- Location tracking
- Emergency workflows
- Safety-oriented interaction systems

---

## 🖥️ Graphical Control Interface
Provides a local PyQt5-based GUI for:
- Troubleshooting
- Monitoring system status
- Calibration control
- AI pipeline visualization

---

# 🎤 Sample Voice Commands

```text
"Describe the scene."
"Status."
"Calibrate."
"What's around me?"
```

---

# 🎮 Keyboard Controls

| Key | Function |
|------|----------|
| S | Trigger immediate scene summary |
| V | Start voice interaction mode |
| C | Manual depth calibration |
| M | Request calibration metrics |
| Q | Quit current process |

---

# 💻 Tech Stack

## Core Technologies
- Python
- PyTorch
- OpenCV
- YOLOv8
- MiDaS
- PyQt5

## AI / ML Components
- Object Detection
- Depth Estimation
- Scene Understanding
- Voice Interaction
- Audio Feedback Systems

---

# 📂 Project Structure

```bash
NAVIS-AI/
├── src/
│   ├── main.py              # Application Entry Point & NAVIS AI Core
│   ├── core/                # Detection, Depth, Audio & Tracking Systems
│   ├── ui/                  # PyQt5 Frontend Interface
│   └── utils/               # Configurations & Helper Modules
│
├── tests/                   # Base Unit Tests
├── test_basic.py            # Hardware Validation Script
├── requirements.txt         # Python Dependencies
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/amitbaghel001/NAVIS-AI-Assistive-Vision-System.git
cd NAVIS-AI-Assistive-Vision-System
```

---

## 2️⃣ Create Virtual Environment

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

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running NAVIS AI

```bash
python src/main.py
```

> On first launch, AI model weights may automatically download.

---

# 📸 Screenshots

> Add screenshots here:
- Live Detection View
- Depth Estimation Interface
- Voice Assistant Panel
- GUI Dashboard

Example:

```md
![NAVIS Dashboard](./screenshots/dashboard.png)
```

---

# 🌍 Vision & Impact

NAVIS AI was built with the goal of empowering visually impaired individuals through intelligent accessibility technology.

The project focuses on combining AI, computer vision, and real-time interaction systems to create safer and more independent navigation experiences.

---

# 🔮 Future Improvements

- Wearable smart-glass integration
- Real-time GPS navigation
- Edge-device optimization
- Multilingual voice assistant
- Mobile deployment
- AI-powered contextual assistance

---

# 👨‍💻 Author

## Amit Baghel

AI/ML Developer passionate about:
- Computer Vision
- Intelligent Systems
- Accessibility-focused AI
- Real-world AI applications

- LinkedIn: https://linkedin.com/in/amit0baghel
- GitHub: https://github.com/amitbaghel001

---

# ❤️ Final Note

> “Empowering visually impaired individuals to navigate the world with greater independence, awareness, and confidence.”

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
