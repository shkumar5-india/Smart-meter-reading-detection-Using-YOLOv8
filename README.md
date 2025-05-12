**Change The Branch from main to master to view the project code**

                    (or)
**Follow The Link to view the code : 

https://github.com/shkumar5-india/Smart-meter-reading-detection-Using-YOLOv8/tree/master

**


Smart Meter Reading Detection Using Deep Learning

This project aims to automate the process of reading electricity meter values from images using deep learning. The solution uses computer vision techniques to detect the LED display panel and extract numeric readings accurately, even under varied conditions like angles, lighting, and obstructions.



Features

Automatic Detection: Locates the LED panel on the electric meter image.

Digit Segmentation: Identifies individual digits from the panel.

Support for Variability: Handles different meter types, angles, and lighting conditions.



Training

1. Panel Detection (YOLOv8)

yolo task=detect mode=train data=panel_data.yaml model=yolov8n.pt epochs=100 imgsz=640

2. Digit Detection (YOLOv8/CNN)

yolo task=detect mode=train data=digits_data.yaml model=yolov8n.pt epochs=100 imgsz=640



Output

Annotated image with bounding box around the LED panel

Final meter reading printed in Front-end Page
