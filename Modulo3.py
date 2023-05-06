# Funcion para imprimir listados varios, se crea con dos requerimientos el cuel uno muestra que listado es y el otro el item de los listados
def imprimir_nombres(mostrar, Titulo):
    print("-----" + Titulo + "-------\n")
    for item in mostrar:
        print(item)
    print("\n----FIN LISTADO----\n\n")


# Listado Inicial
Listado = [
    "Harry Houdini",
    "Newton",
    "David Blaine",
    "Hawking",
    "Messi",
    "Teller",
    "Einstein",
    "Pele",
    "Juanes",
]


# Funcion Para manipular magos y a la vez crear los distintos listados solicitados magos, cientificos y otros
def hacer_grandioso(Listado):
    for valor in Listado:
        if valor == "Harry Houdini" or valor == "David Blaine" or valor == "Teller":
            # Se agrega El gran al listado de magos junto con el item
            magos.append("El Gran " + valor)
            # se remueve los que no corresponde a cientifico ni a magos
            otros.remove(valor)
        elif valor == "Newton" or valor == "Hawking" or valor == "Einstein":
            # Se agrega item segun corresponda en los if
            cientificos.append(valor)
            # se remueve los que no corresponde a cientifico ni a magos
            otros.remove(valor)


# Se inicializa el listado magos en cero
magos = []
# se inicializa el listado cientificos en cero
cientificos = []
# Se crea listado otros duplicando el listado inicial Listado
otros = list(Listado)

# se llama a la funcion hacer grandioso, el cual manipula todas los listados solicitados
hacer_grandioso(Listado)

# Se invoca la funcionimprimir_nombres para mostrar los listados
imprimir_nombres(Listado, "Listado Inicial")
imprimir_nombres(magos, "Listado de Magos")
imprimir_nombres(cientificos, "Listado de Científicos")
imprimir_nombres(otros, "Listado de Otros")
