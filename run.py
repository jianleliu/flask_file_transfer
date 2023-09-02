"""Start the application by running this python script."""

import api
from config import AppConfig
from lib.sql.query import max_allowed_packet, get_max_allowed_packet

#Flask Object.
web = api.web

def update_max_allowed_packet(max_packet:int):
    """Check if the max_allowed_packet is equal to MAX_CONTENT_LENGTH.
       Update if false.
    """
    if max_packet != AppConfig.MAX_CONTENT_LENGTH:
        max_allowed_packet(AppConfig.MAX_CONTENT_LENGTH)

if __name__ == '__main__':
    #Flask Configs.
    web.secret_key = AppConfig.SECRET_KEY
    web.config['SESSION_TYPE'] = AppConfig.SESSION_TYPE
    web.config['UPLOAD_FOLDER'] = AppConfig.UPLOAD_FOLDER
    web.config['MAX_CONTENT_LENGTH'] = AppConfig.MAX_CONTENT_LENGTH
    #Other configs.
    update_max_allowed_packet(get_max_allowed_packet())
    #Run Flask app.
    web.run(
        host=AppConfig.HOST,
        port=AppConfig.PORT,
        debug=AppConfig.DEBUG
        )
