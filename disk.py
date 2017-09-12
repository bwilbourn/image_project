def get_fonts():
    with open('fonts.txt', 'r') as file:
        font_list = file.readlines()
    fonts = {}
    for font in font_list:
        font_name, font_file = font.split(', ')
        fonts[font_name] = font_file.strip()
    return fonts


def get_colors():
    with open('colors.txt', 'r') as file:
        lines = file.readlines()
    colors = {}
    for line in lines:
        colorname, color_values = line.split(': ')
        r, g, b = color_values.split(', ')
        colors[colorname] = (int(r), int(g), int(b))
    return colors


def get_pictures():
    with open('pictures.txt', 'r') as file:
        picture_string = file.read()
    return picture_string.split('\n')
