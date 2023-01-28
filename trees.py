# binary tree using array
# import numpy as np

tree = [None]*10

def root(key):
    if tree[0] != None:
        print('the tree already has root')
    else:
        tree[0] = key

def toleft(data,parent):
    if tree[parent] == None:
        print('cant assign child coz no parent for position', (parent *2)+1)
    else:
        tree[(parent*2)+1] = data

def toright(data , parent):
    if tree[parent] == None:
        print('no parent is found so cant set child at position ', (parent *2)+2)
    else:
        tree[(parent*2)+2] = data

def printtree():
    for i in tree:
        if i != None:
            print(i , end="")
        else:
            print('_',end="")

root('a')
toright('c',0)
toleft('b',0)
toleft('d',1)
toright('e',1)
toright('f',2)
printtree()