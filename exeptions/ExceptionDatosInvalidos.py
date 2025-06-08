class ExceptionDatosInvalidos(Exception):
    
    def __init__(self, mensaje="Datos ingresados no válidos."):
        super().__init__(mensaje)