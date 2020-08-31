class Node:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def walk(self, code, way):
        self.left.walk(code, way + '0')
        self.right.walk(code, way + '1')


class Leaf:

    def __init__(self, char):
        self.char = char

    def walk(self, code, way):
        code[self.char] = way


a1 = Leaf('a')
a2 = Leaf('b')
a3 = Leaf('c')
a4 = Leaf('d')
a5 = Leaf('e')
n1 = Node(a1, a2)
n2 = Node(n1, )