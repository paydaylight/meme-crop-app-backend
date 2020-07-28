from flask_restful import Resource


class UploadImage(Resource):
    def post(self):
        print("here!")
        return {'msg': "a"}, 200


