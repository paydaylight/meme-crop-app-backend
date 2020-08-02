from classes import ImageManipulator
from models.image import Image
import uuid


class ParentImage:
    def __init__(self, image_path, caption_text):
        self.og_image_path = image_path
        self.mp = ImageManipulator(image_path, caption_text)

    def call(self):
        og_image = self.create_og_image()
        parent_image = self.create_og_image_with_caption(og_image.id)
        print(parent_image, "in parent_image")
        return parent_image

    def create_og_image(self):
        og_image = Image(caption=self.mp.caption_text, url=self.og_image_path)
        og_image.save()
        return og_image

    def create_og_image_with_caption(self, og_image_id):
        og_image_with_caption_file = self._og_image_with_caption()
        new_id = str(uuid.uuid4())

        parent_image = Image(id=new_id,
                             caption=self.mp.caption_text,
                             url=self.mp.image_path(new_id),
                             parent_id=og_image_id)

        og_image_with_caption_file.save(self.mp.image_path(new_id))
        parent_image.save()
        return parent_image

    def _og_image_with_caption(self):
        caption_image = self.mp.caption_image(self.mp.caption_text, self.mp.width, 50)
        return self.mp.concat_vertical(self.mp.image, caption_image)
