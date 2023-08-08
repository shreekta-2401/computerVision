import cv2
import numpy as np


def color_detection(image_path, lower_color_range, upper_color_range):
    # Load the input image
    image = cv2.imread(image_path)

    # Convert BGR image to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Create a mask for the specified color range
    mask = cv2.inRange(hsv_image, lower_color_range, upper_color_range)

    # Bitwise-AND the mask and original image
    result = cv2.bitwise_and(image, image, mask=mask)

    # Display the result
    cv2.imshow('Color Detection', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Specify the lower and upper bounds of the blue color range (in HSV)
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])
input_image_path = r'C:\Users\lenovo\Pictures\flowers\Butterfly-bannerghatta-pictures.jpg'
color_detection(input_image_path, lower_blue, upper_blue)
