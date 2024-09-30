import validators

print(validators.url("https://www.youtube.com/watch?v=gJLVTKhTnog&list=RDilNt2bikxDI&index=2"))

llm = ChatGroq(model="Gemma-7b-It", api_key=groq_api_key)
url = "https://www.youtube.com/watch?v=9lyPBa5Kd3I&list=RDilNt2bikxDI&index=5"
               pattern = r"(?:v=|\/)([a-zA-Z0-9_-]{11})(?:&|$)"
               match = re.search(pattern, url)
               if match:
                    video_id = match.group(1)
                    transcript = YouTubeTranscriptApi.get_transcript(video_id)
                    if transcript :
                        st.write(transcript)
                    else :
                        st.error("Error in getting transcript for the video")