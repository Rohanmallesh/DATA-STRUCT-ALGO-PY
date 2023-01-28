class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.data , end=" ")
        preorder(root.left)
        preorder(root.right)

def search(root,key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.right , key)
    else :
        return search(root.left , key)

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif(root.data <key):
          root.right = insert(root.right , key )
        else:
          root.left = insert(root.left , key)
    return root


if __name__ == "__main__":
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right.left = Node(13)
    preorder(root)
    print("\nTHE SEARCHED ELEMENT IS ")
    t = search(root,6)
    print(t.data)
    insert(root,9)
    print("After insersion :-")
    preorder(root)