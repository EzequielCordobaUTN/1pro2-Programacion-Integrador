import csv

def cargar_paises(ruta):
    with open(ruta, encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        return [
            {
                'nombre': fila['nombre'].strip(),
                'poblacion': int(fila['poblacion']),
                'superficie': int(fila['superficie']),
                'continente': fila['continente'].strip()
            }
            for fila in lector
        ]

def buscar_pais(paises, termino):
    termino = termino.lower()
    return [
        pais for pais in paises
        if termino in pais['nombre'].lower()
    ]

def filtrar_por_continente(paises, continente):
    continente = continente.lower()
    return [
        pais for pais in paises
        if pais['continente'].lower() == continente
    ]

def filtrar_por_poblacion(paises, minimo, maximo):
    return [
        pais for pais in paises
        if minimo <= pais['poblacion'] <= maximo
    ]

def filtrar_por_superficie(paises, minimo, maximo):
    return [
        pais for pais in paises
        if minimo <= pais['superficie'] <= maximo
    ]
