
class Node:
    def __init__(self,data) :
        self.data = data
        self.next = None

class linllist:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == '__main__':
    link = linllist()
    link.head = Node(1)
    link.head.next = Node(2)
    link.printlist()