# reverse a list

def k(n):
    l=[]
    while n:
        l.append(n.pop())
    return l
n=[10,20,3,40,50,6]
print(k(n))