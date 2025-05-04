from PIL import Image

def convert_image_to_png(input_path: str, output_path: str):
    """
    Open any image and re-save it as a lossless PNG 
    """
    img = Image.open(input_path)
    # Ensure it's in RGB mode 
    rgb = img.convert("RGB")
    rgb.save(output_path, format="PNG")
