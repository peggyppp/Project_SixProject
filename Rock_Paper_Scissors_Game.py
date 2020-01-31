'''
Rock, Paper, Scissors Game
Make a rock-paper-scissors game where it is the player vs
the computer. The computer’s answer will be randomly generated,
while the program will ask the user for their input.

This project will better your understanding of while loops and
if statements.
'''
def new_game():
    #產生電腦結果
    import random
    computer = random.choice(['R', 'P', 'S'])
    print('computer: ', computer)
    return computer

def enter_ch():
    #判斷input是否為有效值 或要退出程式-> quit

    print(' << Rock, Paper, Scissors Game >>')
    enter = input('Please choose: R -> Rock, P -> Paper, S -> Scissors: ')

    if enter == 'quit':
        return 'quit'
    elif enter in ['R', 'P', 'S']:
        return enter
    else:
        print('Invalid input ->', enter)
        return enter_ch()



def check(computer: int, user: int):
    #檢查函數，判定結果並進行下一局。若輸入quit則結束程式

    if user == 'quit':
        print()

    elif user == computer:
        print('>>>> 平手!')
        print('--------------------------------------')
        print()
        check(new_game(),enter_ch())

    elif (user == 'R' and computer == 'S') or (user == 'S' and computer == 'P') or (user == 'P' and computer == 'R'):
        print('>>>> You Win!')
        print('--------------------------------------')
        print()
        check(new_game(),enter_ch())

    elif (user == 'R' and computer == 'P') or (user == 'S' and computer == 'R') or (user == 'P' and computer == 'S'):
        print('>>>> Computer Win!')
        print('--------------------------------------')
        print()
        check(new_game(),enter_ch())





if __name__ == "__main__":
    # 這裏是你的測試碼
    print('--------------------------------------')
    print()

    computer = new_game()
    user = enter_ch()

    check(computer, user)
