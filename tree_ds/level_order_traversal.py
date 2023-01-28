# level order traversal of tree

class node:
    def __init__(self,data):
        self.data  = data
        self.left = None
        self.right = None

def levelorder(root):
    h = height(root)
    for i in range(1,h+1):
        printcurrentnode(root,i)

def printcurrentnode(root,level):
    if root is None:
        return 
    if level ==1:
        print(root.data,end="")
    elif(level >1):
        printcurrentnode(root.left, level-1)
        printcurrentnode(root.right, level-1)


def height(root):
    if root is None:
        return 0

    else:
        lh = height(root.left)
        rh= height(root.right)
        if lh>rh:
            return lh+1
        else:
            return rh+1


if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)

h = height(root)
print(f'the height of tree is {h}')

print('THE level order travered tree is :')
levelorder(root)