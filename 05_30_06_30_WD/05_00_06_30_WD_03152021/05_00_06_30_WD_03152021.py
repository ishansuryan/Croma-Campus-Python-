# num = int(input("Enter a number"))

# if num<10:
#     if num>5:
#         print("The number is grater than 5 nut smaler than 10")
    
#     elif num < 5:
#         print("The number is smaller than 5")
        
#     else: 
#         print("Numbers is equal to 5")

# elif num == 10:
#     print('the number is equal to 10')

# else:
#     print("the number is grater than 10")


# year = 2000
# if year % 4 == 0:
    
#     if year % 100 == 0:
#         print("it is a century and leap year")
    
#     else: print("It is a leap year")

# else: print('it is not a leap year')

sex = 'M'

if sex == "F":
    print('She can work in Urban Area only')

elif sex == "M":
    age = 40
    
    if 20<age<40:
        print("He can work anywhere")
    
    elif 40<=age<60:
        print("He can work in urban areas only")
    
    else:
        print('ERROR')
num = 123456789000000

print(str(num)[::-1])