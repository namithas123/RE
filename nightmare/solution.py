

def stack(inp,m):
    res = chr(inp-m)
    m=(m+1)%4
    return res,m

def rec(inp):
    i=0
    a=[]
    # int j = 0
    j=len(inp)-1
    while(i<len(inp)/2):
        a.append(inp[i])
        i+=1
        a.append(inp[j])
        j=j-1
    return ''.join(a[::-1])
def link(inp):
    w=[] 
    Z=[]
        # w=w[::-1]
    for i in range(14,len(inp)):
        w.append(inp[i])
    for i in range(0,14):
        w.append(inp[i])
    for i in range(0,14):
        Z.append(w[i])
    Z=Z[::-1]
    for i in range(14,len(inp)):
        Z.append(w[i])

    return ''.join(Z)

strin="20_a1qti0]n/5f642kb\\2`qq4\\0q"
value=(rec(link(strin)))
m=0
val=0
full=[]
for i in range(0,28):
    for k in range(33,127):
        op,m=stack(k,m)
        # print(op,value[i])
        if(op==value[i]):
            val=m 
            full.append(chr(k))
            # print(chr(k))
            break
        else:
            m=val
print("flag{"+''.join(full[::-1])+"}")


