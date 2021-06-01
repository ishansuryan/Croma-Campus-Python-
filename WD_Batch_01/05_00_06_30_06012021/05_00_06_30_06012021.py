# for i in range(5):
#     for space in range(5-i-1):
#         print(end = ' ')
#     for star in range(5):
#         print('*', end = '')
#     print()

# else with a loop

for i in range(5):
    j = input('Enter the gate: ')
    if j.lower() in ['north', 'east', 'south', 'west']:
        break

else:
    print('loop ended normally')
