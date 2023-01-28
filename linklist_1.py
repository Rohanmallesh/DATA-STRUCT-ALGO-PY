class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class linkedlist:

    def __init__(self):
        self.head = None


    def front_insert(self ,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def after_insert(self ,prev_node, new_data):
        if(self.head == None):
            self.head =Node(new_data)
        temp = self.head
        while temp:
            if (temp.data == prev_node):
                new_node = Node(new_data)
                new_node.next = temp.next
                temp.next = new_node
                break
            temp = temp.next


    def end_insert(self , new_data):
        if(self.head == None):
            self.head = Node(new_data)
        temp = self.head
        while temp:
            if (temp.next == None):
                temp.next = Node(new_data)
                break
            temp = temp.next
        

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    link = linkedlist()
    link.head = Node(1)
    link.head.next = Node(2)
    link.front_insert(0)
    link.after_insert(2,3)
    link.end_insert(4)
    link.printlist()