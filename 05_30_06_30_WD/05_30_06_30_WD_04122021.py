from datetime import datetime

now_=datetime.now()
print(now_)
print(now_.strftime('%A-%d-%B-%Y_%I-%m-%S-%p'))
print(now_.strftime('%c'))