def posicion_rocket_groot(pila_pjs):
    pos = len(pila_pjs)
    for personaje in pila_pjs[::-1]:
        if personaje[0] == "Rocket Raccoon" or personaje[0] == "Groot":
            return pos
        pos -= 1
    return "Rocket Raccoon y Groot no están en la pila"

def pjs_mas_5_pelis(pila_pjs):
    personajes = []
    for personaje in pila_pjs:
        if personaje[1] > 5:
            personajes.append((personaje[0], personaje[1]))
    return personajes

def pelis_black_widow(pila_pjs):
    for personaje in pila_pjs:
        if personaje[0] == "Black Widow":
            return personaje[1]
    return "Black Widow no está en la pila"

def iniciales_pjs(pila_pjs, iniciales):
    personajes = []
    for personaje in pila_pjs:
        if personaje[0][0] in iniciales:
            personajes.append(personaje[0])
    return personajes

pila_pjs = []

#'Nombre del heroe, cantidad de pelis en el MCU'
pjs_mcu = [
    ('Iron Man', 10),
    ('Cap America', 8),
    ("Thor", 7),
    ("Hulk", 6),
    ("Black Widow", 7),
    ("Hawkeye", 5),
    ("Spider Man", 5),
    ("Black Panther", 4),
    ("Dr Strange", 4),
    ("Rocket Raccoon", 5),
    ("Groot", 4),
    ("Wanda", 4),
    ("Falcon", 4),
    ("War Machine", 4),
    ("Ant Man", 3),
    ("Bucky", 3),
    ("Vision", 3),
    ("Wasp", 2),
    ("Capitana Marvel", 2),
    ("Drax", 2),
    ("Gamora", 2),
    ("Star Lord", 2),
    ("Mantis", 2),
    ("Nebula", 2),
    ("Thanos", 3),
]

for pj in pjs_mcu:
    pila_pjs.append(pj)

print("Posicion de Rocket Racoon y Groot:", posicion_rocket_groot(pila_pjs))
print("Personajes que salen en mas de 5 peliculas", pjs_mas_5_pelis(pila_pjs))
print("Peliculas en las que aparece Black Widow", pelis_black_widow(pila_pjs))
print("Personajes cuyos nombres empiezan con C, D y G:", iniciales_pjs(pila_pjs, ["C", "D", "G"]))
