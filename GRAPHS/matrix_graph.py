# this program to implement the graph using matrix representation
import numpy as np
class graph:
   def __init__(self,n,bool):
      self.mat = np.zeros((n,n))
      self.directed = bool
      
   def insert_edge(self,v):
      v1 , v2 = v
      self.mat[v1,v2] = 1
      if self.directed is False:
         self.mat[v2,v1] = 1
      else:
         raise 'Invalid verteces!....'
         
   def printgraph(self):
      print(self.mat)
         

if __name__ == '__main__':
   n = int(input('Enter the number of vertices: '))
   grp = graph(n,False)
   lis = [(1,2),(4,3),(2,0)]
   # grp.insert_edge((1,2))
   for i in lis:
      grp.insert_edge(i)
   grp.printgraph()
   