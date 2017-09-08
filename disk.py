from PIL import Image, ImageFont, ImageDraw

img = Image.open("photos/class_picture.jpg").convert("L").convert("RGB")
x, y = img.size
y = y // 5
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype('fonts/Jenthill.ttf', 45)
# draw.text((x, y),"Sample Text",(r,g,b))
draw.text(
    (16, y),
    "Base Camp Coding Academy First Day of School", (51, 204, 204),
    font=font)
img.show()