#this program is about Palindrome
#Palindrom is something who have the same result if reversed for e.g. " MOM "
#how do we know whether the given string or number is palindrome
number = 0
reverse = 0
temp = 0
number = int(input("Please Enter the number to Check whether it is a palidrome : "))
print(number)
temp = number #given number is copied in temp variable

while(temp != 0):                       # until the number is reversed
    reverse = reverse * 10              # reverse will store the reversed number by one digit and shift the place of digit
    reverse = reverse + temp % 10       # remainder of the given number gives last digit every time and is stored in reverse
    temp = int(temp/10)                 # every last digit of given number is eliminated here 
if(reverse == number):
    print("Number is a Palindrome")
    
else:
    print("Number is not a Palindrome")


