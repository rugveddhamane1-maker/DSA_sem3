class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def create_tree(self):
        value = int(input("Enter node value (-1 for None): "))

        if value == -1:
            return None

        new_node = Node(value)
        print("Enter Left Child of", value)
        new_node.left = self.create_tree()
        print("Enter Right Child of", value)
        new_node.right = self.create_tree()
        return new_node

    def print_preorder(self, node):
        if node is None:
            return
        print(node.val, end=" ")
        self.print_preorder(node.left)
        self.print_preorder(node.right)

    def print_inorder(self, node):
        if node is None:
            return
        self.print_inorder(node.left)
        print(node.val, end=" ")
        self.print_inorder(node.right)

    def print_postorder(self, node):
        if node is None:
            return
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print(node.val, end=" ")


tree = Tree()
root = tree.create_tree()

print("Preorder: ", end="")
tree.print_preorder(root)
print()

print("Inorder: ", end="")
tree.print_inorder(root)
print()

print("Postorder: ", end="")
tree.print_postorder(root)
print()