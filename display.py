import cv2

def display_instructions(frame):
    """
    Draws instructions for controlling the video directly onto the frame.
    """
    instructions = [
        "'Q': Quit",
        "'S': Stop/pause",
        "'C': Continue",
        "'R': Restart"
    ]
    y0, dy = 20, 30  # Initial Y position and line spacing
    for i, line in enumerate(instructions):
        y = y0 + i * dy
        cv2.putText(frame, line, (10, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
