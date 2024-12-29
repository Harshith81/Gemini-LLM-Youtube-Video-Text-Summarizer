import streamlit as st
from dotenv import load_dotenv
   
load_dotenv() ##load all the nevironment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# prompt="""You are Yotube video summarizer. You will be taking the transcript text
# and summarizing the entire video and providing the important summary in points
# within 250 words. Please provide the summary of the text given here:  """

prompt="""You are the Youtube video summarizer, where you will be taking the transcript text and then you will be summarizing the entire video and as the output firstly i want the important keywords to be mentioned, secondly the summary need to be provided in a detailed manner, thirdly i want you to mention any explanation images,graphs,demostrations,prodcut photos and only other important images restrict the usage of images to minimum like 2-4, fourthly i want you to mention any important dates or deadlines specified in the video, and also any important website links,materials,courses,articles mentioned or refered in the video need to be mentioned and finally say Thank you."""


## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id=youtube_video_url.split("=")[1]
        
        transcript_text=YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e
    
## getting the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text,prompt):

    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("YouTube Transcript to Detailed Notes Converter")
st.text("Get clear and concise summary of your Yt Video!!")
youtube_link = st.text_input("Paste the YouTube Video Link Below and Press Enter:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Get Summary"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_gemini_content(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
