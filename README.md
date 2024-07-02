# AI-Emotion-Detection-using-OpenCV-and-DeepFace

This project leverages OpenCV and DeepFace to detect and analyze facial emotions in real-time.

## Overview

The primary goal of this project is to build a system that can capture video input from a webcam, detect faces in the video frames, and classify the detected faces into various emotion categories using the DeepFace library.

## Features

- Real-time video capture and processing
- Face detection using OpenCV
- Emotion analysis using DeepFace
- Displays dominant emotion and confidence score

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/charankulal/AI-Emotion-Detection-using-OpenCV-and-DeepFace.git
   cd AI-Emotion-Detection-using-OpenCV-and-DeepFace
   ```

2. Create a virtual environment

   ```bash
   python -m venv venv
    ```

3. Activate the virtual environment

   - On windows
  
    ```bash
    venv\Scripts\activate
    ```

    - On Linux/MacOS
  
    ```bash
    source venv/bin/activate
    ```

4. Install required packages

   ```bash
   pip install -r requirements.txt
   ```

5. Running Application

   ```bash
   streamlit run app.py
   ```

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
