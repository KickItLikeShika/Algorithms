class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    # Exercise
    def inorder_tree_walk(self, root):
        if root:
            self.inorder_tree_walk(root.left)
            print(root.data)
            self.inorder_tree_walk(root.right)


if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    root.inorder_tree_walk(root)
