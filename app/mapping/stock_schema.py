from marshmallow import validate, Schema, fields, post_load
from app.models import Stock

class StockSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto = fields.Integer(required=True)
    fecha_transaccion = fields.DateTime(required=False)
    cantidad = fields.Float(required=True, validate=validate.Range(min=0))
    entrada_salida = fields.Integer(required=True, validate=validate.OneOf([1, 2]))  # 1: entrada, 2: salida

    @post_load
    def make_stock(self, data, **kwargs):
        return Stock(**data)