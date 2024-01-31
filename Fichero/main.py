from datetime import datetime
from gestor_f import Gestor
from ordenamiento import quicksort_asc,quicksort_desc,mergesort_asc,merge_asc,mergesort_desc,merge_desc,shellsort,heapsort,dict_mayor_a_menor,dict_menor_a_mayor
from file_m import Archivo_d
gestor = Gestor()
def crear_u():
    while True:
        try:
            nombre = input("Nombre de la unidad: ")
            capacidad_t = int(input("Capacidad de memoria de la unidad: "))
            tipo_u = input("Tipo de unidad: ")
            gestor.nueva_u(nombre, capacidad_t, tipo_u)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def crear_c():
    while True:
        try:
            nombre = input("Nombre de la carpeta: ")
            id = input("Id de la unidad: ")
            gestor.nueva_c(id, nombre)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def crear_f():
    while True:
        try:
            nombre = input("Nombre del fichero: ")
            id = input("Id de la unidad: ")
            id_c = input("Id de la carpeta: ")
            tamano = int(input("Cuanto pesa el fichero: "))
            extension = input("Tipo de extension del fichero: ")
            contenido = input("Contenido almacenado del fichero: ")
            gestor.nuevo_f(id, id_c, tamano, nombre, extension, contenido)
            gestor.calculos(id, id_c)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def lista_c():
    while True:
        try:
            id = input("Id de la unidad: ")
            gestor.listar_c(id)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def lista_f():
    while True:
        try:
            id = input("Id de la unidad: ")
            id_c = input("Id de la carpeta: ")
            gestor.listar_f(id,id_c)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def borra_u():
    while True:
        try:
            id = input("Id de la unidad: ")
            gestor.borrar_u(id)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def borra_c():
    while True:
        try:
            id = input("Id de la unidad: ")
            id_c = input("Id de la carpeta a borrar: ")
            gestor.borrar_c(id,id_c)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def borra_c():
    while True:
        try:
            id = input("Id de la unidad: ")
            id_c = input("Id de la carpeta a borrar: ")
            gestor.borrar_c(id,id_c)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def borra_f():
    while True:
        try:
            id = input("Id de la unidad: ")
            id_c = input("Id de la carpeta: ")
            id_f = input("Id de la carpeta: ")
            gestor.borrar_f(id,id_c,id_f)
            return False
        except ValueError:
            print("Ocurrio algun error volver a intentar")

