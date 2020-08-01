from flask_restful import Api
import config
from api.v1.images_controller import UploadOriginalImage, GetImageFromCaption

api = Api(prefix=config.API_V1_PREFIX)

api.add_resource(UploadOriginalImage, '/images')
api.add_resource(GetImageFromCaption, '/images/<string:parent_id>/derivative')