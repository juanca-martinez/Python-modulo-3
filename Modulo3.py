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
Otros = []

for lista in Listado:
    print(lista)
    if lista == 'Harry Houdini' or lista == "David Blaine" or lista == "Teller":
        print(lista + " es el mejor mago de todos los tiempos")
    elif lista == 'Newton' or lista == "Hawking" or lista == "Einstein":
        print(lista + " es el mejor cientifico de todos los tiempos")
    else:
        print(lista + " es el mejor deportista de todos los tiempos")
