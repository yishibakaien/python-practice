
from PIL import Image

im = Image.open('test.jpg')

print(im.format, im.size, im.mode)

im.thumbnail((200, 200))

im.save('thumb.png', 'JPEG')

import sys

print(sys.path)