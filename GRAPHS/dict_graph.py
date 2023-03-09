#  this python code to implement the graph data structure using dictionary
class graph:
    def __init__(self):
        self.dic = dict()
        
    def addvertex(self,v):
        self.dic[v] = []
    
    def addedge(self,v,directed = True):
        v1,v2 = v
        self.dic[v1]=v2
        if directed is False:
            self.dic[v2] = v1
        
    def printdict(self):
        print(self.dic)


if __name__ == '__main__':
    
    lis = ['a','b','c','d']
    grp = graph()
    for i in lis:
      grp.addvertex(i)
    grp.printdict()
    
    lis1 = [('a','b'),('b','c'),('d','a'),('a','c')]
    for i in lis1:
        grp.addedge(i,True)
    grp.printdict()