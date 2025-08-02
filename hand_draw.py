import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create a blank canvas for drawing
canvas = None
prev_x, prev_y = None, None
drawing = False

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Flip frame in horizontal direction
    frame = cv2.flip(frame, 1)
    # Get frame dimensions
    h, w, _ = frame.shape

    if canvas is None:
        canvas = np.zeros((h, w, 3), dtype=np.uint8)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(frame_rgb)

    # Reset drawing and clear states
    drawing = False
    clear_canvas = False

    # Check if hand landmarks are detected
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Get coordinates of index finger tip (landmark 8), middle finger tip (landmark 12), and thumb tip (landmark 4)
            index_tip = hand_landmarks.landmark[8]
            middle_tip = hand_landmarks.landmark[12]
            thumb_tip = hand_landmarks.landmark[4]

            # Convert normalized coordinates to pixel values
            x = int(index_tip.x * w)
            y = int(index_tip.y * h)

            # Check for clear canvas gesture thumb tip above index finger tip
            if thumb_tip.y < index_tip.y - 0.05: 
                clear_canvas = True
                cv2.putText(frame, "Clearing Canvas", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                canvas = np.zeros((h, w, 3), dtype=np.uint8)
                prev_x, prev_y = None, None
            # Check for drawing gesture: index finger above middle finger
            elif index_tip.y < middle_tip.y - 0.05:
                drawing = True
                cv2.putText(frame, "Drawing: ON", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                drawing = False
                cv2.putText(frame, "Drawing: OFF", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                prev_x, prev_y = None, None

            # Draw on canvas if in drawing mode
            if drawing and prev_x is not None and prev_y is not None:
                cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 255, 0), 5)

            # Update previous point
            prev_x, prev_y = x, y

            # Draw circle at index finger tip for visual feedback
            cv2.circle(frame, (x, y), 10, (0, 0, 255), -1)

            # Draw hand landmarks on frame
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Combine frame and canvas
    canvas_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(canvas_gray, 20, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Apply mask to frame and canvas
    frame_bg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    canvas_fg = cv2.bitwise_and(canvas, canvas, mask=mask)
    # Combine the two
    combined = cv2.add(frame_bg, canvas_fg)

    # Display the combined output
    cv2.imshow("Virtual Writing", combined)

    # Handle key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        canvas = np.zeros((h, w, 3), dtype=np.uint8)
        prev_x, prev_y = None, None

# Release resources
cap.release()
cv2.destroyAllWindows()
hands.close()