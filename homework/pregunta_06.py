"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """

    with open("files/input/data.csv", "r") as file:
        lines = file.readlines()

    key_min_max = {}
    for line in lines:
        columns = line.split("\t")
        dict_entries = columns[4].split(",")
        for entry in dict_entries:
            key, value = entry.split(":")
            value = int(value)
            if key in key_min_max:
                current_min, current_max = key_min_max[key]
                key_min_max[key] = (min(current_min, value), max(current_max, value))
            else:
                key_min_max[key] = (value, value)

    result = [(key, min_max[0], min_max[1]) for key, min_max in key_min_max.items()]
    result.sort()

    return result
