YouTube Video Summarizer
This project utilizes Streamlit and Google's Generative AI to summarize YouTube videos based on their transcripts. It provides a clear and concise summary of video content, highlighting keywords, details, and important elements.

Table of Contents
Introduction
Setup
Requirements
Installation
Usage
Running the Application
Input
Output
Contributing
License
Introduction
This application uses Streamlit, a Python framework for creating web applications, to build a tool that summarizes YouTube videos based on their transcripts. It leverages Google's Generative AI (Gemini Pro) to generate detailed summaries from the video transcripts.

The core functionalities include:

Extracting transcript data from YouTube videos using the YouTube Transcript API.
Generating summaries using Google's Generative AI based on predefined prompts.
Setup
Requirements
Make sure you have the following installed:

Python (3.7+)
pip (Python package installer)
Google API key (for Gemini Pro API)
Dependencies listed in requirements.txt
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/your-repo.git
cd your-repo
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root directory.
Add your Google API key:
dotenv
Copy code
GOOGLE_API_KEY=your_api_key_here
Usage
Running the Application
To run the application locally:

bash
Copy code
streamlit run app.py
This will start the Streamlit server and open a browser window with the application.

Input
Paste the YouTube video link into the input field and press Enter.
Output
The application will display an image thumbnail of the video.
Clicking on "Get Summary" will generate and display a detailed summary of the video based on the defined prompts.
