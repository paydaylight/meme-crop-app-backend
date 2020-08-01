from PIL import Image
from PIL import ImageDraw

def caption_image(text, width, height):
    img = Image.new('RGB', (width, height), color="white")
    d = ImageDraw.Draw(img)
    d.text((0, 0), text, fill=(255, 0, 0), align="center")
    return img


def concat_vertical(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst


def concat_horizontal(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def horizontal_crop():
    per_crop_height = height / len(original_caption_hash.keys())
    print(per_crop_height)
    iterator = 0

    for char in original_caption_hash:
        cropped_part = original.crop((0, iterator, width, iterator + per_crop_height))
        original_caption_hash[char] = cropped_part
        iterator += per_crop_height

original_caption = "shierke"
generate_caption = ["shish", "erkesh"]

original_caption_chars = list(original_caption)
original_caption_hash = {}

for char in original_caption_chars:
    original_caption_hash[char] = None

test_image = "test.png"
original = Image.open(test_image)

# original.show()

width, height = original.size   # Get dimensions

vertical_toggle = False

if not vertical_toggle:
    # per_crop_height = height/len(original_caption_hash.keys())
    per_crop_height = height/len(original_caption)
    print(per_crop_height)
    iterator = 0

    for char in original_caption_hash:
        cropped_part = original.crop((0, iterator, width, iterator+per_crop_height))
        original_caption_hash[char] = cropped_part
        iterator += per_crop_height
        # cropped_part.show()


for new_caption in generate_caption:
    new_caption_list = list(new_caption)
    current = original_caption_hash[new_caption_list[0]]

    for char in new_caption_list[1:]:
        current = concat_vertical(current, original_caption_hash[char])

    current = concat_vertical(current, caption_image(new_caption, width, 50))
    current.show()







print(original_caption_hash)
print(len(original_caption_hash.keys()))
# test_image = "test.jpg"
# original = Image.open(test_image)
# original.show()
#
# width, height = original.size   # Get dimensions
# left = width/4
# top = height/4
# right = 3 * width/4
# bottom = 3 * height/4
# cropped_example = original.crop((left, top, right, bottom))
#
# cropped_example.show()