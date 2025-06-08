import datetime

class Reposición:
    def __init__(self, pieza, cantidad, fecha):
        self.reposicion = []
        self.pieza = pieza
        self.cantidad = cantidad
        self.fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d")
        if self.cantidad <= 0:
            raise ValueError("La cantidad de piezas a reponer debe ser mayor que cero.")
        self.fecha_reposición = None
    
    def registrar_reposición(self, fecha_reposición):
        if self.fecha_reposición is None:
            self.fecha_reposición = fecha_reposición
        else:
            raise ValueError("La reposición ya ha sido registrada.")