
# task3_ai_chatbot_web.py

import nltk
from nltk.chat.util import Chat, reflections
import gradio as gr

# If needed for the first time
# nltk.download('punkt')

# === Chatbot Rules ===
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you?", ["I'm doing great, thanks!", "I'm good. How can I help you?"]],
    [r"what is your name?", ["I'm an AI chatbot built with Python."]],
    [r"what can you do?", ["I can answer general and IT-related questions."]],
    [r"bye|exit|quit", ["Goodbye! Take care."]],

    # IT-related
    [r"what is python?", ["Python is a high-level programming language."]],
    [r"what is an api?", ["API stands for Application Programming Interface."]],
    [r"what is machine learning?", ["It is a field of AI focused on learning from data."]],
    [r"what is git?", ["Git is a version control system."]],
    [r"what is html?", ["HTML is used to structure web content."]],
]

# === Create chatbot ===
chatbot = Chat(pairs, reflections)

# === Response function ===
def respond(message):
    return chatbot.respond(message) or "Sorry, I do not understand."

# === Gradio Interface ===
iface = gr.Interface(
    fn=respond,
    inputs=gr.Textbox(lines=2, placeholder="Type your message here..."),
    outputs="text",
    title="🧠 AI Chatbot (Internship Project)",
    description="Ask general or IT-related questions like 'what is Python?' or 'what is an API?'"
)

# === Launch interface ===
if __name__ == "__main__":
    iface.launch(share=True)
