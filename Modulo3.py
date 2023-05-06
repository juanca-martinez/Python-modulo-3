def imprimir_nombres(mostrar, Titulo):
    print("-----" + Titulo + "-------\n")
    for item in mostrar:
        print(item)
    print("\n----FIN LISTADO----\n\n")


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


def hacer_grandioso(Listado):
    for valor in Listado:
        if valor == "Harry Houdini" or valor == "David Blaine" or valor == "Teller":
            magos.append("El Gran " + valor)
            otros.remove(valor)
        elif valor == "Newton" or valor == "Hawking" or valor == "Einstein":
            cientificos.append(valor)
            otros.remove(valor)


magos = []
cientificos = []
otros = list(Listado)
hacer_grandioso(Listado)
imprimir_nombres(Listado, "Listado Inicial")
imprimir_nombres(magos, "Listado de Magos")
imprimir_nombres(cientificos, "Listado de Científicos")
imprimir_nombres(otros, "Listado de Otros")
