#Let us Find out the largest and second largest number in a list
#we will first get some numbers from the user
#Then we will store it in a list
#After that largest and second largest will be given in output
def largest():      # this function gives us largest value
    bucket_length = len(temp)
    large = temp[0]
    for i in range(bucket_length):
        if(temp[i] >= large):
            for j in range(bucket_length):
                if(temp[i]>=bucket[j]):
                    large = temp[i]
                else:
                    large = temp[j]
    return large

j = 0
bucket = []
large = 0
second_large = 0
size = int(input("Please enter the size of list : "))
for i in range(size):
    bucket.insert(i,int(input("Enter number : "+str(i+1)+" : ")))
temp = bucket
temp2 = []
bucket_length = len(temp)
print("The largest number is : " + str(largest()))

# to get second largest we eliminate the largest number even if there are two equal numbers 
large = largest()
for i in range(bucket_length):
    if(large!=temp[i]):
        j = j + 1
        temp2.insert(j,temp[i])
temp = []
temp = temp2
print("The Second Largest number is : " + str(largest()))
    
    
    
    
