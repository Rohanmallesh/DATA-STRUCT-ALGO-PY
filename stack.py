class element:
    def __init__(self , data):
        self.data = data
        self.down = None
stack_size = 0
class stack:
    def __init__(self):
        self.top = None

    def push(self,new_data):
        if(self.top == None):
            element(new_data)
        new_element = element(new_data)
        new_element.down = self.top
        self.top = new_element

    def pop(self ):
        temp = self.top
        if(temp == None):
            print('STACK underflow.........')
        temp.data == None
        self.top = self.top.down

    def printstack(self):
        print(' ')
        print('STACK FOLLOWED BY..... ')
        print(' ')
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.down

if __name__ == '__main__':
    stk = stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.printstack()
    stk.pop()
    # stk.pop()
    stk.printstack()

    