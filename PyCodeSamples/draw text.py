from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
img = Image.open("1.jpg")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("cmb10.ttf", 160)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text((10, 0),"!!!!!!!!!",(255,255,255),font=font)
img.save('sample-out.jpg')
