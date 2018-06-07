L1 = [1,2,3,]
L2 = [3,4,5]
L3 = [0,0,0]
for i in range(3):
    x = L1[i]
    for j in range(3):
        y = L2[j]
        if x == y:
            L3[i] = x
           # return L3[i]


print (L3)