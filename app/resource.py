from flask import Blueprint, request
from marshmallow import ValidationError
from .services import StockService, ResponseBuilder
from .mapping import StockSchema, ResponseSchema

stock = Blueprint('stock', __name__)

response_schema = ResponseSchema()
stock_schema = StockSchema()
stock_service = StockService()

@stock.route('/inventarios/ingresar', methods=['PUT'])
def ingresar_producto():
    response_builder = ResponseBuilder()
    try:
        stock = stock_schema.load(request.json)
        data = stock_schema.dump(stock_service.ingresar(stock))
        response_builder.add_message("Inventario added").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422

@stock.route('/inventarios/retirar', methods=['POST'])
def retirar_producto():
    response_builder = ResponseBuilder()
    try:
        stock = stock_schema.load(request.json)
        data = stock_schema.dump(stock_service.retirar(stock))
        response_builder.add_message("Inventario added").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422