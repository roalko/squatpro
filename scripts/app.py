import streamlit as st
import cv2
import skvideo
import requests
from io import StringIO
import pipeline as pipe
import streamlit.components.v1 as components
import time

st.set_page_config(
        page_title="SquatPro",
        layout="centered",
        initial_sidebar_state="expanded",
        )

from PIL import Image
image = Image.open('squatpro-logos_black.png')
st.image(image,width=700)

st.markdown("# **A tool to verify your squatting technique!**")

st.markdown("### INSTRUCTIONS")
st.markdown("##### 1. Locate an area with a plain wall")
st.markdown("##### 2. Record a video of you squatting from the side")
st.markdown("##### 3. Make sure it is five seconds or less!")

uploaded_file = st.file_uploader("Upload your file here", type=["MOV", "mp4"])

if uploaded_file is not None:
    video_bytes = uploaded_file.getvalue()

    result = pipe.predict_test(video_bytes)

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    if result[0][0] >= 0.5:
        st.balloons()
        st.markdown('### ***CONGRATS, YOUR FORM IS STUNNING! AND YOUR BACK IS THANKFUL.***')
        with st.beta_expander("Still Feel Like You Could Use Some Tips? Click here!"):

            st.markdown("### STARTING POSITION")
            st.markdown("##### * Stand with your feet shoulder-width apart. Your knees and feet should be pointing in the same direction")
            st.markdown('##### * Raise your arms out in front of you for balance (or you can leave them by your side and raise them as you descend')

            st.markdown("### EXECUTION")
            st.markdown("##### * Keep your head up and torso upright as you squat")
            st.markdown("##### * Bending your hips back, make sure to descend until your thighs are parallel with the floor")
            st.markdown("##### * Exhale as you return to the starting position.")

            st.markdown('### See the video below for a demonstration of proper form')
            squat_video = open('Air_Squat_720p.mp4', 'rb')
            video_bytes = squat_video.read()
            st.video(video_bytes)

    if result[0][0] < 0.5:

        st.markdown('### Oops! looks like your form was a little off')

        st.markdown('##### Here are some tips to improve! Take a look and upload a new squat!')

        st.markdown("### STARTING POSTIION")
        st.markdown("##### * Stand with your feet shoulder-width apart. Your knees and feet should be pointing in the same direction")
        st.markdown('##### * Raise your arms out in front of you for balance (or you can leave them by your side and raise them as you descend)')

        st.markdown("### EXECUTION")
        st.markdown("##### * Keep your head up and torso upright as you squat")
        st.markdown("##### * Bending your hips back, make sure to descend until your thighs are parallel with the floor.")
        st.markdown("##### * Exhale as you return to the starting position.")

        st.markdown('### See the video below for a demonstration of proper form')
        squat_video = open('Air_Squat_720p.mp4', 'rb')
        video_bytes = squat_video.read()
        st.video(video_bytes)

        with st.beta_expander("Still Feel Like You Need Tips On Your Form"):
            st.markdown("### Comments and Tips")
            st.markdown("##### * Keep your knees and feet pointing in the same direction, and your feet flat on the floor throughout the movement.")
            st.markdown("##### * Keep an equal distribution of weight through your forefoot and heel.")
            st.markdown("##### * Keep your back straight, head facing forward, and torso upright.")

