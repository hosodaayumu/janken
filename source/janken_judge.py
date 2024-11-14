def judge(user, cpu):
    if user == cpu:
        return 'same'
    elif (user == 1 and cpu == 2) or (user == 2 and cpu == 3) or (user == 3 and cpu == 1):
        return 'win'
    else:
        return 'lose'
    