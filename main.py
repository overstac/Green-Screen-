import cv2
import numpy as np

foreground= cv2.imread("giraffe.jpeg")
background= cv2.imread("safari.jpeg")

print(foreground[40, 40])
width= foreground.shape[1]
height= foreground.shape[0]

resized_back= cv2.resize(background, (width, height))

for i in range(width):
    for j in range (height):
        pixel= foreground[j,i]
        if np.any(pixel == [28, 255, 76]):
            foreground[j, i] = resized_back[j, i]

cv2.imwrite("output.jpeg", foreground)