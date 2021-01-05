from PIL import Image


MAIN_PAGE_WIDTH = 1280
MAIN_PAGE_HEIGHT = 860


def handle_main_page_image(file):
    image = Image.open(file)
    width, height = image.size

    new_width = round(height * MAIN_PAGE_WIDTH / MAIN_PAGE_HEIGHT)
    resized_image = image.resize((new_width, height), Image.ANTIALIAS)
    resized_image.save(file.name)
