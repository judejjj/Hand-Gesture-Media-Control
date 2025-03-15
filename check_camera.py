import cv2

cap = cv2.VideoCapture(0)  # Open default camera (change 0 to 1 if needed)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        break
    
    cv2.imshow("Camera Test", frame)  # Display camera feed

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
