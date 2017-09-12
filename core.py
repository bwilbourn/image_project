from PIL import Image, ImageFont, ImageDraw, ImageFilter
from random import choice


class PhotoEditor:
    def __init__(self, pictures, colors, fonts):
        ''' ([str], {str}, {str}, {str}) -> '''
        self.pictures = pictures
        self.colors = colors
        self.fonts = fonts
        self.filters = {
            "BLUR": ImageFilter.BLUR,
            "CONTOUR": ImageFilter.CONTOUR,
            "DETAIL": ImageFilter.DETAIL,
            "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
            "EDGE_ENHANCE_MORE": ImageFilter.EDGE_ENHANCE_MORE,
            "EMBOSS": ImageFilter.EMBOSS,
            "FIND_EDGES": ImageFilter.FIND_EDGES,
            "SMOOTH": ImageFilter.SMOOTH,
            "SMOOTH_MORE": ImageFilter.SMOOTH_MORE,
            "SHARPEN": ImageFilter.SHARPEN
        }

    def get_random_picture(self):
        return choice(self.pictures)


class Photo:
    def __init__(self, filename, color, font, pfilter):
        self.filename = filename
        self.color = color
        self.font = ImageFont.truetype(font, 45)
        self.filter = pfilter
        self.photo = Image.open(filename).filter(pfilter)

    def add_text_and_filter_photo(self, text):
        x, y = self.photo.size
        y = y // 2
        draw = ImageDraw.Draw(self.photo)
        draw.text((16, y), text, self.color, font=self.font)
