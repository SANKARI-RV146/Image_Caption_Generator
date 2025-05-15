from PIL import Image
import torch

def generate_caption(image: Image.Image, model, processor) -> str:
    print("Processing image and generating caption...")
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    print(f"Caption Generated: {caption}")
    return caption

