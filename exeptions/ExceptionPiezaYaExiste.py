class ExceptionPiezaYaExiste(Exception):
    
    def __init__(self, mensaje="Pieza ya registrada con esta descripción."):
        super().__init__(mensaje)