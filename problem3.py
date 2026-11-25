
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root

        while True:
            if key < current.data:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left

            elif key > current.data:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

            else:
                return  


    def search(self, key):
        current = self.root

        while current is not None:
            if key == current.data:
                return True

            elif key < current.data:
                current = current.left

            else:
                current = current.right

        return False


    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current


    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return None

        if key < root.data:
            root.left = self._delete(root.left, key)

        elif key > root.data:
            root.right = self._delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            successor = self.min_value_node(root.right)
            root.data = successor.data
            root.right = self._delete(
                root.right, successor.data
            )

        return root


    def inorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            result.append(node.data)
            traverse(node.right)

        traverse(self.root)
        return result



if __name__ == "__main__":

    bst = BST()

    for key in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        bst.insert(key)

    print(bst.inorder())       
    print(bst.search(35))      
    print(bst.search(99))      

    bst.delete(20)             
    bst.delete(40)             

    print(bst.inorder())       
