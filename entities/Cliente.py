from abc import ABC, abstractmethod
class Cliente(ABC):
    _contador_id = 1
    def __init__(self, telefono: str, correo: str):
        self.id_cliente = Cliente._contador_id
        Cliente._contador_id += 1
        self.telefono = telefono
        self.correo = correo

    @abstractmethod
    def tipo(self):
        pass
    def __str__(self):
        return f"ID {self.id_cliente} - Tipo: {self.tipo()}"

class ClienteParticular(Cliente):
    
    def __init__(self, cedula: str, nombre_completo: str, telefono: str, correo: str):
        super().__init__(telefono, correo)
        self.cedula = cedula
        self.nombre_completo = nombre_completo
    
    def tipo(self):
        return "Particular"
    
    def __str__(self):
        return f"{super().__str__()} - {self.nombre_completo} (Cédula: {self.cedula} - Teléfono: {self.telefono} - Correo: {self.correo})"

class Empresa(Cliente):
    
    def __init__(self, rut: str, nombre: str, pagina_web: str, telefono: str, correo: str):
        super().__init__(telefono, correo)
        self.rut = rut
        self.nombre = nombre
        self.pagina_web = pagina_web
    
    def tipo(self):
        return "Empresa"
    
    def __str__(self):
        return f"{super().__str__()} - {self.nombre} (RUT: {self.rut})"