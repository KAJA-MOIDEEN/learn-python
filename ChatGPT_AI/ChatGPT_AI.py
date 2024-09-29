import speech_recognition as sr
import pyttsx3
import os
import openai
from dotenv import load_dotenv
from openai.error import RateLimitError, APIError, InvalidRequestError

# Load the OpenAI key from environment variables 
load_dotenv()  
OPENAI_KEY = os.getenv('OPENAI_KEY')
if not OPENAI_KEY:
    raise ValueError("OpenAI API key not found in environment variables.")

openai.api_key = OPENAI_KEY

def SpeakText(command):
    """Convert text to speech."""
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def listen_command(recognizer, microphone):
    """Listen to the user's command and convert it to text."""
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            SpeakText("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            SpeakText("Sorry, my speech service is down.")
            return None

def send_to_chatGPT(messages, model="gpt-3.5-turbo"):
    """Send messages to ChatGPT and return the response."""
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )
        message = response['choices'][0]['message']['content']
        messages.append({'role': 'assistant', 'content': message})
        return message
    except RateLimitError as e:
        SpeakText("Rate limit exceeded. Please try again later.")
        print(e)
        return "Rate limit exceeded."
    except InvalidRequestError as e:
        SpeakText(f"Request error: {str(e)}")
        return "There was an issue with the request."
    except APIError as e:
        SpeakText("API error occurred. Please try again later.")
        return f"API error: {str(e)}"
    except Exception as e:
        SpeakText("An unexpected error occurred.")
        return f"Error: {str(e)}"

# Initialize recognizer and microphone once
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Start the interaction
SpeakText("Hello! I am Jarvis, your personal assistant. How can I help you today?")

messages = []
while True:
    text = listen_command(recognizer, microphone)
    if text:
        messages.append({"role": "user", "content": text})

        # Check for exit command
        if any(exit_command in text.lower() for exit_command in ["exit", "quit", "bye", "stop"]):
            SpeakText("Goodbye! Have a great day!")
            break

        response = send_to_chatGPT(messages)
        SpeakText(response)
        print(response)
