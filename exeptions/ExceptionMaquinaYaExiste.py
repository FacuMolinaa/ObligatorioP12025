class ExceptionMaquinaYaExiste(Exception):
    
    def __init__(self, mensaje="Máquina ya registrada con esta descripción."):
        super().__init__(mensaje)