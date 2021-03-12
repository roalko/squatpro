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
image = Image.open('/scripts/squatpro-logos_black.png')
st.image(image,width=700)

st.markdown("# **A tool to verify your squatting technique!**")

st.markdown("### INSTRUCTIONS")
st.markdown("##### 1. Locate an area with a plain wall")
st.markdown("##### 2. Record a video of you squatting from the side")
st.markdown("##### 3. Make sure it is five seconds or less")

uploaded_file = st.file_uploader("Upload your file here:", type=["MOV", "mp4"])

if uploaded_file is not None:
    video_bytes = uploaded_file.getvalue()

    result = pipe.predict_test(video_bytes)

    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)

    if result[0][0] >= 0.5:
        st.balloons()
        st.markdown('### ***CONGRATS, YOU ARE A SQUATPRO!! YOUR BACK & KNEES ARE THANKFUL!!***')
        with st.beta_expander("Still Feel Like You Could Use Some Tips? Click here:"):

            st.markdown("### STARTING POSITION")
            st.markdown("##### * Stand with your feet shoulder-width apart. Your knees and feet should be pointing in the same direction.")
            st.markdown('##### * Raise your arms out in front of you for balance (or you can leave them by your side and raise them as you descend).')

            st.markdown("### EXECUTION")
            st.markdown("##### * Keep your head up and torso upright as you squat.")
            st.markdown("##### * Bending your hips back, make sure to descend until your thighs are parallel with the floor.")
            st.markdown("##### * Exhale as you return to the starting position.")

            st.markdown("### Comments and Tips")
            st.markdown("##### * Keep your knees and feet pointing in the same direction, and your feet flat on the floor throughout the movement.")
            st.markdown("##### * Keep an equal distribution of weight through your forefoot and heel.")
            st.markdown("##### * Keep your back straight, head facing forward, and torso upright.")

            st.markdown('### See the video below for a demonstration of proper squat form')
            squat_video = open('/scripts/Air_Squat_720p.mp4', 'rb')
            video_bytes = squat_video.read()
            st.video(video_bytes)

        with st.beta_expander("Click here for tips on correcting the most common squatting mistakes:"):
            st.markdown('### For some people, anatomical differences play a role in how difficult it is to drop into a squat\
                (e.g., the positioning of the ball-and-socket joint of your hips), but even those with the most squat-resistant\
                bone structure can learn to access deep, comfortable squats.')


            st.markdown("## Mistake 1: Torso collapses")
            st.markdown("### Fix: Improve hip, ankle and spinal mobility, as well as core strength.")

            st.markdown("### The most common squat mistake, the forward lean, occurs when a combination of inflexible joints and\
                 weak core muscles prevent you from holding yourself upright in a deep squat. \
                 Your hips and ankles don't allow for a large enough range of motion, while your core (abdominals and back muscles)\
                 can't support your spine. Weak glute muscles may also cause you to lean forward.")

            st.markdown("### To fix a forward lean, you'll need to improve mobility in your hips, \
            ankles and spine, as well increase your core strength.")

            st.markdown("### Here are some instructional videos that can help you get started:")
            st.markdown("### [Hip mobility flow](https://www.youtube.com/watch?v=bipdDS8tiEg)")
            st.markdown("### [Ankle mobility exercises for better squats](https://www.youtube.com/watch?v=WkdXHQ74khI)")
            st.markdown("### [Foam rolling routine for spinal flexibility](https://www.youtube.com/watch?v=WDYFfr6KRoM)")
            st.markdown("### [Core strengthening routine](https://www.youtube.com/watch?v=q6NIWNnvOK0&list=PLWBWBhYeaclyiURiF0WzjIupsjcvIhJqJ&index=2)")


            st.markdown("## Mistake 2: Heels come off the ground")
            st.markdown("### Fix: Improve ankle and hip mobility.")

            st.markdown("### If you cannot keep your feet flat on the ground during a squat, that's another common sign of limited mobility,\
             particularly in the ankles. Hip mobility and spinal mobility limitations can also contribute to your heels raising off of the ground.")

            st.markdown("### To fix this common squat mistake, spend a lot of time on your ankle mobility, but don't neglect your other joints. \
            When it comes to squatting, optimal mobility in all joints (even your upper body) plus great core strength leads to faultless form.")

            st.markdown("### [Top three ankle mobility exercises](https://www.youtube.com/watch?v=IikP_teeLkI)")
            st.markdown("### [Hip mobility for a PERFECT squat](https://www.youtube.com/watch?v=888Fod2Fcmo)")
            st.markdown("### [Full body mobility routine](https://www.youtube.com/watch?v=4kXCxpomK5c)")


            st.markdown("## Mistake 3: Knees collapsing")
            st.markdown("### Fix: Improve ankle mobility, core strength and glute strength.")

            st.markdown("### If your knees tend to collapse during a squat, that's another common sign of limited mobility in the ankles.\
             Weak glutes or a weak transfer of weight into the hips from the core can also contribute to your knees to go inwards during a squat.")

            st.markdown("### To fix the mistake of your knees collapsing while squatting, focus on improving your ankle mobility. \
            Strengthening you core and your glutes will further help you to achieve that perfect SQUATPRO form.")

            st.markdown("### [Improve your squat depth with ankle mobility](https://www.youtube.com/watch?v=eSS4-LF4VKM)")
            st.markdown("### [Glute strengthening workout](https://www.youtube.com/watch?v=Bf8uyQOmqU8&list=PLWBWBhYeaclySRjd_eezv3aAQe9FN9ZJw&index=32)")
            st.markdown("### [Total core workout](https://www.youtube.com/watch?v=1GxTkJpufx0&list=PLWBWBhYeaclyiURiF0WzjIupsjcvIhJqJ&index=1)")


    if result[0][0] < 0.5:

        st.markdown('### Oops! looks like your form was a little off')

        st.markdown('##### Here are some tips to improve! Take a look and upload a new squat!')

        st.markdown("### STARTING POSITION")
        st.markdown("##### * Stand with your feet shoulder-width apart. Your knees and feet should be pointing in the same direction.")
        st.markdown('##### * Raise your arms out in front of you for balance (or you can leave them by your side and raise them as you descend).')

        st.markdown("### EXECUTION")
        st.markdown("##### * Keep your head up and torso upright as you squat.")
        st.markdown("##### * Bending your hips back, make sure to descend until your thighs are parallel with the floor.")
        st.markdown("##### * Exhale as you return to the starting position.")

        st.markdown("### Comments and Tips")
        st.markdown("##### * Keep your knees and feet pointing in the same direction, and your feet flat on the floor throughout the movement.")
        st.markdown("##### * Keep an equal distribution of weight through your forefoot and heel.")
        st.markdown("##### * Keep your back straight, head facing forward, and torso upright.")

        st.markdown('### See the video below for a demonstration of proper squat form')
        squat_video = open('/scripts/Air_Squat_720p.mp4', 'rb')
        video_bytes = squat_video.read()
        st.video(video_bytes)

        with st.beta_expander("Click here for tips on correcting the most common squatting mistakes:"):
            st.markdown('### For some people, anatomical differences play a role in how difficult it is to drop into a squat\
                (e.g., the positioning of the ball-and-socket joint of your hips), but even those with the most squat-resistant\
                bone structure can learn to access deep, comfortable squats.')


            st.markdown("## Mistake 1: Torso collapses")
            st.markdown("### Fix: Improve hip, ankle and spinal mobility, as well as core strength.")

            st.markdown("### The most common squat mistake, the forward lean, occurs when a combination of inflexible joints and\
                 weak core muscles prevent you from holding yourself upright in a deep squat. \
                 Your hips and ankles don't allow for a large enough range of motion, while your core (abdominals and back muscles)\
                 can't support your spine. Weak glute muscles may also cause you to lean forward.")

            st.markdown("### To fix a forward lean, you'll need to improve mobility in your hips, \
            ankles and spine, as well increase your core strength.")

            st.markdown("### Here are some instructional videos that can help you get started:")
            st.markdown("### [Hip mobility flow](https://www.youtube.com/watch?v=bipdDS8tiEg)")
            st.markdown("### [Ankle mobility exercises for better squats](https://www.youtube.com/watch?v=WkdXHQ74khI)")
            st.markdown("### [Foam rolling routine for spinal flexibility](https://www.youtube.com/watch?v=WDYFfr6KRoM)")
            st.markdown("### [Core strengthening routine](https://www.youtube.com/watch?v=q6NIWNnvOK0&list=PLWBWBhYeaclyiURiF0WzjIupsjcvIhJqJ&index=2)")


            st.markdown("## Mistake 2: Heels come off the ground")
            st.markdown("### Fix: Improve ankle and hip mobility.")

            st.markdown("### If you cannot keep your feet flat on the ground during a squat, that's another common sign of limited mobility,\
             particularly in the ankles. Hip mobility and spinal mobility limitations can also contribute to your heels raising off of the ground.")

            st.markdown("### To fix this common squat mistake, spend a lot of time on your ankle mobility, but don't neglect your other joints. \
            When it comes to squatting, optimal mobility in all joints (even your upper body) plus great core strength leads to faultless form.")

            st.markdown("### [Top three ankle mobility exercises](https://www.youtube.com/watch?v=IikP_teeLkI)")
            st.markdown("### [Hip mobility for a PERFECT squat](https://www.youtube.com/watch?v=888Fod2Fcmo)")
            st.markdown("### [Full body mobility routine](https://www.youtube.com/watch?v=4kXCxpomK5c)")


            st.markdown("## Mistake 3: Knees collapsing")
            st.markdown("### Fix: Improve ankle mobility, core strength and glute strength.")

            st.markdown("### If your knees tend to collapse during a squat, that's another common sign of limited mobility in the ankles.\
             Weak glutes or a weak transfer of weight into the hips from the core can also contribute to your knees to go inwards during a squat.")

            st.markdown("### To fix the mistake of your knees collapsing while squatting, focus on improving your ankle mobility. \
            Strengthening you core and your glutes will further help you to achieve that perfect SQUATPRO form.")

            st.markdown("### [Improve your squat depth with ankle mobility](https://www.youtube.com/watch?v=eSS4-LF4VKM)")
            st.markdown("### [Glute strengthening workout](https://www.youtube.com/watch?v=Bf8uyQOmqU8&list=PLWBWBhYeaclySRjd_eezv3aAQe9FN9ZJw&index=32)")
            st.markdown("### [Total core workout](https://www.youtube.com/watch?v=1GxTkJpufx0&list=PLWBWBhYeaclyiURiF0WzjIupsjcvIhJqJ&index=1)")


