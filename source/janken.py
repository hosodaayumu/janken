import player
import computer
import janken_judge

def janken_main():
    count = 1
    cnt_user = 0
    cnt_cpu = 0
    
    for janken in range(1,4):
        print(f"\n--- ラウンド{janken}---")

        while True:
            user = player.pon()
            cpu = computer.pon()
            if janken_judge.judge(user, cpu) == 'same':
                print('あいこです！もう一回チャレンジ！')
            elif janken_judge.judge(user, cpu) == 'win':
                print('あなたの勝ちです！')
                cnt_user += 1
                count += 1
                break
            elif janken_judge.judge(user, cpu) == 'lose':
                print('コンピューターの勝ちです！')
                cnt_cpu += 1
                count += 1
                break
    
    
    print('---------------')
    print('【最終結果】')
    print(f'あなた：{cnt_user}勝')
    print(f'コンピューター：{cnt_cpu}勝')
    if cnt_user > cnt_cpu:
        print('あなたの総合勝利です！')
    else:
        print('あなたの負けです……')


if __name__ == '__main__':

    janken_main()

