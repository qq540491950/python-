import tesserocr
from PIL import Image

image = Image.open("123.jpg")
print(tesserocr.image_to_text(image))
