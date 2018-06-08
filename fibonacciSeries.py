#Now Let us start with the second program which is about Fibonacci series
#Except for the first two terms of the sequence, every other term is the sum of the previous two terms
# 0 1 1 2 3 5 8 13 21 34  . . . . and so on

x = 1  
y = 0 
z = 0  # Variable which stores the Fibonacci Series
i = 0
l1 = []
l = int(input("Please Enter the lenght of series : "))
for i in range(l):  # this loop generates the series according 
    l1.insert(i,z)  # to the lenghth given by user
    z = x + y
    x = y
    y = z
print (l1)
    
#Never thought it would be this easy to write the code for Fibonacci series

