from datetime import datetime

class Pedido:
    ESTADO_ENTREGADO = "entregado"
    ESTADO_PENDIENTE = "pendiente"
    
    def __init__(self, cliente, maquina):
        self.cliente = cliente
        self.maquina = maquina
        self.fecha_recepcion = datetime.now()
        self.fecha_entrega = None
        self.estado = Pedido.ESTADO_PENDIENTE
        self.precio_venta = 0.0
        self._calcular_precio_venta()
    
    def _calcular_precio_venta(self):
        base = self.maquina.costo_produccion * 1.5
        if self.cliente.tipo() == "Empresa":
            base *= 0.8
        self.precio_venta = base
    
    def entregar(self):
        self.estado = Pedido.ESTADO_ENTREGADO
        self.fecha_entrega = datetime.now()
    
    def __str__(self):
        estado = self.estado
