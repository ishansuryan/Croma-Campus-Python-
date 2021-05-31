# while loop
# syntax while condition risulting in True or False:

# gate = ['north', 'east', 'west', 'south']

# user_val = '!'

# while user_val not in gate :
#     user_val = input('Enter a gate to exit or q to quit: ').lower()

#     if user_val == 'q':
#         print('Are you sure tou want to quit [y/n]: ',end = ' ')
#         user_val = input()

#         if user_val == 'y':
#             break



# Guess the number game

h = 1000
l = 0
turn = 0

while turn <10:

    guess = (h+l)//2
    print('my guess is:',guess)
    print('Please type "h" if my guess is higher, "l" for my guess is lower and "c" if my guess is correct: ', end = '')
    usr_inpt = input()
    if usr_inpt in 'hlc':
        turn +=1

        if usr_inpt == 'h':
            h = guess-1
        
        elif usr_inpt =='l':
            l = guess + 1
        
        else :
            print(f'Yes I got the answer in {turn} tries')
            break

        if  turn == 9:
            print(f'your number is {(h+l)//2}')
            break
    
    else: print('Please enter a valid value')  
