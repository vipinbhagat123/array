# remove duplicates

def k(n):
    l=[]
    for i in n:
        if i not in l:
            l.append(i)
    return l
        
    return n

n=[1, 2, 2, 3, 4, 3, 5]
print(k(n))