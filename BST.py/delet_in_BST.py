class node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def preorder(root):
    if root:
        print(root.data , end=" ")
        preorder(root.left)
        preorder(root.right)
    
def insert(root,key):
    new_node = node(key)
    if root is None:
        return new_node
    else:
        if root.data == key:
            return root
        elif root.data <key:
            root.right = insert(root.right , key)
        else:
            root.left = insert(root.left , key)
    return root

def search(root,key):
    if root is None:
        print("element not exist")
        return root
    else:
        if root.data == key:
            print("element exist")
            return root
        elif root.data < key:
            return search(root.right , key)
        else:
            return search(root.left , key)

def minvalue(root):
    if root is None:
        return root
    else:
        while root:
            if root.left is None:
                return root
            root = root.left

def maxvalue(root):
    if root is None:
        return root
    else:
        while root:
            if root.right is None:
                return root
            root = root.right

def inorder_preceder(root, inroot):
    pass

def inorder_succesor(root, inroot):
    pass

def deletenode(root ,key):
    if root is None:
        return root
    if root.data <key:
        root.right = deletenode(root.right , key)
    elif root.data >key:
        root.left = deletenode(root.left , key)
    else:
        if root.right is None:
            temp = root.left
            root = None
            return temp
        
        elif root.left is None:
            temp = root.right 
            root = None
            return temp
        
        temp = minvalue(root.right)
        root.data = temp.data       
        root.right = deletenode(root.right, temp.data)
 
    return root
            
            

if __name__ == "__main__":
    root = node(8)
    insert(root, 10)
    insert(root,3)
    insert(root, 6)
    insert(root,1)
    insert(root, 14)
    insert(root,13)
    insert(root,4)
    insert(root,7)
    preorder(root)
    print('\n SEARCHED ELEMENT:-')
    search(root,6)
    # print(T.data)
    print('\n SMALL ELEMENT IN THE TREE IS :-')
    t =minvalue(root)
    print(t.data)

    preorder(root)

    print('\n The maximum value in the tree is :-')
    k=maxvalue(root)
    print(k.data)
    
    deletenode(root,10)
    preorder(root)
