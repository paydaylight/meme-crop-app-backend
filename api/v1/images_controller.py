from flask_restful import Resource, reqparse
import werkzeug
from models.image import Image
import uuid
from strategies import ParentImage
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

        # print(og_image_with_caption)

        return serializers.serialize_image(og_image_with_caption)


class GetImageFromCaption(Resource):
    def get(self):
        target_image = Image.query("")
        return {'success': True}, 200


