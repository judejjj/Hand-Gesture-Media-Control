import cv2
import mediapipe as mp
import pyautogui
import time  

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=1)

cap = cv2.VideoCapture(0)

# Timer to prevent rapid actions
last_action_time = 0  
cooldown_time = 0.5  # Time interval in seconds (adjust as needed)

def detect_fingers(hand_landmarks):
    """Detects the number of extended fingers and controls media with delay."""
    global last_action_time
    current_time = time.time()

    landmarks = hand_landmarks.landmark

    thumb_tip, thumb_ip = landmarks[4], landmarks[3]
    index_tip, index_pip = landmarks[8], landmarks[6]
    middle_tip, middle_pip = landmarks[12], landmarks[10]
    ring_tip, ring_pip = landmarks[16], landmarks[14]
    pinky_tip, pinky_pip = landmarks[20], landmarks[18]

    fingers_up = {
        "Thumb": thumb_tip.x > thumb_ip.x if hand_landmarks.landmark[5].x > hand_landmarks.landmark[17].x else thumb_tip.x < thumb_ip.x,
        "Index": index_tip.y < index_pip.y,
        "Middle": middle_tip.y < middle_pip.y,
        "Ring": ring_tip.y < ring_pip.y,
        "Pinky": pinky_tip.y < pinky_pip.y
    }

    count = sum(fingers_up.values())  # Count fingers up

    # Only trigger action if cooldown time has passed
    if current_time - last_action_time > cooldown_time:
        if count == 1:
            pyautogui.press("right")  # Seek Forward
        elif count == 2:
            pyautogui.press("left")  # Seek Backward
        elif count == 3:
            pyautogui.press("up")  # Volume Up
        elif count == 4:
            pyautogui.press("down")  # Volume Down
        elif count == 5:
            pyautogui.press("space")  # Play/Pause
        elif count == 0:
            pyautogui.press("m")  # Mute
        
        last_action_time = current_time  # Update last action time

    print(f"Detected: {count} Fingers Up")  # Output to terminal

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        # Process only the first detected hand
        detect_fingers(result.multi_hand_landmarks[0])

    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break

cap.release()
cv2.destroyAllWindows()
