# Virtual Hand Tracking and Drawing

A Python application that uses computer vision to track hand movements and enable virtual drawing on a canvas using gestures. Built with **MediaPipe** for hand landmark detection and **OpenCV** for video processing, this program allows users to draw by raising their index finger and clear the canvas with a thumb gesture or keypress.

## Features

- **Draw on Canvas**: Raise your index finger above your middle finger to draw green lines by moving your hand.
- **Clear Canvas**: Raise your thumb above your index finger or press the `c` key to reset the canvas.
- **Real-Time Feedback**:
  - Displays hand landmarks and a red cursor on the index finger tip.
  - Shows status text: "Drawing: ON/OFF" and "Clearing Canvas".
- **Key Controls**:
  - `c`: Clear the canvas.
  - `q`: Quit the program.

## Prerequisites

- **Python 3.x**: Version 3.12 or higher.
- **Webcam**: A working webcam for capturing hand movements.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/HasinduRanasinghe/virtual-hand-drawing.git
   cd virtual-hand-drawing
   ```

2. **Create a Virtual Environment** (recommended):
   ```bash
   python3 -m venv myenv
   ```
   Activate the virtual environment:
   - **Windows**:
     ```bash
     myenv\Scripts\activate
     ```
   - **Linux**:
     ```bash
     source myenv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install opencv-python mediapipe numpy
   ```

## Usage

1. **Run the Program**:
   ```bash
   python hand_draw.py
   ```
   This opens a window displaying the webcam feed with hand tracking and the virtual canvas.

2. **Gestures**:
   - **Draw**: Raise your index finger above your middle finger and move your hand to draw green lines.
   - **Clear Canvas**: Raise your thumb above your index finger to reset the canvas to black.
   - **Key Controls**:
     - Press `c` to clear the canvas.
     - Press `q` to quit the program.

3. **Visual Feedback**:
   - A red circle marks the index finger tip.
   - Hand landmarks are overlaid on the webcam feed.
   - Status text:
     - `"Drawing: ON"` (green) when drawing.
     - `"Drawing: OFF"` (red) when not drawing.
     - `"Clearing Canvas"` (blue) when the clear gesture is detected.
