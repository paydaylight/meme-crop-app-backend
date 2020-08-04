from PIL import Image, ImageDraw, ImageFont

UPLOADS = "uploads"


class ImageManipulator:
    def __init__(self, image_path, caption_text):
        self.image = Image.open(image_path)
        # self.width, self.height = self.image.size
        self.caption_text = caption_text.strip()
        self.caption_chars = list(caption_text.replace(' ', ''))
        self.caption_dict = {}

        for char in self.caption_chars:
            self.caption_dict[char] = None

    @staticmethod
    def caption_image(text, width, height=50):
        img = Image.new('RGB', (width, height), color="white")
        font = ImageFont.truetype("assets/fonts/Montserrat/Montserrat-Light.ttf", 40)
        d = ImageDraw.Draw(img)
        w, h = d.textsize(text, font=font)
        h += int(h * 0.21)
        d.text(((width - w) / 2, (height - h) / 2), text=text, fill='black', font=font)
        return img

    @staticmethod
    def concat_vertical(im1, im2):
        dst = Image.new('RGB', (im1.width, im1.height + im2.height), (255, 255, 255))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (0, im1.height))
        return dst

    @staticmethod
    def concat_horizontal(im1, im2):
        dst = Image.new('RGB', (im1.width + im2.width, im1.height), (255, 255, 255))
        dst.paste(im1, (0, 0))
        dst.paste(im2, (im1.width, 0))
        return dst

    def populate_dict_horizontal(self, caption_text):
        per_crop_height = self.image.height / len(caption_text.replace(' ', ''))
        iterator = 0

        for char in self.caption_dict:
            cropped_part = self.image.crop((0, iterator, self.image.width, iterator + per_crop_height))
            self.caption_dict[char] = cropped_part
            iterator += per_crop_height

    def populate_dict_vertical(self, caption_text):
        per_crop_width = self.image.width / len(caption_text.replace(' ', ''))
        iterator = 0

        for char in self.caption_dict:
            cropped_part = self.image.crop((iterator, 0, iterator + per_crop_width, self.image.height))
            self.caption_dict[char] = cropped_part
            iterator += per_crop_width

    def map_dict_to_vertical_caption(self, new_caption):
        new_caption_list = list(new_caption.replace(' ', ''))
        current = self.caption_dict[new_caption_list[0]]

        for char in new_caption_list[1:]:
            current = self.concat_horizontal(current, self.caption_dict[char])

        return current

    def map_dict_to_horizontal_caption(self, new_caption):
        new_caption_list = list(new_caption.replace(' ', ''))
        current = self.caption_dict[new_caption_list[0]]

        for char in new_caption_list[1:]:
            current = self.concat_vertical(current, self.caption_dict[char])

        return current

    def image_path(self, img_id):
        return f"{UPLOADS}/{img_id}.png"

    def resize(self, image, size=(432, 540)):
        image.thumbnail(size, Image.LANCZOS)
        return image


