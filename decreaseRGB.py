import PIL
import openingImage
from PIL import Image
im = Image.open('barbara.jpg').convert('RGB')

# Split into 3 channels
r, g, b = im.split()

# decrease Reds by 10% try changing for correctness
r = r.point(lambda i: i * 0.9)

# Decrease Greens by 10% try changing for correctness
g = g.point(lambda i: i * 0.9)

# Decrease blue by 10%try changing for correctness
b = b.point(lambda i: i * 0.9)

# Recombine back to RGB image
result = Image.merge('RGB', (r, g, b))

result.save('brgb.png')
result.show()