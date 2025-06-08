from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

# Configure Gemini
genai.configure(api_key=API_KEY)

# Define model config
generation_config = {
    "temperature": 0.7,         # Controls randomness (0 = deterministic)
    "top_p": 0.9,               # Nucleus sampling (smaller = more focused)
    "top_k": 40,                # Limits number of top tokens to sample from
    "max_output_tokens": 1024,  # Max tokens in the response
    "response_mime_type": "text/plain"
}

# Optional: add context or instruction to guide model behavior
system_instruction = "Eres un modelo de IA especializado en debate BP"

# Create model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=system_instruction
)

chat = model.start_chat()

# Simple interactive loop
print("Chat started (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
