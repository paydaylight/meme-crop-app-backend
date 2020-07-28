from PIL import Image
from PIL import ImageDraw


def caption_image(text, width, height):
    img = Image.new('RGB', (width, height), color="white")
    d = ImageDraw.Draw(img)
    d.text((0, 0), text, fill=(255, 0, 0), align="center")
    return img


def concat_vertical(im1, im2):
    img = Image.new('RGB', (im1.width, im1.height + im2.height))
    img.paste(im1, (0, 0))
    img.paste(im2, (0, im1.height))
    return img


def concat_horizontal(im1, im2):
    img = Image.new('RGB', (im1.width + im2.width, im1.height))
    img.paste(im1, (0, 0))
    img.paste(im2, (im1.width, 0))
    return img