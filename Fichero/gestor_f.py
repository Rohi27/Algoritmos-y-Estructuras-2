from file_m import Archivo_d as A_d  # Importa la clase Archivo_d del módulo file_m con el alias A_d
import uuid  # Importa el módulo uuid
from datetime import datetime  # Importa el módulo datetime
a_d = A_d()  # Crea una instancia de la clase Archivo_d llamada a_d

class Gestor():  # Define la clase Gestor
    def __init__(self) -> None:  # Define el método de inicialización de la clase
        self.data = []  # Crea un atributo llamado data que es una lista vacía

    def nueva_u(self, name, capacidad_t, tipo_u):  # Define el método nueva_u
       self.data = a_d.lee_f()  # Lee los datos del archivo JSON y los asigna a self.data
       id_u = str(uuid.uuid4())[:4]  # Genera un ID único de 4 caracteres utilizando el módulo uuid
       new_u = {  # Crea un diccionario con los datos de la nueva unidad
        "id": id_u,
        "nombre": name,
        "capacidad_t": capacidad_t,
        "tipo_u": tipo_u,
        "lista_c": [],
        "capacidad_d": 0
       }
       self.data.append(new_u)  # Agrega la nueva unidad a la lista de datos
       a_d.escribir_f(self.data)  # Escribe los datos actualizados en el archivo JSON
       print(f"Unidad {name} creada exitosamente")

    
    def nueva_c(self, id, nombre):
        self.data = a_d.lee_f()  # Lee los datos del archivo
        id_c = str(uuid.uuid4())[:4]  # Genera un identificador único para la carpeta
        new_c = {
        "id": id_c,
        "nombre": nombre,
        "fecha_c": str(datetime.now().date()),
        "tamano_t": None,
        "lista_f": []
        }
        for i in self.data:
            if i['id'] == id:
                i['lista_c'].append(new_c)  # Agrega la nueva carpeta al atributo "lista_c" de la unidad correspondiente
                a_d.escribir_f(self.data)  # Escribe los datos actualizados en el archivo
                break
            else:
                print(f"Unidad con id {id} no se encuentra")  # Imprime un mensaje de error si la unidad no se encuentra


    def nuevo_f(self,id,id_c,tamaño,nombre,extension,contenido):
        self.data = a_d.lee_f()
        id_f = str(uuid.uuid4())[:4]
        new_f ={"id":id_f,
                "nombre": nombre,
                "tamano": tamaño,
                "extension":extension,
                "fecha_c": str(datetime.now().date()),
                "fecha_m": str(datetime.now().date()),
                "contenido": contenido
                }
        for i in self.data:
            if i["id"]==id:
                    for j in i["lista_c"]:
                        if j["id"]==id_c:
                            j["lista_f"].append(new_f)
                            a_d.escribir_f(self.data)
                            break
            '''else:
                print(f"Carpeta con id {id} no se encuentra")'''
    
    def calculos(self,id,id_c):
        self.data = a_d.lee_f()
        res = 0
        res_2 = 0
        for i in self.data:
            if i["id"]==id:
                for j in i["lista_c"]:
                    if j["id"]==id_c:
                        for x in j["lista_f"]:
                            res += x['tamano']
                            j["tamano_t"] = res
                    res_2 +=j["tamano_t"]
                i["capacidad_d"] = i["capacidad_t"]- res_2
        a_d.escribir_f(self.data)

    def listar_u(self):
        self.data = a_d.lee_f()
        if len(self.data) == 0:
            print("There's no users registered")
        for i in self.data:
            print(f"id: {i['id']} | nombre: {i['nombre']} | capacidad total :{i['capacidad_t']}kb | capacidad disponible: {i['capacidad_d']}kb | tipo unidad: {i['tipo_u']}")

    def listar_c(self,id):
        self.data = a_d.lee_f()
        if len(self.data) == 0:
            print("There's no users registered")
        for i in self.data:
            if i["id"]==id:
                if len(i["lista_c"]) == 0:
                    print("La carpeta no tiene contenido")
                else:
                    for j in i["lista_c"]:
                        print(f"id: {j['id']} | nombre: {i['nombre']} | fecha creacion: {j['fecha_c']} | tamaño total: {j['tamano_t']}kb")
            '''else:
                print(f"Unidad con id {id} no se encuentra")'''

    def listar_f(self,id,id_c):
        self.data = a_d.lee_f()
        for i in self.data:
            if i["id"]==id:
                for j in i["lista_c"]:
                    if j["id"]==id_c:
                        if len(j["lista_f"]) == 0:
                            print("La carpeta no tiene ficheros")
                        else:
                            for x in j["lista_f"]:
                                print(f"id: {x['id']} | nombre: {x['nombre']} | fecha creacion: {x['fecha_c']} | fecha modificacion: {x['fecha_m']} | extension: {x['extension']} | contenido: {x['contenido']}")
                    '''else:
                        print(f"Unidad con id {id_c} no se encuentra")
            else:
                print(f"Unidad con id {id} no se encuentra")'''
    
    def borrar_u (self,id):
        self.data = a_d.lee_f()
        for i in self.data:
            if i["id"]==id:
                print(f"Unidad {i['tipo_u']} ha sido borrada exitosamente")
                self.data.remove(i)
            '''else:
                print(f"Unidad con id {id} no se encuentra")'''
        a_d.escribir_f(self.data)
    
    def borrar_c (self,id, id_c):
        self.data = a_d.lee_f()
        for i in self.data:
            if i["id"]==id:
                for j in i["lista_c"]:
                    if j["id"] == id_c:
                        i["capacidad_d"] += j["tamano_t"]
                        print(f"Carpeta {i['nombre']} ha sido borrada exitosamente")
                        i['lista_c'].remove(j)
        a_d.escribir_f(self.data)

    def borrar_f (self,id, id_c, id_f):
        self.data = a_d.lee_f()
        for i in self.data:
            if i["id"]==id:
                for j in i["lista_c"]:
                    if j["id"] == id_c:
                        for x in j['lista_f']:
                            if x["id"] == id_f:
                                j["tamano_t"] -= x["tamano"]
                                i["capacidad_d"] += x["tamano"]
                                print(f"Fichero con el nombre {x['nombre']} ha sido borrado exitosamente")
                                j['lista_f'].remove(x)
        a_d.escribir_f(self.data)