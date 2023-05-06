def imprimeLista(mostrar, Titulo):
    print("-----" + Titulo + "-------\n")
    for item in mostrar:
        print(item)
    print('\n----FIN LISTADO----\n')

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


magos = []
cientificos = []
otros = list(Listado)

for indice, valor in enumerate(Listado):
    print(indice, valor)
    if valor == "Harry Houdini" or valor == "David Blaine" or valor == "Teller":
        #print(valor + " es el mejor mago de todos los tiempos")
        magos.append("El Gran " + valor)
        otros.remove(valor)
    elif valor == "Newton" or valor == "Hawking" or valor == "Einstein":
        #print(valor + " es el mejor cientifico de todos los tiempos")
        cientificos.append(valor)
        otros.remove(valor)


imprimeLista(magos, "Listado de Magos")
imprimeLista(cientificos, "Listado de Cientificos")
imprimeLista(otros, "Listado de Otros")

