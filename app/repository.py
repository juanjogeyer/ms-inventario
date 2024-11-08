from app import db
from app.models import Stock

class StockRepository:
    
    def add(self, stock: Stock) -> Stock:
        db.session.add(stock)
        db.session.commit()
        return stock