from models.image import Image as ImageModel
from classes import ImageManipulator
from PIL import Image


class ComboImage:
    # def __init__(self):
    #     self.manipulator = ImageManipulator(None, None)

    def call(self, parent_id):
        parent_image = ImageModel.query.get(parent_id)
        derivative_images = ImageModel.query.filter(ImageModel.parent_id == parent_id).order_by(ImageModel.created_at)
        print(derivative_images, parent_image)
        images_array = list(derivative_images)
        map(lambda i: Image.open(i.url), derivative_images)
        images_array.insert(0, Image.open(parent_image.url))

        print(len(images_array))
        for image in images_array:
            pass