def main():
    print("----------Menu Principal----------")
    while True:
        try:
            print("1) Agregar unidad")
            print("2) Agregar carpeta")
            print("3) Agregar fichero")
            print("4) Listar unidad")
            print("5) Listar carpeta")
            print("6) Listar fichero")
            print("7) Borrar unidad")
            print("8) Borrar carpeta")
            print("9) Borrar fichero")
            print("10) algoritmos de ordenamiento")
            print("11) Salir")
            user = int(input(("/> ")))
            if user == 1:
                crear_u()
            elif user == 2:
                crear_c()
            elif user == 3:
                crear_f()
            elif user == 4:
                gestor.listar_u()
            elif user == 5:
                lista_c()
            elif user == 6:
                lista_f()
            elif user == 7:
                borra_u()
            elif user == 8:
                borra_c()
            elif user == 9:
                borra_f()
            elif user == 10:
                a_d = Archivo_d()
                data = a_d.lee_f()
                print("1) Quicksort")
                print("2) Mergesort")
                print("3) Shellsort")
                print("4) Heapsort")
                print("5) Ordenar por creacion")
                user_s = int(input(("/> ")))
                if user_s == 1:
                    id = input("Id de la unidad: ")
                    id_c = input("Id de la carpeta: ")
                    if len(data) == 0:
                        print("There's no users registered")
                    for i in data:
                        if i["id"]==id:
                            if len(i["lista_c"]) == 0:
                                print("La carpeta no tiene contenido")
                            else:
                                carpeta = i["lista_c"]
                    for i in data:
                        if i["id"]==id:
                            for j in i["lista_c"]:
                                if j["id"]==id_c:
                                    if len(j["lista_f"]) == 0:
                                        print("La carpeta no tiene ficheros")
                                    else:
                                        fichero = j["lista_f"]

                    print("1) ascendente")
                    print("2) descendente")
                    user_a = int(input("=> "))
                    if user_a == 1:
                        print("Carpetas")
                        carp_ord = quicksort_asc(carpeta, "tamano_t")
                        for i in carp_ord:
                            print(f"{i['nombre']} - {i['fecha_c']} - {i['tamano_t']}kb")
                        print("Ficheros")
                        fic_ord = quicksort_asc(fichero, "tamano_t")
                        for x in fic_ord:
                            print(f"{x['nombre']} - {x['fecha_c']} - {x['fecha_m']} - {x['extension']} - {x['contenido']}")
                    elif user_a == 2:
                        carp_ord = quicksort_desc(carpeta, "tamano_t")
                        for i in carp_ord:
                            print(f"{i['nombre']} - {i['fecha_c']} - {i['tamano_t']}kb")
                        fic_ord = quicksort_desc(fichero, "tamano")
                        for x in fic_ord:
                            print(f"{x['nombre']} - {x['fecha_c']} - {x['fecha_m']} - {x['extension']} - {x['contenido']}")
                elif user_s == 2:
                    id = input("Id de la unidad: ")
                    id_c = input("Id de la carpeta: ")
                    if len(data) == 0:
                        print("There's no users registered")
                    for i in data:
                        if i["id"]==id:
                            if len(i["lista_c"]) == 0:
                                print("La carpeta no tiene contenido")
                            else:
                                for j in i["lista_c"]:
                                    j["fecha_c"] = int(j["fecha_c"].replace("-", ""))
                                carpeta = i["lista_c"]
                    for i in data:
                        if i["id"]==id:
                            for j in i["lista_c"]:
                                if j["id"]==id_c:
                                    if len(j["lista_f"]) == 0:
                                        print("La carpeta no tiene ficheros")
                                    else:
                                        for x in j["lista_f"]:
                                            x["fecha_c"] = int(j["fecha_c"].replace("-", ""))
                                        fichero = j["lista_f"]

                    print("1) ascendente")
                    print("2) descendente")
                    user_a = int(input("=> "))
                    if user_a == 1:
                        print("Carpetas")
                        carp_ord = merge_asc(carpeta, "fecha_c")
                        for i in carp_ord:
                            print(f"{i['nombre']} - {i['fecha_c']} - {i['tamano_t']}kb")
                        print("Ficheros")
                        fic_ord = merge_asc(fichero, "fecha_c")
                        for x in fic_ord:
                            print(f"{x['nombre']} - {x['fecha_c']} - {x['fecha_m']} - {x['extension']} - {x['contenido']}")
                    elif user_a == 2:
                        carp_ord = merge_desc(carpeta, "tamano_t")
                        for i in carp_ord:
                            print(f"{i['nombre']} - {i['fecha_c']} - {i['tamano_t']}kb")
                        fic_ord = merge_desc(fichero, "fecha_c")
                        for x in fic_ord:
                            print(f"{x['nombre']} - {x['fecha_c']} - {x['fecha_m']} - {x['extension']} - {x['contenido']}")

                elif user_s == 3:
                    id = input("Id de la unidad: ")
                    id_c = input("Id de la carpeta: ")
                    if len(data) == 0:
                        print("There's no users registered")
                    for i in data:
                        if i["id"]==id:
                            if len(i["lista_c"]) == 0:
                                print("La carpeta no tiene contenido")
                            else:
                                carpeta = i["lista_c"]
                    for i in data:
                        if i["id"]==id:
                            for j in i["lista_c"]:
                                if j["id"]==id_c:
                                    if len(j["lista_f"]) == 0:
                                        print("La carpeta no tiene ficheros")
                                    else:
                                        fichero = j["lista_f"]
                    print("Carpeta")
                    shellsort(carpeta,"tamano_t")
                    inicio_r = int(input("Ingrese el índice de inicio del rango: "))
                    final_r = int(input("Ingrese el índice de fin del rango: "))
                    carp_ord = [elem for elem in carpeta if inicio_r <= elem["tamano_t"] <= final_r]
                    for i in carp_ord:
                            print(f"{i['nombre']} - {i['fecha_c']} - {i['tamano_t']}kb")
                    print("Fichero")
                    shellsort(fichero,"tamano")
                    inicio_r = int(input("Ingrese el índice de inicio del rango: "))
                    final_r = int(input("Ingrese el índice de fin del rango: "))
                    fic_ord = [elem for elem in fichero if inicio_r <= elem["tamano"] <= final_r]
                    for i in fic_ord:
                            print(f"{i['nombre']} - {i['fecha_c']} - {i['fecha_m']} - {i['extension']} - {i['contenido']}")
                elif user_s == 4:
                    id = input("Id de la unidad: ")
                    id_c = input("Id de la carpeta: ")
                    if len(data) == 0:
                        print("There's no users registered")
                    for i in data:
                        if i["id"]==id:
                            if len(i["lista_c"]) == 0:
                                print("La carpeta no tiene contenido")
                            else:
                                carpeta = i["lista_c"]
                    for i in data:
                        if i["id"]==id:
                            for j in i["lista_c"]:
                                if j["id"]==id_c:
                                    if len(j["lista_f"]) == 0:
                                        print("La carpeta no tiene ficheros")
                                    else:
                                        fichero = j["lista_f"]
                    print("Carpeta")
                    inicio_r = int(input("Ingrese el índice de inicio del rango: "))
                    final_r = int(input("Ingrese el índice de fin del rango: "))
                    carp_r = [elem for elem in carpeta if inicio_r <= elem["tamano_t"] <= final_r]
                    heapsort(carp_r, "tamano_t", 0, len(carp_r))
                    for i in carp_r:
                        print(f"{i['nombre']} - {i['fecha_c']} - {i['tamano_t']}kb")
                    print("Fichero")
                    inicio_r = int(input("Ingrese el índice de inicio del rango: "))
                    final_r = int(input("Ingrese el índice de fin del rango: "))
                    fic_r = [elem for elem in fichero if inicio_r <= elem["tamano"] <= final_r]
                    heapsort(carp_r, "tamano", 0, len(carp_r))
                    for i in fic_r:
                        for i in fic_ord:
                            print(f"{i['nombre']} - {i['fecha_c']} - {i['fecha_m']} - {i['extension']} - {i['contenido']}")
                elif user_s == 5:
                    id = input("Id de la unidad: ")
                    id_c = input("Id de la carpeta: ")
                    if len(data) == 0:
                        print("There's no users registered")
                    for i in data:
                        if i["id"]==id:
                            if len(i["lista_c"]) == 0:
                                print("La carpeta no tiene contenido")
                            else:
                                for j in i["lista_c"]:
                                    j["fecha_c"] = int(j["fecha_c"].replace("-", ""))
                                carpeta = i["lista_c"]
                    for i in data:
                        if i["id"]==id:
                            for j in i["lista_c"]:
                                if j["id"]==id_c:
                                    if len(j["lista_f"]) == 0:
                                        print("La carpeta no tiene ficheros")
                                    else:
                                        for x in j["lista_f"]:
                                            x["fecha_c"] = int(j["fecha_c"].replace("-", ""))
                                        fichero = j["lista_f"]
                    
                    carp_ord = dict_mayor_a_menor(carpeta,"fecha_c")
                    for i in carp_ord:
                        print(f"{i['nombre']} - {i['fecha_c']} - {i['tamano_t']}kb")
                    print("Ficheros")
                    fic_ord = dict_mayor_a_menor(fichero,"fecha_c")
                    for i in carp_ord:
                        print(f"{i['nombre']} - {i['fecha_c']} - {i['fecha_m']} - {i['extension']} - {i['contenido']}")
            elif user == 11:
                print("Programa Finalizado Correctamente")
                break
        except ValueError:
            print("Ocurrio algun error volver a intentar")

main()