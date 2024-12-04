import cv2 
from ultralytics import YOLO
import numpy as np 

def load_yolo_model(model_path):
    """Load YOLO model with the given path."""
    return YOLO(model_path)

def detect_objects(model, frema, class_name, display_width):
    """Detect segm"""