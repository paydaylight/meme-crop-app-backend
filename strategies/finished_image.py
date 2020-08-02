from models.image import Image as ImageModel
from classes import ImageManipulator
from PIL import Image
class FinishedImage:
    def __init__(self):
        self.manipulator = ImageManipulator(None, None)

    def call(self, parent_id):
        parent_image = ImageModel.query(id=parent_id).first()
        derivative_images = parent_image.derivatives

        images_array = list(derivative_images)
        map(lambda i: Image.open(i.url), derivative_images)
        images_array.insert(0, Image.open(parent_image.url))

        for image in images_array:
            pass

