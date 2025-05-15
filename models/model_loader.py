from transformers import BlipProcessor, BlipForConditionalGeneration

def load_model():
    print("Loading pre-trained BLIP model...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    print("Model loaded successfully.")
    return model, processor
