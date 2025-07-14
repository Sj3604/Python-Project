# 👁️ Real-Time Face Detection with OpenCV

Welcome to a beginner-friendly project that uses **OpenCV** and **Haar Cascade Classifier** to detect human faces in real time using your webcam! 🎥💻

---

## 📌 About the Project

This Python project captures video from your webcam and highlights detected human faces with rectangles — live! It's a great starting point to explore computer vision and real-time image processing.

---

## 🛠️ Technologies Used

- 🐍 Python
- 📷 OpenCV
- 🧠 Haarcascade XML Classifier

---

## 📂 Files

- `face_detector.py`: Main Python script
- Uses: `haarcascade_frontalface_default.xml` (automatically loaded from OpenCV)

---

## 📸 How It Works

1. Loads the Haar cascade face detector from OpenCV
2. Accesses your webcam
3. Reads video frames continuously
4. Converts frames to grayscale (for better detection performance)
5. Detects faces and draws rectangles around them
6. Press a key to exit the window

---

## 🚀 Getting Started

### 1. Install OpenCV

```bash
pip install opencv-python
