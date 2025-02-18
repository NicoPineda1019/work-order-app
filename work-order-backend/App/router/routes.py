from flask import Blueprint
from flask import jsonify, make_response, request
from App.useCase.order import Order
from App.utils.validity import Validity
bp = Blueprint('routes', __name__)

@bp.route('/v1/order', methods=['POST'])
def create_order():
    try:
        Validity.validateOrderRequest(request)
        response, status_code = Order.process(request)
    except Exception as e:
        print(f'{e}')
        response = {'error': f'{e}'}
        status_code = 400
    return make_response(jsonify(response), status_code)

@bp.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
