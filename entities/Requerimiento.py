class Requerimiento:
    
    def __init__(self, pieza, cantidad_necesaria: int):
        self.pieza = pieza
        self.cantidad_necesaria = cantidad_necesaria
    
    def __str__(self):
        return f"{self.cantidad_necesaria} x {self.pieza.descripcion} (Código {self.pieza.codigo})"