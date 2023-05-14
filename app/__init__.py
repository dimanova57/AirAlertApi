import secrets
from flask import Flask, make_response
from flask_cors import CORS
import json
from app.db_communicate import get_list_of_region


AIR_ALERT_is = True

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(16)

CORS(app)


@app.route('/<region_name>')
def air_alert_main(region_name):
    if name == 'all':
        regions = get_list_of_region()
        response = make_response(regions)
        return response




