from entities.Pieza import Pieza
from entities.Maquina import Maquina
from entities.Requerimiento import Requerimiento
from entities.Cliente import ClienteParticular, Empresa
from entities.Pedido import Pedido
from entities.Sistema import Sistema

from exeptions import ExceptionClienteYaExiste
from exeptions import ExceptionPiezaYaExiste
from exeptions import ExceptionMaquinaYaExiste


def menu_principal():
    print("=============== Menú Principal ===============")
    print("1 - Registrar")
    print("2 - Listar")
    print("3. Salir")

def menu_registrar():
    print("=============== Registrar ===============")
    print("1 - Pieza")
    print("2 - Máquina")
    print("3 - Cliente")
    print("4 - Pedido")
    print("5 - Reposición")
    print("6. Volver")

def menu_listar():
    print("=============== Listar ===============")
    print("1 - Clientes")
    print("2 - Pedidos")
    print("3 - Máquinas")
    print("4 - Piezas")
    print("5 - Contabilidad")
    print("6. Volver")

def registrar_pieza(sistema):
    print("=============== Registrar Pieza ===============")
    descripcion = input("Descripción: ")
    costo = input("Costo unitario: ")
    tamano_lote = input("Tamaño de lote Reposición: ")
    
    try:
        costo = float(costo)
        tamano_lote = int(tamano_lote)
        pieza = Pieza(descripcion, costo, tamano_lote)
        sistema.agregar_pieza(pieza)
        print(f"Pieza {pieza.codigo} registrada.")
    
    except ValueError:
        print("Error: Costo o tamaño de lote inválido.")
   
    except ExceptionPiezaYaExiste as e:
        print("Error:", e)

def registrar_maquina(sistema):
    print("--- Registrar Máquina ---")
    descripcion = input("Descripción: ")
    maquina = Maquina(descripcion)
    
    while True:
        opcion = input("Agregar requisito de pieza? (s/n): ")
        if opcion != "s":
            break
       
        print("Piezas disponibles:")
        piezas_usadas = {r.pieza for r in maquina.requerimientos}
        piezas_disponibles = [p for p in sistema.piezas if p not in piezas_usadas]
        
        for p in piezas_disponibles:
            print(f"{p.codigo} - {p.descripcion}")
        codigo = input("Código pieza: ")
        
        try:
            codigo = int(codigo)
        
        except ValueError:
            print("Código inválido.")
            continue
        
        pieza_sel = None
        
        for p in piezas_disponibles:
            if p.codigo == codigo:
                pieza_sel = p
                break
        
        if not pieza_sel:
            print("Pieza inválida.")
            continue
        cantidad = input("Cantidad necesaria: ")
        
        try:
            cantidad = int(cantidad)
        
        except ValueError:
            print("Cantidad inválida.")
            continue
        req = Requerimiento(pieza_sel, cantidad)
        maquina.agregar_requerimiento(req)
    
    try:
        sistema.agregar_maquina(maquina)
        print(f"Máquina {maquina.codigo} registrada.")
    
    except ExceptionMaquinaYaExiste as e:
        print("Error:", e)

def registrar_cliente(sistema):
    print(" -- Registrar Cliente --")
    tipo = input("Tipo (1 - Particular, 2 - Empresa): ")

    if tipo == "1":
        cedula = input("Cedula: ")
        nombre = input("Nombre completo: ")
        telefono = input("Telefono: ")
        correo = input("Correo: ")
        cliente = ClienteParticular(cedula, nombre, telefono, correo)

    elif tipo == "2":
        rut = input("RUT: ")
        nombre = input("Nombre Empresa: ")
        pagina = input("Pagina web: ")
        telefono = input("Teléfono: ")
        correo = input("Correo: ")
        cliente = Empresa(rut, nombre, pagina, telefono, correo)

    else:
        print("Tipo inválido.")
        return

    try:
        sistema.agregar_cliente(cliente)
        print(f"Cliente {cliente.id_cliente} registrado.")
    except ExceptionClienteYaExiste as e:
        print("Error:", e)

