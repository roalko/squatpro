import streamlit as st
import cv2
import skvideo

st.title("Welcome to SquatPro!")

st.header("The online tool to check if you are using proper technique!")

st.text("INSTRUCTIONS")

st.text("1. Locate an area with a plain wall")
st.text("2. Record a video of you squatting from the side")
st.text("3. Make sure it is five seconds or less!")


uploaded_file = st.file_uploader("Upload your file here",type=["MOV", "mp4"])

if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)
    st.video(bytes_data)

    '''in_file = open("bytes_data", "rb") # opening for [r]eading as [b]inary
                data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
                in_file.close()

                out_file = open("out-file", "wb") # open for [w]riting as [b]inary
                out_file.write(data)
                out_file.close()'''

    def send_vide(bytes_date):
        return bytes_data


st.text("Still Need Code For Wrong or Right")
st.text("Still Need API as well, but we are getting an upload")


st.text("Check the Instructional Video Below to See if your Squat Matches")
squat_video = open('my_video.mp4', 'rb')
video_bytes = squat_video.read()
st.video(video_bytes)


from PIL import Image
image = Image.open('squatpro-logos_black.png')
st.image(image,width=150)
