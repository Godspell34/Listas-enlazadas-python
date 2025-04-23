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

    # Insertar un nuevo valor al inicio de la lista
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

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

    # Método que cuenta la cantidad de nodos en la lista
    def cantidadNodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Método que suma los valores enteros de la lista
    def sumaValores(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

    # Método que imprime el primer valor de la lista
    def primerValor(self):
        if self.cabeza:
            print("El primer valor de la lista es:", self.cabeza.valor)
        else:
            print("La lista está vacía")

# Esta línea asegura que el siguiente bloque solo se ejecuta si el archivo se corre directamente, y no cuando es importado como módulo en otro archivo
if __name__ == "__main__":
    lista = ListaEnlazada()  # Creando el objeto lista

    # Leer datos desde la entrada
    while True:
        valor = input("Ingrese un número para insertar en la lista (o 'salir' para terminar): ")
        if valor.lower() == 'salir':
            break
        lista.insertar(int(valor))  # Inserta al final

    # Imprimir la lista
    lista.imprimir() 

    # Imprimir la cantidad de nodos
    print("Cantidad de nodos en la lista:", lista.cantidadNodos())

    # Imprimir la suma de los valores
    print("Suma de los valores en la lista:", lista.sumaValores())

    # Imprimir el primer valor de la lista
    lista.primerValor()

    # Ejemplo de inserción al inicio
    lista.insertar_inicio(0)
    print("Después de insertar 0 al inicio:")
    lista.imprimir()  # Imprime la lista después de la inserción al inicio
