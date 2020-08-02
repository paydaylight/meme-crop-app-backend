from classes import ImageManipulator
from models.image import Image
import uuid


class DerivativeImage:
    def __init__(self, mode={'horizontal': True}):
        self.mode = mode

    def call(self, image_id, new_caption):
        parent_image = Image.query.get(image_id)
        og_image = parent_image.parent

        mp = ImageManipulator(og_image.url, new_caption)

        populate_dict_function, map_dict_to_caption_function = self.functions_from_mode(mp)

        populate_dict_function()
        derivative_image = map_dict_to_caption_function(mp.caption_text)
        derivative_image_with_caption = self._derivative_image_with_caption(derivative_image, mp)

        new_id = str(uuid.uuid4())
        stored_derivative_image = Image(id=new_id,
                                        caption=mp.caption_text,
                                        url=mp.image_path(new_id),
                                        parent_id=og_image.id)

        derivative_image_with_caption.save(mp.image_path(new_id))
        stored_derivative_image.save()

        return stored_derivative_image

    def _derivative_image_with_caption(self, image, mp):
        caption_image = mp.caption_image(mp.caption_text, mp.width, 50)
        return mp.concat_vertical(image, caption_image)

    def functions_from_mode(self, mp):
        if self.mode['horizontal']:
            return mp.populate_dict_vertical, mp.map_dict_to_vertical_caption
        elif self.mode['vertical']:
            return mp.populate_dict_horizontal, mp.map_dict_to_horizontal_caption
        else:
            return None, None









