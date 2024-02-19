import cv2
import numpy as np
from datetime import datetime
from preprocessing import preprocess_frame
from display import display_instructions

# Initialize video capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open video stream from camera")
    cap.release()
    exit()

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_size = (frame_width, frame_height)
fps = 20.0  # Example FPS value

# Initialize VideoWriter objects to None
video_saver_original = None
video_saver_preprocessed = None

paused = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # Initialize VideoWriter after successful frame capture
    if video_saver_original is None or video_saver_preprocessed is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        original_filename = f'original_{timestamp}.mp4'
        preprocessed_filename = f'preprocessed_{timestamp}.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_saver_original = cv2.VideoWriter(original_filename, fourcc, fps, frame_size)
        video_saver_preprocessed = cv2.VideoWriter(preprocessed_filename, fourcc, fps, frame_size)

    preprocessed_frame = preprocess_frame(frame)

    if not paused:
        # Save the frames
        video_saver_original.write(frame)
        video_saver_preprocessed.write(preprocessed_frame)

    # Display logic
    display_instructions(frame)
    display_frame = cv2.cvtColor(preprocessed_frame, cv2.COLOR_RGB2BGR)
    combined_frame = np.hstack((frame, display_frame))
    cv2.imshow('Original (Left) vs Preprocessed (Right)', combined_frame)

    # User input
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        paused = True
    elif key == ord('c') or key == ord('r'):
        paused = False

# Cleanup
if video_saver_original is not None:
    video_saver_original.release()
if video_saver_preprocessed is not None:
    video_saver_preprocessed.release()
cap.release()
cv2.destroyAllWindows()
