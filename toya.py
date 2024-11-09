import openai
import pyttsx3
import tkinter as tk
from tkinter import scrolledtext
import cv2
from PIL import Image, ImageTk
import threading

# OpenAI API Key
openai.api_key = "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"  # Replace with your actual API key


# Initialize pyttsx3 engine for TTS with modified rate and volume
def init_tts_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if ("zira" in voice.name.lower() or "female" in voice.name.lower()) and "en-us" in voice.id.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.setProperty('rate', 150)   # Increase rate for a lighter, thinner sound
    engine.setProperty('volume', 0.9) # Slightly lower volume for clarity

    return engine



# Function to interact with OpenAI's GPT model
def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Something went wrong: {e}"

# Function to speak the welcome message
def speak_welcome_message():
    engine = init_tts_engine()
    welcome_message = "Welcome to Toya education system."
    engine.say(welcome_message)
    engine.runAndWait()

# GUI setup
root = tk.Tk()
root.title("Kid's Chatbot")
root.geometry("800x800")
root.config(bg="#ffffff")  # Set entire background to white

# Main frame to hold video and chat sections
main_frame = tk.Frame(root, bg="#ffffff")
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Left frame for video
left_frame = tk.Frame(main_frame, bg="#ffffff")
left_frame.grid(row=0, column=0, sticky="n")

# Load and play avatar video
video_path = "static/haile.mp4"  # Path to the uploaded video file
cap = cv2.VideoCapture(video_path)

# Function to play video frames
def play_video():
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (200, 200))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
        video_label.after(30, play_video)
    else:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        play_video()  # Restart video from beginning if it ends

# Video display label with fixed size
video_label = tk.Label(left_frame, bg="#ffffff", width=200, height=200)
video_label.pack(pady=10)
play_video()

# Right frame for chat and user input
right_frame = tk.Frame(main_frame, bg="#ffffff")
right_frame.grid(row=0, column=1, padx=20)

# Title label for the education system
title_label = tk.Label(right_frame, text="TOYA EDUCATION SYSTEM", font=("Arial", 18, "bold"), bg="#ffffff", fg="#333333")
title_label.pack(pady=(10, 5))  # Adding some padding

# Chatbox to display conversation
chatbox = scrolledtext.ScrolledText(right_frame, wrap="word", width=50, height=20, state="disabled", font=("Arial", 12), bg="#ffffff", fg="#333333")
chatbox.pack(pady=10)

# Frame for user input and Ask button
input_frame = tk.Frame(right_frame, bg="#ffffff")
input_frame.pack(pady=10)

# User input field with visible background color and text color
user_input = tk.Entry(input_frame, width=40, font=("Arial", 14), bg="#f0f0f0", fg="#333333")
user_input.grid(row=0, column=0, padx=(0, 10))

# Function to handle question submission
def ask_question():
    prompt = user_input.get()
    if prompt.strip():
        chatbox.config(state="normal")
        chatbox.insert(tk.END, "You: " + prompt + "\n", 'user')
        chatbox.config(state="disabled")

        # Get response from GPT
        answer = chat_with_gpt(prompt)

        # Display response in the chatbox
        chatbox.config(state="normal")
        chatbox.insert(tk.END, "Toya: " + answer + "\n\n", 'bot')
        chatbox.config(state="disabled")

        # Speak out the answer in a separate thread
        speak_thread = threading.Thread(target=speak_answer, args=(answer,))
        speak_thread.start()

    # Clear user input
    user_input.delete(0, tk.END)

    # Restart or continue video playback whenever "Ask" button is clicked
    play_video()

# Function to speak answer without stopping video
def speak_answer(answer):
    engine = init_tts_engine()
    engine.say(answer)
    engine.runAndWait()

# Ask button
ask_button = tk.Button(input_frame, text="Ask", command=ask_question, font=("Arial", 14), bg="#5DADE2", fg="white", borderwidth=2, relief="raised")
ask_button.grid(row=0, column=1)

# Style the chatbox with tags for user and bot
chatbox.tag_config('user', foreground='blue')
chatbox.tag_config('Toya', foreground='green')

# Speak the welcome message when the GUI starts
speak_welcome_message()

# Start the main GUI loop
root.mainloop()

