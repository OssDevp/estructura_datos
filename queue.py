
#  Cola basado en Nodos donde se relacionan atravez de punteros

class Nodes:
    def __init__(self):
        self.info = None
        self.next = None


class Queue:
    def __init__(self):
        self.first_node = None
        self.last_node = None
        self.size = 0

    def enqueue(self, value):
        nodes = Nodes()
        nodes.info = value
        nodes.next = None

        if self.last_node is None:
            self.first_node = nodes
        else:
            self.last_node.next = nodes

        self.size += 1
        self.last_node = nodes

    def dequeue(self):
        if self.first_node is None:
            print("Queue vacio no se puede eliminar")
            return

        info = self.first_node.info
        self.first_node = self.first_node.next
        self.size -= 1

        if self.first_node is None:
            self.last_node = None

        return info

    def peek(self):
        return self.first_node.info

    def is_empty(self):
        return self.first_node is None

    def length(self):
        return self.size

    def show(self):
        copy = Queue()
        current = self.first_node
        while current:
            copy.enqueue(current.info)
            current = current.next

        current = copy.first_node
        while current:
            print(current.info)
            current = current.next


cola = Queue()
cola.enqueue("Osvaldo")
cola.enqueue("Tatiana")
cola.enqueue("Paula")
print(cola.peek())
print(cola.is_empty())
print(cola.length())
cola.show()
