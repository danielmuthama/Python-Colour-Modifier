# Importing Image and ImageOps module from PIL package
from PIL import Image, ImageOps
import decreaseRGB

# creating an og_image object
og_image = Image.open("barbara.jpg")
og_image.show()

# applying grayscale method
gray_image = ImageOps.grayscale(og_image)
gray_image.show()
gray_image.save('barbaraGRYSC.png')