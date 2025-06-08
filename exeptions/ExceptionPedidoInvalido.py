class ExceptionPedidoInvalido(Exception):
    
    def __init__(self, mensaje="Pedido inválido o no se puede procesar."):
        super().__init__(mensaje)