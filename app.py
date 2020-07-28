from flask import Flask
import config
import api
import logging

# logging.basicConfig(level=logging.DEBUG,
#                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
#                    datefmt='%Y-%m-%d %H:%M:%S',
#                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
      # logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)
    app.config.from_object('config')
    api.v1.api.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)