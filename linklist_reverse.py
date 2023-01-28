class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = node(data)
        temp = self.head
        if self.head == None:
            self.head = new_node
        
        while(temp):
            if temp.next == None:
                temp.next = new_node
                break
            temp = temp.next

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data , end=" ")
            temp = temp.next

    def reverselist(self):
        h = self.head
        if h is None or h.next is None:
            return h
        p = llist.reverselist(h.next)
        h.next.next = h
        h.next = None
        return p
       



if __name__ == "__main__":
    llist = linklist()
    llist.insert(1)
    llist.insert(2)
    llist.insert(3)
    llist.insert(4)
    llist.insert(5)
    llist.insert(6)
    llist.printlist()
    llist.reverselist()