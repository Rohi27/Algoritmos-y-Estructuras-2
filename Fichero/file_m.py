import json  # Importa el módulo json
import os  # Importa el módulo os

class Archivo_d:  # Define la clase Archivo_d
    def __init__(self) -> None:  # Define el método de inicialización de la clase
        self.data = []  # Crea un atributo llamado data que es una lista vacía

    def lee_f(self):  # Define el método lee_f
        if not os.path.isfile('data.json'):  # Verifica si el archivo 'data.json' no existe
            with open('data.json', 'w') as f:  # Si el archivo no existe, se crea uno vacío
                json.dump([], f)  # Escribe una lista vacía en el archivo JSON

        with open('data.json', 'r') as f:  # Abre el archivo JSON en modo de lectura
            self.data = json.load(f)  # Carga los datos del archivo JSON en la lista self.data
        return self.data  # Devuelve los datos cargados del archivo

    def escribir_f(self, data):  # Define el método escribir_f
        with open('data.json', 'w') as f:  # Abre el archivo JSON en modo de escritura
            json.dump(data, f)  # Escribe los datos proporcionados en el argumento data en el archivo JSON