def pon():
    input_flag = True
    user = int(input('1.グー 2.チョキ 3.パー\nあなたの手を選択してください。>'))
    if user in [1,2,3]:
        if user == 1:
            print('あなた：グー')
        elif user == 2:
            print('あなた：チョキ')
        else:
            print('あなた：パー')
        return user
        
    else:
        while input_flag == True:
            user = int(input("1,2,3の数字を半角英数字で入力してください>"))
            if user in [1, 2, 3]:
                input_flag = True
            if user == 1:
                print('あなた：グー')
            elif user == 2:
                print('あなた：チョキ')
            else:
                print('あなた：パー')
            return user
    