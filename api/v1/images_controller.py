from flask_restful import Resource
from models import Image

class UploadOriginalImage(Resource):
    def post(self):
        print("here!")
        return {'success': True}, 200


class GetImageFromCaption(Resource):
    def get(self):
        target_image = Image.query("")
        return {'success': True}, 200


