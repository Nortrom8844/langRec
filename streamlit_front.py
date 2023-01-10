import streamlit as st
import pathlib
import langRec as lr

st.markdown("<h1 style='text-align: center;'>YouTube language recognition</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Stumbled upon a YouTube video in an unknown language? Just punе an URL here and press recognize.</h2>", unsafe_allow_html=True)
st.text_input("URL", key="url")

#stage_message = "Enter the url"
#st.markdown("Enter the url", key = stage_message)
#st.text(Enter the url)

if (st.button("recognize")):
    st.info("Video is loading", icon=None)
    videoName = lr.downloadVideo(st.session_state.url)
    
    if (videoName != None):
        st.info("Converting video to audio", icon=None)
        audioName = lr.convertToAudio(videoName)
        
        if (audioName != None):
            st.info("Recognizing language", icon=None)
            lang = lr.recLang("audio.mp3")
            st.markdown("<h2 style='text-align: center; color = green;'>Language recognized: "+lang+".</h2>", unsafe_allow_html=True)
            
            file=pathlib.Path("audio.mp3")
            file.unlink()

            file=pathlib.Path("video.mp4")
            file.unlink()
    else:       
         st.error("Invalid link") 
    



