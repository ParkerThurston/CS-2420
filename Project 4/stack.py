'Creates the stack'
class Node:
    'creates the node in the stack'
    def __init__(self,data):
        self.value = data
        self.next = None
class Stack:
    'Takes the nodes and puts them in stack'
    def __init__(self):
        self.head = Node("head")
        self.size1 = 0

    def push(self, item):
        'puts new node on top of stack'
        node = Node(item)
        node.next = self.head.next
        self.head.next = node
        self.size1 += 1

    def pop(self):
        'pops off top node from stack'
        if self.size1 == 0:
            raise IndexError("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size1 -= 1
        return remove.value

    def top(self):
        'takes a peek at the top node'
        if self.size1 == 0:
            raise IndexError("Popping from an empty stack")
        return self.head.next.value

    def size(self):
        'returns the size of the stack'
        return self.size1

    def clear(self):
        'clears the stack of all nodes'
        if self.size1 > 0:
            self.pop()
