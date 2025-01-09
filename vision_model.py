import cv2
import requests
import numpy as np
import logging
import tensorflow as tf
from insightface.app import FaceAnalysis
from transformers import AutoImageProcessor, TFViTForImageClassification
from pathlib import Path
from PIL import Image
import io

# Set up logging for production-grade usage
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImageProcessor:
    def __init__(self, model_name: str):
        """
        Initialize the image processor and model.
        :param model_name: The model to load for image classification.
        """
        self.image_processor = AutoImageProcessor.from_pretrained(model_name)
        self.model = TFViTForImageClassification.from_pretrained(model_name)

    def process_image(self, img_url: str):
        """
        Process the image from the given URL and perform classification.
        :param img_url: URL of the image.
        :return: Predicted label from the model.
        """
        try:
            # Fetch image using requests
            response = requests.get(img_url)
            if response.status_code != 200:
                raise ValueError(f"Failed to fetch image from URL. Status code: {response.status_code}")
            
            # Load image using Pillow
            img = Image.open(io.BytesIO(response.content))
            logger.info("Image successfully loaded using Pillow.")

            # Convert image to RGB (if not already)
            img = img.convert("RGB")

            # Process image for model input
            inputs = self.image_processor(images=img, return_tensors="tf")
            logger.info("Image successfully processed for model input.")

            # Perform inference
            logits = self._get_inference(inputs)
            predicted_label = self._get_predicted_label(logits)

            return predicted_label

        except ValueError as e:
            logger.error(f"ValueError: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}")
            raise RuntimeError("An unexpected error occurred during image processing.") from e


    def _get_inference(self, inputs):
        """
        Perform model inference.
        :param inputs: The processed inputs for the model.
        :return: Model logits.
        """
        try:
            logits = self.model(**inputs).logits
            logger.info("Inference completed successfully.")
            return logits
        except Exception as e:
            logger.error(f"Error during inference: {str(e)}")
            raise

    def _get_predicted_label(self, logits):
        """
        Get the predicted label from the model output logits.
        :param logits: The output logits from the model.
        :return: Predicted label.
        """
        predicted_label = int(tf.math.argmax(logits, axis=-1))
        return self.model.config.id2label[predicted_label]

def main(img_url: str):
    """
    Main function to load and process the image.
    :param image_path: Path to the image file.
    """
    model_name = "Mauregato/vit-base-patch16-224-best-finetuned-on-affectnet_short"
    
    try:
        # Initialize image processor
        processor = ImageProcessor(model_name)
        
        # Process the image and get prediction
        predicted_label = processor.process_image(img_url)
        logger.info(f"Predicted label: {predicted_label}")
    
    except Exception as e:
        logger.error(f"Failed to process the image: {str(e)}")

if __name__ == "__main__":
    img_url = "https://st2.depositphotos.com/1010146/9831/i/950/depositphotos_98319062-stock-photo-laughing-man-closeup.jpg"
    main(img_url)
