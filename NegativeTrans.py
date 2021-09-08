from PIL import Image, ImageOps 
import opcode
import MakeGrayscale

img=Image.open("barbara.jpg")
w,h=img.size     # returns Width and Height of an Image
for i in range(w):
    for j in range(h):
        r,g,b=img.getpixel((i,j))
        r=255-r
        g=255-g    # Since 255 is the Highest Index
        b=255-b
        img.putpixel((i,j),(r,g,b))
img.save('barbaraNT.png')
img.show()