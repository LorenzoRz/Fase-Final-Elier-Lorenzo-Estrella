"""
Nombre del estudiante: Elier Lorenzo Estrella Rodriguez
Grupo: 213022
Programa: Ingenieria de Sistemas
Código Fuente: Auditoria Propia
"""

inventario = [
    ["001", "Telefono", 10, 10],
    ["002", "Portatil", 10, 10],
    ["003", "Lampara", 10, 10],
    ["004", "Teclados", 10, 10],
    ["005", "Microhondas", 10, 10]
]

# Esta funcion nos ayuda a calcular la cantidad exacta a pedir
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

def inventario_tienda(arreglo_inventario):
    print("___________________________________________________________")
    print("       LISTA DE PEDIDOS DE INVENTARIO        ")
    print("___________________________________________________________")
    print("CODIGO|ARTICULO|CANTIDAD A PEDIR")
    
    hubo_pedidos = False
    
# Recorremos el arreglo para validar si necesitamos realizar un pedido.
    for articulo in arreglo_inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]
        
        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
# En la siguiente condicion filtramos los articulos que necesitan realizar un pedido..
        if cantidad_pedir > 0:
            print(f"{codigo} | {nombre} | {cantidad_pedir}")
            hubo_pedidos = True
            
    if not hubo_pedidos:
        print("El inventario esta completo.")
        
    print("___________________________________________________________")

inventario_tienda(inventario)