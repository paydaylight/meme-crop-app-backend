from flask_restful import Api
import config
from api.v1.images_controller import UploadImage

api = Api(prefix=config.API_V1_PREFIX)

api.add_resource(UploadImage, '/image')