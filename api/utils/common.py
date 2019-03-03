import traceback
from typing import Type
from flask import request
from logzero import logger
from http import HTTPStatus
from functools import partial
from flask import jsonify, make_response


def json_response(data=None, status: HTTPStatus = HTTPStatus.OK, headers=None):
    """

    Returns json response with given payload, status and headers

    :param data: Data to response
    :type data: Any
    :param status: Http status code in response
    :type staus: HTTPStatus
    :param headers: Header information in response

    """

    headers = headers or {}

    if "Content-Type" not in headers:
        headers["Content-Type"] = "application/json"
    return make_response(jsonify(data), status, headers)


def log_error(error_message, code):
    tb = traceback.format_exc(limit=5)
    path = "?".join([request.path, request.query_string]) if request.query_string else request.path

    logger.error(f"{request.remote_addr} {request.method} {path} {code} {error_message} \n {tb}")


def error_response(message, code):
    return {"message": message}, code
