#A Program to compare two list and get the intersection
#First we create the lists
L1 = []
L2 = []
L3 = []
#Take user input about length of list and elements

#def list(): # <= this is a fucntion 
a = int(input(" Please Enter how many numbers you want in first list:  "))
for i in range(a):
    L1.insert(i,int(input("Enter  number "+ str(i+1) + " of the list ")))

b = int(input(" Please Enter how many numbers you want in second list:  "))  
for i in range(b):
    L2.insert(i,int(input("Enter  number "+ str(i+1) + " of the list ")))
#getting the length of the list
c = len(L1)
d = len(L2)

#def intersect(): # < = even this is a function 
#Here we compare two list and get the common element in list 3
k = 0
i = 0
j = 0
for i in range(c):
    x = L1[i]
    for j in range(d):
        y = L2[j]
        if x == y:
            L3.insert(k,x)
            k = k + 1
print (" List one " + str(L1))
print (" List two " + str(L2))
print (" List of intersection " + str(L3))
