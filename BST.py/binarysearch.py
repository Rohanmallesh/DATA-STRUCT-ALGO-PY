class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def search(root, key):
    if root is None:
        return root
    elif root.data == key:
        return root
    elif root.data <key:
        return search(root.right , key)
    else:
        return search(root.left , key)

def insert(root,key):
    nod = node(key)
    if root is None:
        return nod
    elif root.data == key:
        return root
    elif root.data <key :
        root.right = insert(root.right , key)
    else:
        root.left = insert(root.left , key)
    return root

def preorder(root):
    if root:
        print(root.data , end=" ")
        preorder(root.left )
        preorder(root.right)

root = node(8)
insert(root,3)
insert(root,10)
insert(root,1)
insert(root,6)
insert(root,14)
insert(root,4)
insert(root,7)
insert(root,13)
insert(root,9)
preorder(root)
print("\n the searched element is :")
t=search(root,6)
print(t.data)
