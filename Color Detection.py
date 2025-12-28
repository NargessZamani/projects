import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame from BGR to HSV color space
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define purple color range in HSV
    lower_purple = np.array([125, 50, 50])
    upper_purple = np.array([155, 255, 255])

    # Create mask for purple color
    mask_purple = cv2.inRange(frame_hsv, lower_purple, upper_purple)

    # Apply mask to original frame
    frame_masked = cv2.bitwise_and(frame, frame, mask=mask_purple)

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Purple Mask", mask_purple)
    cv2.imshow("Detected Purple", frame_masked)

    if cv2.waitKey(5) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
