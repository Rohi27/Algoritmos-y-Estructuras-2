class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class Pila:
    def __init__(self):
        self.cabeza = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo

    def desapilar(self):
        if self.cabeza is None:
            return None

        nodo_desapilado = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return nodo_desapilado.valor

    def esta_vacia(self):
        return self.cabeza is None


class Cola:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def desencolar(self):
        if self.cabeza is None:
            return None

        nodo_desencolado = self.cabeza
        self.cabeza = self.cabeza.siguiente

        if self.cabeza is None:
            self.cola = None

        return nodo_desencolado.valor

    def esta_vacia(self):
        return self.cabeza is None


def main():
    lista = [1, 2, 3, 4, 5]
    
    # Convertir lista enlazada en una pila
    pila = Pila()
    for elemento in lista:
        pila.apilar(elemento)

    # Desapilar elementos de la pila
    print("Pila:")
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        print(elemento)

    # Convertir lista enlazada en una cola
    cola = Cola()
    for elemento in lista:
        cola.encolar(elemento)

    # Desencolar elementos de la cola
    print("Cola:")
    while not cola.esta_vacia():
        elemento = cola.desencolar()
        print(elemento)


if __name__ == "__main__":
    main()
