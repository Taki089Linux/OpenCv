import cv2
import numpy as np

# Initialize video capture object for the default webcam
cap = cv2.VideoCapture(0)

# Initialize background subtractor for motion detection
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Apply the background subtractor to get the foreground mask
    fgmask = fgbg.apply(frame)

    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw lines on the frame based on detected contours
    for cnt in contours:
        # Filter out small contours
        if cv2.contourArea(cnt) > 500:
            # Approximate the contour to a polygon
            approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
            x, y, w, h = cv2.boundingRect(cnt)

            # Draw the bounding box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Draw lines for head, body, hands, and feet
            cv2.line(frame, (x + w//2, y), (x + w//2, y + h//3), (0, 0, 255), 2)  # Head
            cv2.line(frame, (x + w//2, y + h//3), (x + w//2, y + 2*h//3), (0, 255, 0), 2)  # Body
            cv2.line(frame, (x, y + h//3), (x + w, y + h//3), (255, 0, 0), 2)  # Hands
            cv2.line(frame, (x + w//4, y + 2*h//3), (x + 3*w//4, y + 2*h//3), (0, 255, 255), 2)  # Feet

    # Display the resulting frame
    cv2.imshow('Motion Detection with RGB Lines', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()