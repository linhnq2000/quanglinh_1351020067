a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 88]
b = [1, 3, 5, 4, 7, 88, 66, 59, 40, 54]
c=[]
for i in max(a,b):
    if i in min(a, b) and i not in c:
            c.append(i) 
    print(c)