from app.repository import StockRepository
from app.models import Stock
from datetime import datetime
from app import cache

repository = StockRepository()

class StockService:

    def retirar(self, stock: Stock) -> Stock:
        if stock is not None:
            stock_actual = repository.calcular_stock_total(stock.producto)
            if stock_actual < stock.cantidad:
                raise ValueError(
                    f"Stock insuficiente para el producto {stock.producto}. "
                    f"Disponible: {stock_actual}, solicitado: {stock.cantidad}"
                )
            
            # Configuramos la salida como -1 y registramos la transacción
            stock.fecha_transaccion = stock.fecha_transaccion or datetime.now()
            stock.entrada_salida = -1  # Salida de producto
            result = repository.add(stock)
            cache.set(f'stock_{stock.id}', result, timeout=60)
            return result

    def ingresar(self, stock: Stock) -> Stock:
        if stock is not None:
            stock.fecha_transaccion = stock.fecha_transaccion or datetime.now()
            stock.entrada_salida = 1  # Entrada de producto
            result = repository.add(stock)
            cache.set(f'stock_{stock.id}', result, timeout=60)
            return result