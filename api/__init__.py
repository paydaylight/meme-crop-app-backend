import time
from flask import jsonify
from flask_restful import Api, Resource
import config

api = Api(prefix=config.API_PREFIX)


class TaskStatusAPI(Resource):
   def get(self, task_id):
       return {}


class DataProcessingAPI(Resource):
   def post(self):

       return {'task_id': 0}, 200





# data processing endpoint
api.add_resource(DataProcessingAPI, '/process_data')

# task status endpoint
api.add_resource(TaskStatusAPI, '/tasks/<string:task_id>')