#import NegativeTrans
from PIL import Image, ImageOps 
import math
import PIL


def spotlight(img: Image, center: (int, int), radius: int) -> Image:
    width, height = img.size
    overlay_color = (255, 212, 64, 128)
    img_overlay = Image.new(size=img.size, color=overlay_color, mode='RGBA')
    for x in range(width):
        for y in range(height):
            dx = x - center[0]
            dy = y - center[1]
            distance = math.sqrt(dx * dx + dy * dy)
            if distance < radius:
                img_overlay.putpixel((x, y), (23, 230, 150, 0))
    img.paste(img_overlay, None, mask=img_overlay)
    return img


if __name__ == '__main__':
    orig_file_name = 'barbara.jpg'
    img = Image.open('{}.jpg'.format('barbara'))
    spotlight_img = spotlight(img, (475, 900), 400)
    spotlight_img.save('barbarasun.jpg')
    spotlight_img.show()