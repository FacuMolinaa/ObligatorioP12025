class ExceptionClienteYaExiste(Exception):
    
    def __init__(self, mensaje="Cliente ya registrado con este identificador."):
        super().__init__(mensaje)