# n_row = 5
# for row in range(n_row):
#     for column in range(n_row - row):
#         print(end = ' ')
#     for star in range(row+1):
#         print(end = '*')
#     if row == 12:
#         print('\nBreaking the loop')
#         break
#     print()

# else:
#     print('the loop ended normally')
    
# While loops
# Syantax = 
# while Condition which risults in true or false: '''If condition id true we enter inside loop'''
#     code to be executer till condition is True   
# n_row = 0
# while n_row <=2:
#     print('the loop is executed {} number of times'.format(n_row+1))
#     n_row+=1          # n_row = n_row + 1


# gate = ['North','East','West', 'South']

# user_input = input("Enter the gate to exit")

# while user_input.capitalize() not in gate:
#     print("You chose the wrong gate choose again")
#     user_input = input("Enter the gate to exit: ")
#     if user_input.casefold() == 'quit':
#         print("You quit")
#         print('You Loose')
#         break
    
# else:
#     print('You chose the correct gate')

# Number Guessing game
user_input = None
tries = 0
high = 1000
low = 0
print('guess a number between 0 to 1000 and i will guess that number in max 10 tries')
while tries < 9:
    guess = (high + low)//2
    print(f'my guess is {guess}')
    user_input = input("enter h for my guess is higher l for my guess is lower c if my guess is correct: ")
    
    if user_input in 'hlc':
        
        tries +=1
        
        if user_input == 'h':
            high = guess -1
        
        elif user_input == 'l':
            low = guess +1
        
        elif user_input == 'c':
            print(f'Yes i guessed the number in {tries} tries')
            break
    
    else :
        print('Please enter a valid input')

else:
    print(f"Your number is {(high + low)//2} and i guessed it in {tries +1} tries") 