from classes import ImageManipulator
from models import Image
import uuid


class DerivativeImage:
    def __init__(self, mode={'horizontal': True}):
        if mode['horizontal']:
            self.concat_function = ImageManipulator.concat_horizontal
            self.populate_dict_function = ImageManipulator.concat_horizontal
            self.map_dict_to_caption_function = ImageManipulator.map_dict_to_vertical_caption
        elif mode['vertical']:
            self.concat_function = ImageManipulator.concat_vertical
            self.populate_dict_function = ImageManipulator.concat_vertical
            self.map_dict_to_caption_function = ImageManipulator.map_dict_to_horizontal_caption

    def call(self, image_id):
        parent_image = Image.query.get(image_id)







