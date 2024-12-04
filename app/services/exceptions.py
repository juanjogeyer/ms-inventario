class StockInsuficienteException(Exception):
    """Excepción lanzada cuando no hay suficiente stock disponible."""
    def __init__(self, producto_id, cantidad_disponible, cantidad_requerida):
        self.producto_id = producto_id
        self.cantidad_disponible = cantidad_disponible
        self.cantidad_requerida = cantidad_requerida
        super().__init__(f"Stock insuficiente para el producto {producto_id}. "
                         f"Disponible: {cantidad_disponible}, Requerido: {cantidad_requerida}")
