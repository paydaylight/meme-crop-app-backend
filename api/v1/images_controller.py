from flask_restful import Resource, reqparse
import werkzeug
from models.image import Image
import uuid
from strategies import ParentImage, DerivativeImage
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
    def get(self, parent_id):
        parser = reqparse.RequestParser()
        parser.add_argument('caption', type=str, required=True, help="Caption cannot be blank!")
        parser.add_argument('horizontal', type=bool)
        args = parser.parse_args()
        caption = args['caption']

        if args['horizontal']:
            mode = {'horizontal': True}
        else:
            mode = {'vertical': True}

        print(mode, args)

        strategy = DerivativeImage(mode)
        derivative_image = strategy.call(parent_id, caption)

        return serializers.serialize_image(derivative_image)


