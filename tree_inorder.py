#this program is to implement tree traversal technique called inorder traversal

class node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

def printinorder(root):
    #   print('INORDER TRAVERSAL AS FOLLOWS:-')
      if root:
          printinorder(root.left)
          print(root.data, end="")
          printinorder(root.right)

def printpostorder(root):
        # print('POSTORDER TRAVERSAL AS FOLLOWS:-')
        if root:
            printpostorder(root.left)
            printpostorder(root.right)
            print(root.data , end="")

def printpreorder(root):
        # print('PREORDER TRAVERSAL AS FOLLOWS:-')

        if root:
            print(root.data,end="")
            printpreorder(root.left)
            printpreorder(root.right)    

class tree:
    def __init__(self) :
        self.root = None


   
tf = node(6)
print(tf.data)

if __name__ == '__main__':
    root = node(1)
    root.left = node(2)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(5)

    print('inorder traversal is as follows : ')

    printpreorder(root)

