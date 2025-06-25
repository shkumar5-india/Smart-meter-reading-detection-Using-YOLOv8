import os
from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
from ultralytics import YOLO

app = Flask(__name__)

# Paths to YOLO models
PANEL_MODEL_PATH = r'D:\Reading of Meter\best.pt'
DIGIT_MODEL_PATH = r'D:\Reading of Meter\first.pt'

# Ensure models exist
if not os.path.exists(PANEL_MODEL_PATH):
    raise FileNotFoundError(f"Panel model not found at: {PANEL_MODEL_PATH}")
if not os.path.exists(DIGIT_MODEL_PATH):
    raise FileNotFoundError(f"Digit model not found at: {DIGIT_MODEL_PATH}")

# Load models
panel_model = YOLO(PANEL_MODEL_PATH)
digit_model = YOLO(DIGIT_MODEL_PATH)

# Upload folder
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    meter_reading = None
    original_image = None
    cropped_panel_image = None
    annotated_image = None

    if request.method == 'POST':
        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', error="No image selected.")

        filename = file.filename
        saved_image_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(saved_image_path)

        original_image = 'uploads/' + filename  # relative path

        # Convert to OpenCV format for panel detection
        image_cv2 = cv2.imread(saved_image_path)

        # Detect panel
        panel_results = panel_model(saved_image_path)
        panel_boxes = panel_results[0].boxes

        if len(panel_boxes) == 0:
            return render_template('index.html', error="No panel detected.", original_image=original_image)

        # Crop panel
        x1, y1, x2, y2 = map(int, panel_boxes[0].xyxy[0])
        cropped_panel = image_cv2[y1:y2, x1:x2]
        cropped_filename = f"cropped_{filename}"
        cropped_path = os.path.join(UPLOAD_FOLDER, cropped_filename)
        cv2.imwrite(cropped_path, cropped_panel)

        cropped_panel_image = 'uploads/' + cropped_filename

        # Detect digits on cropped panel
        cropped_pil = Image.open(cropped_path).convert("RGB")
        results = digit_model(cropped_pil)
        class_names = digit_model.names
        boxes = results[0].boxes

        draw = ImageDraw.Draw(cropped_pil)
        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            font = ImageFont.load_default()

        digits = []

        for box, cls_id in zip(boxes.xyxy, boxes.cls):
            x1, y1, x2, y2 = map(int, box.tolist())
            label = class_names[int(cls_id)]
            cx = (x1 + x2) / 2

            if label.isdigit() or label == '.':
                digits.append((cx, label))
                draw.rectangle([x1, y1, x2, y2], outline='red', width=2)
                draw.text((x1, y1 - 10), label, fill='red', font=font)

        digits.sort(key=lambda x: x[0])
        meter_reading = ''.join([label for _, label in digits])

        # Save annotated image
        annotated_filename = 'annotated_' + filename
        annotated_path = os.path.join(UPLOAD_FOLDER, annotated_filename)
        cropped_pil.save(annotated_path)

        annotated_image = 'uploads/' + annotated_filename

    return render_template('index.html',
                           meter_reading=meter_reading,
                           original_image=original_image,
                           cropped_panel_image=cropped_panel_image,
                           annotated_image=annotated_image)

if __name__ == '__main__':
    app.run(debug=True)
