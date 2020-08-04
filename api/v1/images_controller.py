from flask_restful import Resource, reqparse
import werkzeug
from models.image import Image
import uuid
from strategies import ParentImage, DerivativeImage, ComboImage
from flask import jsonify, request
import serializers


class UploadOriginalImage(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('caption', type=str, required=True, help="Caption cannot be blank!")
        parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')

        args = parser.parse_args()
        print(args)
        og_file = args['image']
        caption = args['caption']
        og_file_path = f"uploads/{uuid.uuid4()}.png"
        og_file.save(og_file_path)

        strategy = ParentImage(og_file_path, caption)
        og_image_with_caption = strategy.call()

        return serializers.serialize_image(og_image_with_caption)


class GetImageFromCaption(Resource):
    def post(self, parent_id):
        parser = reqparse.RequestParser()
        parser.add_argument('caption', type=str, required=True, help="Caption cannot be blank!")
        parser.add_argument('vertical', type=str)
        args = parser.parse_args()
        caption = args['caption']

        if args['vertical']:
            mode = {'vertical': True, 'horizontal': False}
        else:
            mode = {'horizontal': True, 'vertical': False}

        strategy = DerivativeImage(mode)
        derivative_image = strategy.call(parent_id, caption)

        return serializers.serialize_image(derivative_image)


class ImageCombo(Resource):
    def post(self, parent_id):
        strategy = ComboImage()
        canvas = strategy.call(parent_id)
        return serializers.serialize_image(canvas)



