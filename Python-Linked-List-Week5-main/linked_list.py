"""
+=========================================== +
| AUTOR: ALEX DIAZ y SSLER FLORES            |
| FECHA: 23-04-2025                          |
| DESCRIPCIÓN: Modificación de la lista      |
| enlazada para incluir varios metodos       |
| y funcionalidades.                         |
| VERSION: 1.0                               |
+=========================================== +
"""
#Ejemplificando la creación de una lista enlazada simple

# Clase Nodo - representa un nodo de la lista
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - gestiona la lista y sus operaciones
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Insertar un nuevo valor al final de la lista
    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Eliminar el primer nodo que contenga el valor
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True  # Valor eliminado
            anterior = actual
            actual = actual.siguiente

        return False  # Valor no encontrado

    # Método para buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Método que imprime los valores de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def cantidad_nodos(self):
        contador = 0
        actual = self.cabeza
        # mientras actual no sea None, se cuenta en la lista
        while actual:
            contador += 1
            actual = actual.siguiente
        print(f"Cantidad de Nodos: {contador}")
        return contador
    # insertar al inicio
    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor=valor)
        nuevo_nodo.siguiente = self.cabeza 
        self.cabeza = nuevo_nodo # el puntero se cambia hacia la cabeza actual, y luego se cambia la cabecera al nuevo nodo. 

    def sumar_valores_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        print(f"Suma de valores: {suma}")
        return suma
    
    def primer_valor(self):
        return self.cabeza.valor if self.cabeza else None
    
if __name__ == "__main__":
    lista = ListaEnlazada()  #Creando el objeto lista

    # Pedir al usuario que inserte valor para llenar la lista
    while True:
        try:
            valor = int(input("Ingrese un número entero positivo (-1 para salir): "))
            if valor == -1:
                break
            if valor < 0:
                print("Por favor, ingrese un número entero positivo.")
                continue
            # Insertar el valor en la lista
            lista.insertar(valor)
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    
"""
Modifica el programa para que realice:

Leer los datos que se insertarán en la lista.
Implementar inserción al inicio.
Agregar método cantidadNodos() que cuente los nodos de la lista.
Método que sume los valores enteros de la lista.
Agregar método que imprima el primer valor de la lista.

Investiga: Listas doblemente enlazadas
Proporciona un ejemplo
"""