import cohere
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("Cohere API key not found. Ensure it's set in the .env file.")

co = cohere.ClientV2(api_key=COHERE_API_KEY)

class ChatModel:
    def __init__(self):
        self.system_message = """**Your role is to:**
          - Provide general information and resources on mental health topics. (e.g., anxiety, depression, stress management, coping mechanisms)
          - Offer supportive listening and empathetic responses.
          - Encourage open and honest communication.
          - Promote self-care and healthy lifestyle choices.
          - Guide users towards seeking professional help when necessary.**"""

    def get_response(self, message: str, history: list) -> dict:
        try:
            # Format the chat history for the Cohere API
            chat_messages = [{"role": "system", "content": self.system_message}]
            chat_messages.append({"role": "user", "content": message + " Chat history: " + str(history)})

            # Make the Cohere API call
            res = co.chat(
                model="command-r-plus-08-2024",
                messages=chat_messages
            )
            
            # Extract response content
            response_text = res.message.content[0].text
            history.append(response_text)
            return {"response": response_text, "history": history}
        except Exception as e:
            raise RuntimeError(f"Error communicating with Cohere: {str(e)}")
