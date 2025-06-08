class ExceptionStockInsuficiente(Exception):
    
    def __init__(self, mensaje="Stock insuficiente para completar esta operación."):
        super().__init__(mensaje)