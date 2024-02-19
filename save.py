import cv2

class VideoSaver:
    def __init__(self, original_path, preprocessed_path, frame_size, fps=20.0):
        # Define the codec and create VideoWriter objects
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # For MP4 files
        self.out_original = cv2.VideoWriter(original_path, fourcc, fps, frame_size)
        self.out_preprocessed = cv2.VideoWriter(preprocessed_path, fourcc, fps, frame_size)

    def write_frames(self, original_frame, preprocessed_frame):
        # Write the frames to their respective video files
        self.out_original.write(original_frame)
        self.out_preprocessed.write(preprocessed_frame)

    def release(self):
        # Release the VideoWriter objects
        self.out_original.release()
        self.out_preprocessed.release()
