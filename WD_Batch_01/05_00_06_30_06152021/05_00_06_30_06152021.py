# from datetime import datetime, time, tzinfo
# from pytz import timezone
# us_time = datetime.now(timezone('US/Eastern'))
# print(str(us_time))
# # datetime.now(tzinfo = utc)
# print(help(timezone))

 
# Functions
# def addition():
#     a = int(input("Enter a number for addition: "))
#     b = int(input("Enter a number for addition: "))
#     print("The sum is:",a+b)

# addition()
# addition()
# addition()
# addition()

def minus(a,b):
    return a-b

r1 = minus(2,3)
print(r1)

def devide(a,b):
    print('the devision result is', a/b)

r2 = devide(3,5)
print('value of r2 is:',r2)

# Wap to to check wether a string is a palindrome or not it will return True or false

def palindrome(s):
    if str(s).lower() == str(s).lower()[::-1]:
        return True
    return False

print(palindrome("Nitin"))