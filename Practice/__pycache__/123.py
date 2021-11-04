from Que import que

test = [
    "1. 1+3=?\n(a) 10\n(b) 100\n(c)4\n\n",
    "2. 1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "3. 香蕉是什麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\n\n"
    ]

ques = [
    que(test[0],"a"),
    que(test[1],"a"),
    que(test[2],"a")
]

def run_test(ques):
    score = 0
    for que in ques:
        answer = input(que.descri)
        if answer == que.answer:
            score +=1
    print ("你得到"+str(score)+"分，共"+str(score)+"題")

run_test(ques)