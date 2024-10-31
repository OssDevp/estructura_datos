class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def push(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            print("Indice fuera de rango")

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            print("Indice fuera de rango")
            return None

    def length(self):
        return self.size

    def show(self):
        print(self.data)


mi_array = Array(5)
mi_array.push(0, 5)
mi_array.push(1, 2)
mi_array.push(2, 4)
mi_array.push(3, 7)
mi_array.push(4, 9)

print(mi_array.show())
