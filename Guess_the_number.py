'''
Guess The Number
Write a programme where the computer randomly generates a number
between 0 and 20. The user needs to guess what the number is.
If the user guesses wrong, tell them their guess is either too high,
 or too low.
This will get you started with the random library if you haven't
already used it.
'''

def enter_num():
    #判斷input是否為數值 或要退出程式-> quit
    num = input('Please guess an integer between 0 and 20: ')
    try:
        if num == 'quit':
            return 'quit'
        elif int(num):
            guess = int(num)
            return guess
    except:
        print('Invalid input ->', num)
        return enter_num()



def check(guess: int, target: int):
    #檢查函數，比較guess和target是否相等。若否，告知大或小，並重新輸入數字

    if guess == target:
        print('Correct!')

    elif guess == 'quit':
        print()

    elif guess < target and guess in range(0, 21):
        print('Too low')
        check(enter_num(), target)

    elif guess > target and guess in range(0, 21):
        print('Too high')
        check(enter_num(), target)

    else:
        print('Invalid range')
        check(enter_num(), target)




if __name__ == "__main__":
    # 這裏是你的測試碼
    print('--------------------------------------')
    print()

    import random

    target = random.randint(0, 20)
    guess = enter_num()

    check(guess, target)
    #print(check(guess, target))
