from PIL import Image
from PIL import ImageDraw

UPLOADS = "uploads"


class ImageManipulator:
    def __init__(self, image_path, caption_text):
        self.image = Image.open(image_path)
        self.width, self.height = self.image.size
        self.caption_text = caption_text
        self.caption_chars = list(caption_text)
        self.caption_dict = {}

        for char in self.caption_chars:
            self.caption_dict[char] = None

    def caption_image(self, text, width, height):
        img = Image.new('RGB', (width, height), color="white")
        d = ImageDraw.Draw(img)
        d.text((0, 0), text, fill=(255, 0, 0), align="center")
        return img

    def concat_vertical(self, im1, im2):
        dst = Image.new('RGB', (im1.width, im1.height + im2.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        return dst

    def concat_horizontal(self, im1, im2):
        dst = Image.new('RGB', (im1.width + im2.width, im1.height))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        return dst

    def populate_dict_horizontal(self):
        per_crop_height = self.height / len(self.caption_text)
        iterator = 0

        for char in self.caption_dict:
            cropped_part = self.image.crop((0, iterator, self.width, iterator + per_crop_height))
            self.caption_dict[char] = cropped_part
            iterator += per_crop_height

    def populate_dict_vertical(self):
        per_crop_width = self.width / len(self.caption_text)
        iterator = 0

        for char in self.caption_dict:
            cropped_part = self.image.crop((iterator, 0, iterator + per_crop_width, self.height))
            self.caption_dict[char] = cropped_part
            iterator += per_crop_width

    def map_dict_to_vertical_caption(self, new_caption):
        new_caption_list = list(new_caption)
        current = self.caption_dict[new_caption_list[0]]

        for char in new_caption_list[1:]:
            current = self.concat_vertical(current, self.caption_dict[char])

        return current

    def map_dict_to_horizontal_caption(self, new_caption):
        new_caption_list = list(new_caption)
        current = self.caption_dict[new_caption_list[0]]

        for char in new_caption_list[1:]:
            current = self.concat_horizontal(current, self.caption_dict[char])

        return current

    def image_path(self, img_id):
        return f"{UPLOADS}/{img_id}.png"

