import cv2
import numpy as np

def preprocess_frame(frame):
    # Color Correction
    corrected_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Contrast Enhancement using CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    lab = cv2.cvtColor(corrected_frame, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    l2 = clahe.apply(l)
    lab = cv2.merge((l2, a, b))
    enhanced_frame = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
    
    # Noise Reduction using Gaussian Blur
    final_frame = cv2.GaussianBlur(enhanced_frame, (5, 5), 0)
    
    return final_frame
