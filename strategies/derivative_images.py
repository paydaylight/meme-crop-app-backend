from classes import ImageManipulator
from models import Image
import uuid


class DerivativeImages:
    def __init__(self, image_path, caption_text, mode={'horizontal': True}):
        self.manipulator = ImageManipulator(image_path, caption_text)

        if mode['horizontal']:
            self.concat_function = self.manipulator.concat_horizontal
            self.populate_dict_function = self.manipulator.concat_horizontal
            self.map_dict_to_caption_function = self.manipulator.map_dict_to_vertical_caption
        elif mode['vertical']:
            self.concat_function = self.manipulator.concat_vertical
            self.populate_dict_function = self.manipulator.concat_vertical
            self.map_dict_to_caption_function = self.manipulator.map_dict_to_horizontal_caption





