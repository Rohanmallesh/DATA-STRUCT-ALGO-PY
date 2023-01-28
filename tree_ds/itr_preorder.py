# python program to implement level order 
# traversal with iterative manner

class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def iterative_levelorder(root):
    nodestack = []
    nodestack.append(root)
    while(len(nodestack)>0):
        node = nodestack.pop()
        print(node.data, end="")
        if node.right is not None:
            nodestack.append(node.right)
        if node.left is not None:
            nodestack.append(node.left)

if __name__ == "__main__":
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)
    # iterative_levelorder(root)
    # root = node(10)
    # root.left = node(20)
    # root.right = node(30)
    # root.left.left = node(40)
    # root.left.left.left = node(70)
    # root.left.right = node(50)
    # root.right.left = node(60)
    # root.left.left.right = node(80)
    iterative_levelorder(root)