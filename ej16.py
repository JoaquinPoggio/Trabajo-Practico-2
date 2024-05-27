def interseccion(pila1, pila2):
    conjunto1 = set(pila1)
    conjunto2 = set(pila2)
    interseccion = conjunto1.intersection(conjunto2)
    return list(interseccion)

pila_V = []
pila_VII = []

pjs_V = ["Luke", "Princesa Leia", "Han Solo", "Darth Vader", "Yoda", "Chewbacca" ]
for pj in pjs_V:
    pila_V.append(pj)

pjs_VII = ["Rey", "Finn", "Princesa Leia", "Han Solo", "Luke", "Chewbacca"]
for pj in pjs_VII:
    pila_VII.append(pj)

personajes = interseccion(pila_V, pila_VII)
print("Personajes que estén en los dos episodios:", personajes)