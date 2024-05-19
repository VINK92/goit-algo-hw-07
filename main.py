class BSTNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.data:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)

    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.data

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def find_sum(self):
        if self.root is None:
            return 0
        return self._find_sum(self.root)

    def _find_sum(self, node):
        if node is None:
            return 0
        return self._find_sum(node.left) + node.data + self._find_sum(node.right)

bst = BST()
nodes = [10, 5, 15, 2, 7, 12, 20]

for node in nodes:
    bst.insert(node)

print("Найбільше значення у дереві:", bst.find_max())
print("Найменше значення у дереві:", bst.find_min())
print("Сума всіх значень у дереві:", bst.find_sum())
