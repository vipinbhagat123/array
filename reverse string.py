# reverse a list

def k(n):
    l=''
    for i in n:
        l=i+l
    return l
n='abcde'
print(k(n))