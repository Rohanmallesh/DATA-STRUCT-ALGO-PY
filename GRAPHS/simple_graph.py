class Adjnode:
    def __init__(self,vertex):
        self.vertex = vertex
        self.next = None
        
class graph:
    def __init__(self,vertex):
        self.v = vertex
        self.graph = [None]*self.v
        
    def add_node(self,src,dest):
        new_node = Adjnode(dest)
        new_node.next = self.graph[src]
        self.graph[src ]= new_node
        
        new_node = Adjnode(src)
        new_node.next = self.graph[dest]
        self.graph[dest] = new_node
        
    def print_graph(self):
        for i in range(self.V):
            print(f"Adjacency list of vertex {i}\n head", end="")
            temp = self.graph[i]
            while temp:
                print(temp.vertex, end="")
                temp = temp.next
        
    
if __name__ == "__main__":
    g = graph(1)
    g.add_node()
