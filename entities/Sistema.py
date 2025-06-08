from exeptions import ExceptionPiezaYaExiste, ExceptionMaquinaYaExiste, ExceptionClienteYaExiste
from entities.Cliente import ClienteParticular, Empresa
class Sistema:
    def __init__(self):
        self.piezas = []
        self.maquinas = []
        self.clientes = []
        self.pedidos = []
        self.reposiciones = []

    def agregar_pieza(self, pieza):
        
        if any(p.descripcion == pieza.descripcion for p in self.piezas):
            raise ExceptionPiezaYaExiste(f"Pieza con descripción '{pieza.descripcion}' ya existe.")
        self.piezas.append(pieza)

    def buscar_pieza_por_codigo(self, codigo):
        for p in self.piezas:
            if p.codigo == codigo:
                return p
        return None

    def agregar_maquina(self, maquina):
        if any(m.descripcion == maquina.descripcion for m in self.maquinas):
            raise ExceptionMaquinaYaExiste(f"Máquina con descripción '{maquina.descripcion}' ya existe.")
        self.maquinas.append(maquina)

    def agregar_cliente(self, cliente):
        if isinstance(cliente, ClienteParticular):
            if any(isinstance(c, ClienteParticular) and c.cedula == cliente.cedula for c in self.clientes):
                raise ExceptionClienteYaExiste(f"Cédula '{cliente.cedula}' ya registrada.")
        elif isinstance(cliente, Empresa):
            if any(isinstance(c, Empresa) and c.rut == cliente.rut for c in self.clientes):
                raise ExceptionClienteYaExiste(f"RUT '{cliente.rut}' ya registrado.")
        self.clientes.append(cliente)


