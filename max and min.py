# find max and min

def k(n):
    max_va=n[0]
    min_va=n[0]
    for i in n:
        if i>max_va:
            max_va=i
        if i<min_va:
            min_va=i
    return max_va,min_va
n=[10,20,30,40,50,6]
print(k(n))