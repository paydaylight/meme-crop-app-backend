from classes import ImageManipulator
from models import Image
import uuid


class ParentImage:
    def __init__(self, image_path, caption_text):
        self.manipulator = ImageManipulator(image_path, caption_text)

    def call(self):
        caption_image = self.manipulator.caption_image(self.manipulator.caption_text, self.manipulator.width, 50)
        image_with_caption = self.manipulator.concat_horizontal(self.manipulator.image, caption_image)
        image_id = uuid.uuid4()
        stored = Image(id=image_id, caption=self.manipulator.caption_text, url=self.manipulator.image_path(image_id))
        stored.save()
        image_with_caption.save(self.manipulator.image_path(image_id))
