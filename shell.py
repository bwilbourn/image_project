import disk, core


def main():
    editor = core.PhotoEditor(disk.get_pictures(),
                              disk.get_colors(), disk.get_fonts())
    pic = core.Photo(editor.get_random_picture(), editor.colors['white'],
                     editor.fonts['watermelon'], editor.filters['DETAIL'])
    text = input('what do you want the photo to say? ')
    pic.add_text_and_filter_photo(text)
    pic.photo.show()


if __name__ == '__main__':
    main()