"""
+=========================================== +
| AUTOR: ALEX DIAZ y SSLER FLORES            |
| FECHA: 23-04-2025                          |
| DESCRIPCIÓN: Listas doblemente enlazadas   |
| proporciona un ejemplo                     |
| VERSION: 1.0                               |
+=========================================== +
"""
# Clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None  # Apunta al nodo anterior

# Clase ListaDobleEnlazada
class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None  # Apunta al ultimo nodo de la lista

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:  # Si la lista esta vacia
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.anterior = self.cola  # set el nodo anterior
            self.cola.siguiente = nuevo  # set el siguiente del nodo anterior
            self.cola = nuevo  # cambia la cola de la lista