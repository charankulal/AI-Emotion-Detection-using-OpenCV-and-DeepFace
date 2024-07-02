# Coupled with streamlit
import cv2
import streamlit as st
import numpy as np
from deepface import DeepFace

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def toggle_start():
    st.session_state.start = True
    st.session_state.stop = False

def toggle_stop():
    st.session_state.stop = True
    st.session_state.start = False

# Initialize session state variables
if 'start' not in st.session_state:
    st.session_state.start = False
if 'stop' not in st.session_state:
    st.session_state.stop = False


st.title("FACIAL EMOTION DETECTION - OPENCV")

frame_placeholder = st.empty()
col1, col2, col3, col4 = st.columns(4)

with col2:
    st.button("Start", on_click=toggle_start)
with col3:
    st.button("Stop", on_click=toggle_stop)


if st.session_state.start and not st.session_state.stop:
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.write("The video capture has ended")
            break
        
        result = DeepFace.analyze(frame, actions=["emotion"],enforce_detection=False)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.1, 4)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
        font=cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, result[0]['dominant_emotion'],(0,50),font,1,(0,0,255),2,cv2.LINE_4)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # frame = cv2.flip(frame, 1)
        frame_placeholder.image(frame, channels="RGB")

        if st.session_state.stop:
            frame_placeholder.empty()
            break

    cap.release()
    cv2.destroyAllWindows()


