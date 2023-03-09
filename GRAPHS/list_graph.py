class node:
    def __init__(self,vertex):
        self.vertex = vertex
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def insert(self,vertex):
        new_node = node(vertex)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                # if temp.next == None:
                temp = temp.next
            temp.next = new_node
                
    def traverse_list(self):
        temp = self.head
        while temp:
            print(temp.vertex,end="-->")
            temp = temp.next
            
class graph:
    """
    insert edge in terms of tuple -->(a,b)
    """
    def __init__(self,no_verteces,directed = True):
        self.no_verteces = no_verteces
        self.vertex_list = [linkedlist() for i in range(0,no_verteces)]
        self.directed = directed
        
    def insert_edge(self,edge):
        v1,v2 = edge
        if (v1 >= 0 and v1 <self.no_verteces) and (v2 >=0 and v2<self.no_verteces):
            self.vertex_list[v1].insert(v2)
            if not self.directed:
                self.vertex_list[v2].insert(v1)
        else:
            raise ValueError('invalid vertices please check!...')  
        
    def display_graph(self):
        for i in range(0,self.no_verteces):
            print(i, end='\t')
            self.vertex_list[i].traverse_list()
            print('None')
            
# if __name__ == '__main__':
n = 5 #number of vertices
graph1 = graph(n, directed=False) #create an undirected graph
graph1.insert_edge((0, 3)) 
graph1.insert_edge((1, 3)) 
graph1.insert_edge((1, 2)) 
graph1.insert_edge((2, 4)) 
graph1.insert_edge((3, 4)) 
graph1.display_graph()
    
    
        