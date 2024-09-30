import logging
from langchain_groq import ChatGroq
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.chains.summarize import load_summarize_chain
import validators
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, CouldNotRetrieveTranscript, NoTranscriptAvailable
import re
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Configure logging to print error messages to the terminal
logging.basicConfig(level=logging.ERROR)

st.set_page_config("Summarizer", page_icon='✌️')

with st.sidebar:
    groq_api_key = st.text_input(label="Enter your groq API key", type="password")

llm = None
try:
    llm = ChatGroq(model="Gemma-7b-It", api_key=groq_api_key)
except Exception as e:
    logging.error(f"Error initializing LLM: {str(e)}")
    st.error("An error occurred while initializing the LLM. Please try again.")

prompt_template = '''You are an expert in summarizing the following content.\n\n content : {text}'''
prompt = PromptTemplate(template=prompt_template, input_variables=['text'])

final_prompt_template = '''Give the summary in bullet points for following content.\n\n content : {text}'''
final_prompt = PromptTemplate(template=final_prompt_template, input_variables=['text'])

url = st.text_input("Enter the YouTube or website URL for which you need the summarization.")

if st.button(label="Summarize"):
    if not url.strip():
        st.error("Please provide a URL.")
    elif not groq_api_key.strip():
        st.error("Please provide a Groq API key.")
    else:
        if not validators.url(url):
            st.error("Please enter a valid URL.")
        else:
            try:
                with st.spinner("Waiting...") :
                    if "youtube.com" in url:
                        # Extract video ID from the YouTube URL
                        pattern = r"(?:v=|\/)([a-zA-Z0-9_-]{11})(?:&|$)"
                        match = re.search(pattern, url)
                        if match:
                            video_id = match.group(1)
                        else:
                            st.error("Could not extract video ID from YouTube URL.")
                            raise ValueError("Invalid YouTube video URL")

                        try:
                            loader = YoutubeLoader(video_id=video_id, add_video_info=True)
                        except CouldNotRetrieveTranscript as e:
                            logging.error(f"Could not retrieve transcript: {str(e)}")
                            st.error("Transcript not available for this YouTube video.")
                        except NoTranscriptAvailable as e:
                            logging.error(f"No transcript available: {str(e)}")
                            st.error("No transcript available for this YouTube video.")
                    else:
                        # Non-YouTube URL handling
                        user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/92.0.4515.159 Safari/537.36 Edge/92.0.902.67")

                        headers = {
                            "User-Agent": user_agent
                        }
                        loader = UnstructuredURLLoader(urls=[url], show_progress_bar=True, headers=headers)

                    # Load and split documents
                    data = loader.load_and_split()
                    docs = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=100).split_documents(data)

                    # Build and run summarization chain
                    try:
                        chain = load_summarize_chain(llm=llm, chain_type='map_reduce', map_prompt=prompt,
                                                    combine_prompt=final_prompt, verbose=True)
                        output = chain.invoke({"input_documents": docs})
                        st.write(output['output_text'])
                    except Exception as chain_error:
                        logging.error(f"Error during summarization: {str(chain_error)}")
                        st.error("An error occurred during summarization. Please try again.")

            except Exception as url_error:
                logging.error(f"Error processing the URL: {str(url_error)}")
                st.error("An error occurred while processing the URL. Please try again.")
