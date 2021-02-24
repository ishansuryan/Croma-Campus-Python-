# for row in range(5):
    
#     for space in range(5-row-1):
#         print(end = ' ')
    
#     for start in range(5):
#         print(end = '*')
    
#     print()
    
# While Loops:

# syntax:

# while Condition: Condition can be anything which risults in True or False
# Can be infinite loop easily
# temination conditionj is a must.

# exit = ['North', 'East', 'West', 'South']

# user = input("Please Choose an exit: ").capitalize()

# count = 1

# while True:
#     if user == 'Quit':
#         break 
#     count +=1 # same as count = count + 1    
#     user = input("Please Choose an exit: ").capitalize()
#     if user in exit:
#         print ('you guessed it in {} times'.format(count))
#         break

# Guess the number game:

print('choose any number between 0 and 1000')
low = 0
high = 1000
count = 0
while True :
    guess = (high+low)//2
    print('I guessed the number', guess)
    print("input (h) if guess is higher (l) if my guess is lower (c) if my guess is correct: ", end = '')
    value = input().casefold()
    
    if value in 'hlc':
        count +=1
        
        if value == 'h':
            high = guess -1
        
        elif value == 'l':
            low = guess + 1
        
        elif value == 'c':
            print("i guessed the number in {} times".format(count))
            break
    
    elif value.casefold() == 'quit':        
        print("It's ok you quit")
        break
            
    else : print('please enter correct value')
    
    if count == 9:
            print('number is: ', (high + low)//2)
            print("I guessed the number in {} times".format(count+1))
            break