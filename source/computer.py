from random import randint
def pon():
    cpu =  randint(1, 3) 
    if cpu == 1:
        print('CPU：グー')
    elif cpu == 2:
        print('CPU：チョキ')
    else:
        print('CPU：パー')   
    return  cpu