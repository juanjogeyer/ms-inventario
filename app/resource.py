from flask import Blueprint, request
from marshmallow import ValidationError
from .services import StockService, ResponseBuilder
from .mapping import StockSchema, ResponseSchema

inventario = Blueprint('inventario', __name__)

response_schema = ResponseSchema()
stock_schema = StockSchema()
stock_service = StockService()

@inventario.route('/inventario', methods=['GET'])
def index():
    response_builder = ResponseBuilder()
    data = stock_schema.dump(stock_service.all(), many=True)
    response_builder.add_message("Inventario found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@inventario.route('/inventario', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    try:
        stock = stock_schema.load(request.json)
        data = stock_schema.dump(stock_service.save(stock))
        response_builder.add_message("Inventario added").add_status_code(201).add_data(data)
        return response_schema.dump(response_builder.build()), 201
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422

@inventario.route('/inventario/<int:id>', methods=['DELETE'])
def delete(id):
    response_builder = ResponseBuilder()
    data = stock_service.delete(id)
    if data:
        response_builder.add_message("Inventario deleted").add_status_code(200).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Inventario not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404