class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
                
    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
if __name__ == '__main__':
    llist = linklist()
    llist.insert(1)
    llist.insert(2)
    l = [3,4,5,6,7,8,9]
    for i in l:
        llist.insert(i)
    llist.printlist()