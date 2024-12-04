from app import db
from app.models import Stock

class StockRepository:
    
    def add(self, stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock
    
    def calcular_stock_total(self, producto_id: int) -> float:
        result = db.session.query(
            db.func.sum(Stock.cantidad * Stock.entrada_salida)).filter(Stock.producto == producto_id).scalar()

        return result if result else 0.0