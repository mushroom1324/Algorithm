import sys
sys.setrecursionlimit(10000)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_inorder(self):
        if self.left is not None:
            self.left.print_inorder()
        if self.right is not None:
            self.right.print_inorder()
        if self.data:
            print(self.data)


root = Node(int(sys.stdin.readline()))
while True:
    try:
        temp = int(sys.stdin.readline())
        root.insert(temp)
    except:
        break

root.print_inorder()