import csv
import sys
from itertools import combinations

tokens = {}

with open('localidades.csv', encoding='latin-1') as csv_localidades:
    csv_reader = csv.reader(csv_localidades, delimiter=',')
    acentos = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
    acentuadas = "áéíóú"
    for row in csv_reader:
        loc_original = row[0]
        localidad = loc_original.replace('(','').replace(')','').lower()
        for letra in acentuadas:
            if letra in localidad:
                localidad = localidad.replace(letra, acentos.get(letra))
        if len(localidad) > 3:
            tokensLocal = [localidad[x:y] for x, y in combinations(
			        range(len(localidad) + 1), r = 2) if y-x > 3]
            for token in tokensLocal:
                nuevoValor = tokens.get(token, [])
                nuevoValor.append(loc_original)
                tokens.update({token: nuevoValor})
        else:
            nuevoValor = tokens.get(localidad, [])
            nuevoValor.append(loc_original)
            tokens.update({localidad: nuevoValor})
    # print(sys.getsizeof(tokens))
    # while(True):
    #     valBusqueda = input("¿Qué quieres buscar?: ")
    #     comunidades = tokens.get(valBusqueda, [])
    #     for comunidad in comunidades:
    #         print(comunidad)
    #     print()
    