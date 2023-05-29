import cv2
import numpy as np

# Load the image
try:
    image = cv2.imread('image/1.png')

    # Check if the image is empty
    if image is None:
        print("The image could not be loaded or is a blank image.")

    while True:
        # Show the original image
        cv2.imshow('Original Image', image)

        # Print the menu options
        print("Image Processing Options:")
        print("b: Blurring")
        print("s: Sharpening")
        print("e: Edge Detection")
        print("c: Increase Contrast")
        print("h: Histogram Equalization")
        print("q: Quit")

        # Wait for user key press
        key = cv2.waitKey(0)

        # Check the pressed key
        if key == ord('b'):
            # Blurring
            blurred = cv2.GaussianBlur(image, (5, 5), 0)
            cv2.imshow('Blurred Image', blurred)
            cv2.imwrite('processed_image/blurred.png', blurred)
        elif key == ord('s'):
            # Sharpening
            kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
            sharpened = cv2.filter2D(image, -1, kernel)
            cv2.imshow('Sharpened Image', sharpened)
            cv2.imwrite('processed_image/sharpened.png', sharpened)
        elif key == ord('e'):
            # Edge detection
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            cv2.imshow('Edge Detection', edges)
            cv2.imwrite('processed_image/edges.png', edges)
        elif key == ord('c'):
            # Increase Contrast
            alpha = 1.5
            adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
            cv2.imshow('Increased Contrast', adjusted)
            cv2.imwrite('processed_image/contrast.png', adjusted)
        elif key == ord('h'):
            # Histogram Equalization
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            equalized = cv2.equalizeHist(gray)
            cv2.imshow('Histogram Equalization', equalized)
            cv2.imwrite('processed_image/histogram_equalization.png', equalized)
        elif key == ord('q'):
            # Quit the program
            break
        else:
            print("You entered an incorrect key! Please enter a valid option.")

    # Close all windows
    cv2.destroyAllWindows()

except cv2.error as e:
    print("Error", e)