from PIL import Image, ImageFont, ImageDraw


def filter_photo(photo, font, color):
    ''' photo is string filename (with path) for the image
    ex: "photos/one.jpg" 

    font is string filename with path for the ttf font file
    ex: 'fonts/Jenthill.ttf'

    color is the RGB tuple
    ex:  (51, 204, 204)
    '''
    # img = Image.open("photos/class_picture.jpg").convert("L").convert("RGB")
    img = Image.open(photo).convert("RGB")
    x, y = img.size
    y = y // 2
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    # font = ImageFont.truetype('fonts/Jenthill.ttf', 45)
    font = ImageFont.truetype(font, 45)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((16, y), "BEST FRIENDS", color, font=font)
    # draw.text(
    #     (16, y),
    #     "Base Camp Coding Academy First Day of School", (51, 204, 204),
    #     font=font)
    img.show()


def main():
    all_fonts = ['fonts/font1.ttf', 'fonts/font2.ttf', 'fonts/font3.ttf']
    colors = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'cyan': (51, 204, 204)
    }
    photo = "photos/one.jpg"
    font = 'fonts/Jenthill.ttf'
    color = (51, 204, 204)
    input('Press Enter to Filter Photo!')
    filter_photo(photo, font, color)


if __name__ == '__main__':
    main()