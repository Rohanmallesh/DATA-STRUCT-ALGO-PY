
class node:
    def __init__(self,data):
        self.data = data
        self.below = None

class stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = node(data)
        if self.top == None:
            self.top = new_node
        else:
            new_node.below = self.top
            self.top = new_node

    def pop(self):
        self.top = self.top.below

    def printstack(self):
        temp = self.top
        while temp: 
            print(temp.data)
            temp = temp.below

if __name__ == '__main__':
    stk = stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    stk.printstack()
    print('top elememnt .....')
    print(stk.top.data)
    print(' Poped successfully')
    stk.pop()
    stk.printstack()

