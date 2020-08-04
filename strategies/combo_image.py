from models.image import Image as ImageModel
from classes import ImageManipulator
from PIL import Image, ImageFont, ImageDraw
import uuid


class ComboImage:
    def __init__(self, mode=None):
        if mode is None:
            mode = {'vertical': False, 'horizontal': True}

        self.mode = mode

    def call(self, parent_id):
        parent_image = ImageModel.query.get(parent_id)
        parent_image_file = Image.open(parent_image.url)

        derivative_images = ImageModel.query.filter(ImageModel.parent_id == parent_id, ImageModel.finished == False)\
            .order_by(ImageModel.created_at)

        images_array = list(derivative_images)
        print(images_array)
        images_array = list(map(lambda i: Image.open(i.url), images_array))
        print(images_array)
        images_array.insert(0, parent_image_file)

        if len(images_array) < 4:
            blank_image = Image.new('RGB', parent_image_file.size, (255, 255, 255))
            while len(images_array) != 4:
                images_array.append(blank_image)

        gutter_boundary = 100
        total_width = 2 * parent_image_file.width + 3 * gutter_boundary
        total_height = max(images_array[0].size[1], images_array[1].size[1]) + \
                       max(images_array[2].size[1], images_array[3].size[1]) + \
                       3 * gutter_boundary

        canvas = Image.new('RGB', (total_width, total_height), (255, 255, 255))

        x = y = gutter_boundary
        if images_array[1].size[1] > images_array[0].size[1]:
            y = images_array[1].size[1] - images_array[0].size[1] + gutter_boundary
        canvas.paste(images_array[0], (x, y))

        x += parent_image_file.width + gutter_boundary
        if images_array[0].size[1] > images_array[1].size[1]:
            y = images_array[0].size[1] - images_array[1].size[1] + gutter_boundary
        canvas.paste(images_array[1], (x, y))

        x = gutter_boundary
        y = 2 * gutter_boundary + parent_image_file.height
        curr_y = y
        if images_array[2].size[1] < images_array[3].size[1]:
            y = images_array[3].size[1] - images_array[2].size[1] + curr_y
        canvas.paste(images_array[2], (x, y))

        x += parent_image_file.width + gutter_boundary
        if images_array[3].size[1] < images_array[2].size[1]:
            y = images_array[2].size[1] - images_array[3].size[1] + curr_y
        canvas.paste(images_array[3], (x, y))
        canvas.thumbnail((1920, 1080), Image.LANCZOS)
        logo = self.logo(canvas.size[0])

        canvas = ImageManipulator.concat_vertical(canvas, logo)

        new_id = str(uuid.uuid4())
        canvas_image = ImageModel(id=new_id,
                             url=f"uploads/{new_id}.png",
                             parent_id=parent_id,
                                  finished=True)
        canvas.save(f"uploads/{new_id}.png")
        canvas_image.save()
        return canvas_image

    def logo(self, width, height=50, text="made with meme crop app"):
        img = Image.new('RGB', (width, height), color="white")
        font = ImageFont.truetype("assets/fonts/Montserrat/Montserrat-Light.ttf", 40)
        d = ImageDraw.Draw(img)
        w, h = d.textsize(text, font=font)
        h += int(h * 0.21)
        d.text(((width - w), (height - h) / 2), text=text, fill='black', font=font)
        return img



