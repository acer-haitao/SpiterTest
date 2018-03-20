import os

from PIL import Image, ImageDraw, ImageFont

text = u"1"

im = Image.new("RGB", (300, 50), (255, 255, 255))
dr = ImageDraw.Draw(im)
font = ImageFont.truetype(os.path.join("fonts", "simsun.ttc"), 18)

dr.text((1, 1), text, font=font, fill="#000000")

im.show()
im.save("t.png")
