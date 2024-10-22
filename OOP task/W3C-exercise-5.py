class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.node_insert(self.root, value)

    def node_insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.node_insert(node.left, value)
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.node_insert(node.right, value)

    def search(self, value):
        return self.node_search(self.root, value)

    def node_search(self, node, value):
        if node is None:
            return False
        elif value < node.value:
            return self.node_search(node.left, value)
        elif value > node.value:
            return self.node_search(node.right, value)
    def tree_print(self):
        return self.node_print(self.root)

    def node_print(self, node):
        if node is None:
            return
        else:
            print(node.value)
            self.node_print(node.left)
            self.node_print(node.right)



#main

bst = BinaryTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)

bst.tree_print()
