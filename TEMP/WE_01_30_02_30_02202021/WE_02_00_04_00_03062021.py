from datetime import datetime

current = datetime.now()
time = current.strftime('%H:%M:%S, %A, %d-%B-%Y ')
print(time)

print(datetime.fromtimestamp(10.2))
print(datetime.today())

print(help(datetime))