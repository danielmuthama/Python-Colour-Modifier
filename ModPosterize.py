from PIL import Image, ImageOps 
import SunEffect
  # creating a image1 object  
im1 = Image.open("barbara.jpg")  
  
# applying posterize method on applying value of 1
im2 = ImageOps.posterize(im1, 1)  
  
im2.show() 
im2.save('barbaraPST.png')