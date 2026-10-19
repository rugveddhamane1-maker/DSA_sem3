from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a value
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert(current.left, data)

        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert(current.right, data)

        else:
            print(f"Duplicate value {data} ignored.")

    # Display original BST using in-order traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    # Display BST level-wise
    def level_order(self):
        if self.root is None:
            print("Tree is empty.")
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()
            print(current.data, end=" ")

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        print()

    # Calculate height
    def height(self, node):
        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    # Display leaf nodes
    def leaf_nodes(self, node):
        if node is None:
            return

        if node.left is None and node.right is None:
            print(node.data, end=" ")
            return

        self.leaf_nodes(node.left)
        self.leaf_nodes(node.right)


# Main program
bst = BinarySearchTree()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.insert(value)

print("Original BST (In-order traversal):")
bst.inorder(bst.root)

print("\n\nBST Level-wise:")
bst.level_order()

print("\nHeight of the BST:")
print(bst.height(bst.root))

print("\nLeaf Nodes:")
bst.leaf_nodes(bst.root)
print()