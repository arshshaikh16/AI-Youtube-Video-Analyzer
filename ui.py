import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title = "Youtube Video Analyzer",
    layout = "centered"
)

st.title("AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

#Input box
video_url = st.text_input("Enter Youtube Video Link") #Input as string
#Button
button = st.button("Analyze Video") # Stored as True/False

if video_url and button: #When both are True
    with st.spinner("Analyzing video..."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )
    st.markdown("Analysis Report of Video:")
    st.markdown(response.content)