'''
    LinkesList de con un solo enlace
    EXPLICACION
    Node        ->  Son los nodos que se utilizan para crear las listas
                    ⤷ se crea "value" y el puntero "next" que apunta al sgte nodo
    self.head   ->  Es la Cabeza de la lista y el Nodo Principal
    FUNCIONA:
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║                                                          ║
    ║    sel.head -> Node(1) -> Node(2) -> Node(3) -> None     ║
    ║                ⤷ next(N2) ⤷ next(N3) ⤷ next(None)        ║
    ║                                                          ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def delete(self, value):
        if not self.head:
            print("La lista está vacía")
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            print("Valor no encontrado en la lista")

    def find(self, value):
        current = self.head
        while current.next:
            if current.value == value:
                return True
                break
            current = current.next
        return False

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        print("Lista Enlazada:", elements)


llist = LinkedList()
llist.append("Osvaldo")
llist.append("Tatiana")
llist.append("Paula")
print(llist.find("Tatiana"))
llist.delete("Tatiana")
print(llist.find("Tatiana"))
llist.display()
