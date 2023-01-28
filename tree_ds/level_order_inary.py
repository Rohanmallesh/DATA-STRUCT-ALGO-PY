
a=[None]*10

def root(key):
    if a[0] is not None:
        print('Root already exist')
    else:
        a[0] = key

def toleft(key,parent):
    if a[parent] == None:
        print('parent not exist')
    else:
        a[(parent*2)+1] = key

def toright(key,parent):
    if a[parent] == None:
        print('parent is not available')
    else:
        a[(parent*2)+2] = key

def height(a):
    n = -1
    c=0
    for i in range(-1):
        c += 1
        if a[i] != None:
            break

    return 10-c     
            


def printtree():
    for i in a:
        if i != None:
            print(i,end="")
        else:
            print("_", end="")

rot = root(1)
toleft(2,0)
toright(3,0)
toleft(4,2)
toright(5,2)

printtree()
print('HEIGHT IS :')
h = height(a)
print(h)
