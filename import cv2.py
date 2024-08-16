import cv2

# Start the webcam
cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    ret, frame1 = cap1.read()

    # Display the resulting frame
    cv2.imshow('Webcam', frame)
    cv2.imshow('Webcam', frame1)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()
cap1.release()
cv2.destroyAllWindows()