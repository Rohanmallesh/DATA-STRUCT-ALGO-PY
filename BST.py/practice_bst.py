

class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        
def insert(root,data):
    if root is None:
        return node(data)
    else:
        if root.data ==data:
            return root
        if root.data <data:
            root.right= insert(root.right ,data)
        elif root.data >data:
            root.left = insert(root.left , data)
    return root

def preorder(root):
    if root:
        print(root.data , end=" ")
        preorder(root.left)
        preorder(root.right)
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data , end=" ")
        inorder(root.right)
        
def minvalue(root):
    if root is None:
        return root
    while root:
        if root.left == None:
            return root.data
        root = root.left
def search(root,data):
    if root is None:
        return root 
    else:
        if root.data == data:
            return root
        elif root.data <data:
            return search(root.right , data)
        else:
            return search(root.left , data)
        
def deletenode(root,key):
    if root is None:
        return root
    if root.data <key:
        root.right = deletenode(root.right , key )
    elif root.data >key:
        root.left = deletenode(root.left , key)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp
        if root.left is None:
            temp = root.right
            root = None
            return temp
        
        temp = minvalue(temp.right , temp)
        root.data = temp.data
        root.right = deletenode(root.right , temp.data)
    return root
        
            
if __name__ == "__main__":
    root = node(8)
    insert(root,7)
    preorder(root)
    print("\n")
    inorder(root)
    t =minvalue(root)
    print(t)
    
    deletenode(root,7)
    preorder(root)
    
    