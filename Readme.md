# Summarizer Application

This is a web-based summarization application built with Streamlit and Langchain, which allows users to summarize content from YouTube videos or any webpage. The application uses Groq's language model (LLM) for generating the summaries. 


## Features
- **YouTube Video Summarization**: Extracts transcript and summarizes YouTube video content.
- **Web Page Summarization**: Summarizes the content of any webpage using its URL.
- **Real-Time Feedback**: Displays the summarization progress with verbosity using a callback handler.
- **Error Handling**: Comprehensive error handling for missing transcripts, invalid URLs, and API issues.
  
## Tech Stack
- **Streamlit**: For building the web interface.
- **Langchain**: For handling summarization, text processing, and chaining models.
- **Groq's Gemma-7b-It Model**: The underlying language model used for summarization.
- **Python**: The programming language used to build the app.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/bhaveshAswani112/Text-summarization.git
    cd Text-summarization
    ```

2. Set up a virtual environment and install dependencies:
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

## Configuration

1. **Groq API Key**: To use the Groq language model, you need to provide your API key in the sidebar when prompted.
   
2. **YouTube Video or Webpage URL**: Enter the URL of the YouTube video or webpage you want to summarize in the main input field.

## How to Use

1. **Enter API Key**: In the sidebar, enter your Groq API key.
2. **Submit URL**: In the main input field, enter either a YouTube video link or a webpage URL.
3. **Summarize**: Click the "Summarize" button, and the application will display a summarized output in bullet points.
   
## Error Handling
- **Invalid URL**: The application checks if the URL provided is valid. If not, an error is shown.
- **Transcript Not Available**: If the YouTube video does not have a transcript, the application will inform you.
- **General Errors**: Errors during API interactions, summarization, or URL processing are logged to the terminal for debugging, while the user sees a simple error message.


## Contact
For any questions or feedback, please contact [aswanib133@gmail.com].

