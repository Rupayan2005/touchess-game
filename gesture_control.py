import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

# Mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Swipe detection variables
prev_x, prev_y = 0, 0
swipe_threshold = 60  # Minimum pixel movement to count as swipe
cooldown = 1.0        # Minimum seconds between swipes
last_swipe_time = time.time()

# Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)  # Mirror image
    h, w, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Index fingertip position (landmark 8)
            x = int(hand_landmarks.landmark[8].x * w)
            y = int(hand_landmarks.landmark[8].y * h)

            dx = x - prev_x
            dy = y - prev_y

            # Only trigger swipe if enough time has passed
            current_time = time.time()
            if current_time - last_swipe_time > cooldown:
                if abs(dx) > abs(dy) and abs(dx) > swipe_threshold:
                    if dx > 0:
                        print("➡️ Swipe Right")
                        pyautogui.press('right')
                    else:
                        print("⬅️ Swipe Left")
                        pyautogui.press('left')
                    last_swipe_time = current_time

                elif abs(dy) > swipe_threshold:
                    if dy < 0:
                        print("⬆️ Swipe Up (Jump)")
                        pyautogui.press('up')
                    else:
                        print("⬇️ Swipe Down (Roll)")
                        pyautogui.press('down')
                    last_swipe_time = current_time

            prev_x, prev_y = x, y

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.putText(frame, "Swipe with index finger", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow("Swipe Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
