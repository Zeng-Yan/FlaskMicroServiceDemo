# cython: language_level=3

from flask import jsonify, Response
from flask import current_app as app  # using an application context

from src.configs import STATUS_CODE


@app.route(f'/')  # a URL binding for function below.
def web_init() -> Response:  # a function dealing with URL request.
    response = {'info': '[INFO] welcome', 'status': STATUS_CODE['success']}
    return jsonify(response)
