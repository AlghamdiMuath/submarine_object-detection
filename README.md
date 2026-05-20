# submarine_object-detection

OpenCV-based preprocessing pipeline for live underwater video, intended as a frontend for an object-detection workflow. Captures from the default camera, applies underwater color/contrast corrections frame-by-frame, and saves either the raw or preprocessed stream.

## What's inside

- `main.py` — entrypoint. Opens the camera with `cv2.VideoCapture`, displays original and preprocessed feeds, and lets you record either stream while watching.
- `preprocessing.py` — frame-level transforms (color correction, contrast, denoising) suited to underwater footage.
- `display.py` — UI overlay (instructions, pause indicator, recording markers) drawn on top of the live feed.
- `save.py` — `cv2.VideoWriter` helpers that mux the displayed frames into MP4/AVI files.

## Controls

The on-screen overlay (`display_instructions`) lists the active keys for pausing, toggling preprocessing, and starting/stopping recording.

## Run

```bash
pip install opencv-python numpy
python main.py
```

Note: defaults to camera index `0` and `CAP_DSHOW` (DirectShow on Windows). Change `cv2.VideoCapture(0, cv2.CAP_DSHOW)` in `main.py` if you're on Linux/Mac or using a different camera.

---

*Archived: senior-project exploration, kept for reference.*
