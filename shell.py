import disk, core


def get_filter_name(names):
    print('\nWhat filter would you like?\n ')
    print('\n'.join(names))
    while True:
        choice = input('>>> ').upper()
        if choice in names:
            return choice


def update_image(editor, img, fcolor, fontname, pfilter):
    return core.Photo(img,
                      editor.colors.get(fcolor, 'white'),
                      editor.fonts.get(fontname, 'jenthill'),
                      editor.filters.get(pfilter, 'sharpen'))


def main():
    editor = core.PhotoEditor(disk.get_pictures(),
                              disk.get_colors(), disk.get_fonts())
    fontname = 'jenthill'
    fcolor = 'white'
    print('Britney & Maegan\'s PhotoEditor!')

    # get the filter
    pfilter = get_filter_name(editor.get_filter_names())
    img = editor.get_random_picture()
    pic = update_image(editor, img, fcolor, fontname, pfilter)
    pic.photo.show()

    # get the text
    text = input('What would you like your text to say? ')
    print('\n'.join(editor.get_color_names()))
    fcolor = input('What color would you like the font to be? ')
    pic = update_image(editor, img, fcolor, fontname, pfilter)
    pic.add_text_and_filter_photo(text)
    pic.photo.show()

    # get the fontname
    print('\n'.join(editor.get_font_names()))
    fontname = input('Choose a font you like. ')
    pic = update_image(editor, img, fcolor, fontname, pfilter)
    pic.add_text_and_filter_photo(text)

    pic.photo.show()
    complete = input('Do you like the final master piece? ')
    if complete == 'yes':
        exit()


if __name__ == '__main__':
    main()