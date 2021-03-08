import streamlit as st
import cv2
import skvideo
import requests
from io import StringIO
import pipeline as pipe

#model_arch = pipe.res_model()

st.title("Welcome to SquatPro!")

st.header("The online tool to check if you are using proper technique!")

st.text("INSTRUCTIONS")

st.text("1. Locate an area with a plain wall")
st.text("2. Record a video of you squatting from the side")
st.text("3. Make sure it is five seconds or less!")


uploaded_file = st.file_uploader("Upload your file here",type=["MOV", "mp4","jpg"])

if uploaded_file is not None:

    video_bytes = uploaded_file.getvalue()

    result = pipe.predict_test(video_bytes)

    st.text(f'{result}')


st.text("Still Need Code For Wrong or Right")
st.text("Still Need API as well, but we are getting an upload")


st.text("Check the Instructional Video Below to See if your Squat Matches")
squat_video = open('my_video.mp4', 'rb')
video_bytes = squat_video.read()
st.video(video_bytes)


from PIL import Image
image = Image.open('squatpro-logos_black.png')
st.image(image,width=150)
