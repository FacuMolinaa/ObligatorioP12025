class Maquina:
    _contador_codigo = 1
    def __init__(self, descripcion: str):
        self.codigo = Maquina._contador_codigo
        Maquina._contador_codigo += 1
        self.descripcion = descripcion
        self.requerimientos = []
        self.costo_produccion = 0.0
   
    def agregar_requerimiento(self, requerimiento):
        self.requerimientos.append(requerimiento)
        self._calcular_costo_produccion()
    
    def _calcular_costo_produccion(self):
        total = 0.0
        for req in self.requerimientos:
            total += req.pieza.costo_unitario * req.cantidad_necesaria
        self.costo_produccion = total
    
    def __str__(self):
        return f"Máquina {self.codigo} - {self.descripcion} - Costo producción: ${self.costo_produccion:.2f}"