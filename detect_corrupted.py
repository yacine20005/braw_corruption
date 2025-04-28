import cv2, os, numpy as np
from skimage.metrics import structural_similarity as ssim

FOLDER = "frames"
THREESHOLD = 0.25 

frames = sorted([f for f in os.listdir(FOLDER) if f.endswith(".png")])
corrupted = []

prev = cv2.imread(os.path.join(FOLDER, frames[0]))
for i, frame in enumerate(frames[1:]):
    current = cv2.imread(os.path.join(FOLDER, frame))
    
    if current is None or current.mean() < 10:
        corrupted.append(i+1)
        continue
        
    gray_prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    gray_current = cv2.cvtColor(current, cv2.COLOR_BGR2GRAY)
    s = ssim(gray_prev, gray_current)
    
    if s < THREESHOLD:
        corrupted.append(i+1)
    
    prev = current

with open("corrupted.txt", "w") as f:
    f.write(",".join(map(str, corrupted)))