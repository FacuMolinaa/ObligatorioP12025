class Pieza:
    _contador_codigo = 1

    def __init__(self, descripcion: str, costo_unitario: float, tamano_lote: int, cantidad_disponible = 0):
        self.codigo = Pieza._contador_codigo
        Pieza._contador_codigo += 1
        self.descripcion = descripcion
        self.costo_unitario = costo_unitario
        self.tamano_lote = tamano_lote
        self.cantidad_disponible = cantidad_disponible

    def reponer_stock(self, cantidad_lotes: int):
        
        self.cantidad_disponible += cantidad_lotes * self.tamano_lote

    def consumir_stock(self, cantidad: int):

        if cantidad > self.cantidad_disponible:
            raise ValueError("No hay suficiente stock para consumir")
        self.cantidad_disponible -= cantidad

    def __str__(self):
        return f"Pieza {self.codigo} - {self.descripcion} (Disponible: {self.cantidad_disponible})"
