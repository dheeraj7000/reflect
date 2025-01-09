from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from vision_model import ImageProcessor
import logging
from pydantic import BaseModel
from text_model import ChatModel
import base64

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# FastAPI instance
app = FastAPI()
chat_model = ChatModel()

# Global chat history for the single user
chat_history = []

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str
    history: list

class ImagePayload(BaseModel):
    image_url: str  # Hex string representation of the binary data

# Instantiate the ImageProcessor with the pre-trained model
model_name = "Mauregato/vit-base-patch16-224-best-finetuned-on-affectnet_short"
processor = ImageProcessor(model_name)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    message = request.message

    try:
        result = chat_model.get_response(message, chat_history)
        return ChatResponse(response=result["response"], history=result["history"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/predict_emotion")
async def predict_emotion(payload: ImagePayload):
    """
    API endpoint to predict emotions from base64-encoded image data.
    :param payload: JSON payload containing base64-encoded image data.
    :return: Predicted emotion label.
    """
    try:
        # Process the image and get prediction
        predicted_label = processor.process_image(payload.image_url)
        
        # Return the result as a JSON response
        return JSONResponse(content={"emotion": predicted_label})
    
    except ValueError as e:
        logger.error(f"ValueError: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)