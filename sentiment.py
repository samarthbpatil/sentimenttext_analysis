
import requests

from transformers import pipeline
# Set up API and endpoint
api_url = "https://text-sentiment.p.rapidapi.com/analyze"  # Replace with the API endpoint URL
api_key = "50546ee694msh5906bcae32de3e2p1102d1jsned470d527d15"  # Replace with your API key

headers = {
    "X-RapidAPI-Host": "text-analysis12.p.rapidapi.com",  # Replace with the API host
    "X-RapidAPI-Key": api_key
}

# Input text for sentiment analysis
input_text = "Today has been one of those days where everything seems to go wrong. From the moment I woke up, things just spiraled out of control. I missed my alarm, so I was late for work, and then my computer crashed right in the middle of an important presentation. It's like the universe is conspiring against me. I'm so frustrated and exhausted dealing with all these setbacks."

# Initialize sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Perform sentiment analysis on the input text
sentiment_output = sentiment_analyzer(input_text)

# Get the sentiment label from the output
sentiment_label = sentiment_output[0]["label"]

# Set up sentiment analysis API endpoint
sentiment_api_endpoint = "https://text-sentiment.p.rapidapi.com/analyze"  # Replace with the actual sentiment analysis API endpoint

# Make a request to the sentiment analysis API
response = requests.post(sentiment_api_endpoint, headers=headers, params={"text": input_text})

# Parse the API response
api_sentiment = response.json()

# Display sentiment analysis results
print("Input Text:", input_text)
print("Hugging Face Sentiment Analysis Result:", sentiment_label)
#print("API Sentiment Analysis Result:", api_sentiment)
