import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load environment variables
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize the modern Gemini client
# It automatically picks up GEMINI_API_KEY from os.environ, 
# but passing it explicitly ensures it uses your .env file variable.
client = genai.Client(api_key=API_KEY)

system_instruction = "Eres un modelo de IA especializado en debate BP"

# Define model config using GenerateContentConfig
generation_config = types.GenerateContentConfig(
    temperature=0.7,            # Controls randomness (0 = deterministic)
    top_p=0.9,                  # Nucleus sampling (smaller = more focused)
    top_k=40,                   # Limits number of top tokens to sample from
    max_output_tokens=1024,     # Max tokens in the response
    response_mime_type="text/plain",
    system_instruction=system_instruction
)

# Use the recommended modern model: gemini-2.5-flash
model_id = "gemini-2.5-flash"

# Start the chat session, passing the configuration here
chat = client.chats.create(
    model=model_id,
    config=generation_config
)

print("Chat started (type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    
    # Send message using the modern chat client
    response = chat.send_message(user_input)
    print("Gemini:", response.text)