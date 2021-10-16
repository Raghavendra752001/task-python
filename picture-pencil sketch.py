# task-python
 import cv2
 image = cv2.imread(" dog.jpg")
 gray_image = cv2.cvtcolor(image, cv2.Color_BGR2GRAY)
 inverted_image = 255 - gray image 
 blurred = cv2.GaussianBlur(inverted image,(21,21),0)
 inverted_blur = 255-blurred
 pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
 cv2.imshow("Original Image",image)
 cv2.imshow("Pencil Sketch of iamge",pencil_sketch)
 cv2.waitKey(0)