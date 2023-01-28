class element:
    def __init__(self, data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.front = None
        self.end = None

    def enque(self, new_data):
        new_element = element(new_data)
        if self.end == None:
            self.front = new_element
            self.end = new_element
        else:
            self.end.next = new_element
            self.end = new_element

    def isempty(self):
        self.front = None

    def deque(self):
        if self.front == None :
            print('Nothing left in queue')
        else:
            self.front.data = None
            self.front = self.front.next 

    def printqueue(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next


    
if __name__ == '__main__':
    que = queue()
    que.enque(1)
    que.enque(2)
    que.enque(3)
    que.printqueue()
    print('DEQUED THE FIRST ELEMENT')
    que.deque()
    que.printqueue()
    que.deque()
    que.deque()
    que.deque()
