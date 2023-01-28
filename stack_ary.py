import array

stk = array.array('i',[])
top = stk[0]

def push(data):
     t= stk.append(data)
     top = stk[t]

def pop():
    top = stk[-1-1]

print(stk)
push(1)
print(stk)

