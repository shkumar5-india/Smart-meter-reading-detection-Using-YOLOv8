# ⚡ Smart Meter Reading Detection

This project is a deep learning–based web application that automatically detects and reads electricity meter readings from images using **YOLOv8** object detection models.

Developed as a **Community Service Project (CSP)** by students of the **Department of Artificial Intelligence & Data Science**, this tool aims to automate the meter reading process with high accuracy and ease of use.

---

## 🧠 Key Features

- 🔍 **YOLOv8 Panel Detection** – Identifies the digital panel of the meter.
- 🔢 **Digit Detection** – Uses a second YOLOv8 model to extract digits from the panel.
- 📊 **Smart Reading Logic** – Sorts digits left-to-right to reconstruct the reading.
- 🖼️ **Image Visualization** – Shows original, cropped, and annotated outputs.
- 📱 **Mobile-Friendly Web App** – Use it directly from your phone browser.
- 🔐 **Offline Mobile App (In Progress)** – Planning to port as a fully offline Android/iOS app.

---

## 📸 Sample Output
![annotated_3442051338](https://github.com/user-attachments/assets/8adbe0f3-e1a8-4781-a8cd-120fc61a023f)
![3442051338](https://github.com/user-attachments/assets/1fd1ac9d-d57d-4e06-af39-313b75ae8407)
![cropped_3442051338](https://github.com/user-attachments/assets/0d42ce0c-3cd3-442e-8e99-2f06f65270f9)



## 🚀 Getting Started

### 📦 Prerequisites

- Python 3.8+
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- Flask
- OpenCV
- Pillow
