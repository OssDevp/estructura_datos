class Stack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def push(self, value):
        if self.top < self.capacity - 1:
            self.top += 1
            self.data[self.top] = value
        else:
            print("El stack esta lleno")

    def pop(self):
        if self.top >= 0:
            value = self.data[self.top]
            self.data[self.top] = None
            self.top = self.top - 1
            return value
        else:
            print("No hay elementos en el stack")

    def peek(self):
        if not self.is_empty():
            return self.data[self.top]
        else:
            return None

    def is_empty(self):
        return self.top == -1

    def show(self):
        print(self.data[:self.top + 1])


pila = Stack(3)
pila.push(5)
pila.push(10)
pila.push(15)
print("Mostrar todos los elementos del Stack:")
pila.show()
print("Mostrar el ultimo elemento:")
print(pila.peek())
print("Elimina y recupera el ultimo elemento del Stack")
valor = pila.pop()
print(valor)
print("Mostrar como queda el Stack")
pila.show()
print("Mostrar el ultimo elemento:")
print(pila.peek())
