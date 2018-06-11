#this program is about Palindrome
#Palindrom is something who have the same result if reversed for e.g. " MOM "
#how do we know whether the given string or number is palindrome
number = 0
number = int(input("Please Enter the number to Check whether it is a palidrome : "))
reverse = 0
temp = 0


temp = number

while(reverse<=number):
    reverse = reverse + temp % 10    # 1221 revrse = 1       reverse = 12    reverse 122         reverse = 1221
    if(reverse >= number):
        print(reverse)
        exit()
    reverse = reverse * 10  # reverse = 10                  reverse = 120   reverse 1220
    temp = int(temp/10)     # temp = 122                    temp = 12       temp = 1



#print(reverse)