def registrar_pedido(sistema):
    
    print("-- Registrar Pedido --")
    
    if len(sistema.clientes) == 0 or len(sistema.maquinas) == 0:
        print("Debe haber clientes y máquinas registradas primero.")
        return
    print("Clientes:")
    
    for c in sistema.clientes:
        print(f"{c.id_cliente} - {c}")
    id_cliente = input("ID Cliente: ")
    
    try:
        id_cliente = int(id_cliente)
    
    except ValueError:
        print("ID inválido.")
        return
    cliente = None
    
    for c in sistema.clientes:
    
        if c.id_cliente == id_cliente:
            cliente = c
            break
    
    if cliente is None:
        print("Cliente no encontrado.")
        return
    print("Máquinas:")
    
    for m in sistema.maquinas:
        print(f"{m.codigo} - {m.descripcion}")
    codigo_maquina = input("Código máquina: ")
    
    try:
        codigo_maquina = int(codigo_maquina)
    
    except ValueError:
        print("Código inválido.")
        return
    maquina = None
    
    for m in sistema.maquinas:
        if m.codigo == codigo_maquina:
            maquina = m
            break
    
    if maquina is None:
        print("Máquina no encontrada.")
        return
    pedido = Pedido(cliente, maquina)
    sistema.pedidos.append(pedido)
    print("Pedido registrado.")

def registrar_reposicion(sistema):
    print("====== Registrar Reposición ======")
    
    if len(sistema.piezas) == 0:
        print("No hay piezas para reponer.")
        return
    
    for p in sistema.piezas:
        print(f"{p.codigo} - {p.descripcion}")
    codigo = input("Código pieza: ")
    
    try:
        codigo = int(codigo)
    except ValueError:
        print("Código inválido.")
        return
    pieza = None
    for p in sistema.piezas:
        if p.codigo == codigo:
            pieza = p
            break
    if pieza is None:
        print("Pieza no encontrada.")
        return
    cantidad_lotes = input("Cantidad de lotes a reponer: ")
    try:
        cantidad_lotes = int(cantidad_lotes)
    except ValueError:
        print("Cantidad inválida.")
        return
    pieza.reponer_stock(cantidad_lotes)
    print("Reposición registrada.")


def listar_clientes(sistema):
    print("-- Clientes --")
    for c in sistema.clientes:
        print(c)

def listar_pedidos(sistema):
    print("-- Pedidos --")
    for p in sistema.pedidos:
        print(p)

def listar_maquinas(sistema):
    print("-- Máquinas --")
    for m in sistema.maquinas:
        print(m)

def listar_piezas(sistema):
    print("-- Piezas --")
    for p in sistema.piezas:
        print(p)

def listar_contabilidad(sistema):
    print("-- Contabilidad --")
    
    costo_total = 0
    ingreso_total = 0

    for pedido in sistema.pedidos:
        if pedido.estado == Pedido.ESTADO_ENTREGADO:
            costo_total += pedido.maquina.costo_produccion
            ingreso_total += pedido.precio_venta

    ganancia = ingreso_total - costo_total
    impuesto = ganancia * 0.25
    ganancia_final = ganancia - impuesto

    
    print(f"Costo total: ${costo_total:.2f}")
    print(f"Ingreso total: ${ingreso_total:.2f}")
    print(f"Ganancia: ${ganancia:.2f}")
    print(f"Impuesto IRAE (25%): ${impuesto:.2f}")
    print(f"Ganancia final: ${ganancia_final:.2f}")

def main():
    sistema = Sistema()
    while True:
        menu_principal()
        opcion = input("Opción: ")
        if opcion == "1":
            while True:
                menu_registrar()
                op_reg = input("Opción: ")
                if op_reg == "1":
                    registrar_pieza(sistema)
                elif op_reg == "2":
                    registrar_maquina(sistema)
                elif op_reg == "3":
                    registrar_cliente(sistema)
                elif op_reg == "4":
                    registrar_pedido(sistema)
                elif op_reg == "5":
                    registrar_reposicion(sistema)
                elif op_reg == "6":
                    break
                else:
                    print("Opción inválida.")
        
        elif opcion == "2":
            while True:
                menu_listar()
                op_list = input("Opción: ")
                if op_list == "1":
                    listar_clientes(sistema)
                elif op_list == "2":
                    listar_pedidos(sistema)
                elif op_list == "3":
                    listar_maquinas(sistema)
                elif op_list == "4":
                    listar_piezas(sistema)
                elif op_list == "5":
                    listar_contabilidad(sistema)
                elif op_list == "6":
                    break
                else:
                    print("Opción inválida.")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
