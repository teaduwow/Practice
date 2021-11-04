# 猜數字遊戲
score = 10
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while score != guess and not (out_of_limit):
    guess_count += 1
    if guess_count<=guess_limit:
        guess=int(input("請輸入數字:"))
        if guess > score:
            print("再小")
        elif guess < score:
            print("再大")
    else:
        out_of_limit=True
        
if out_of_limit:
    print("你輸了")
else:
    print ("恭喜")


