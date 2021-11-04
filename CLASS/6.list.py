#列表list
score=[90,80,60,20,95]
score1=90
scoere=80
scoere=60
scoere=20
scoere=95
print(score)

frined=["黑","黃","綠"]
things=[90,"黑",True]
print(things)
#{} []裡面順序會反過來

print(score[0])
print(score[3])
print(score[-1])
print(score[-2])
#位子0開始取到第2位不包刮第2位
print(score[0:2])
print(score[1:4])
print(score[0:])
print(score[:4])
phrase = "HELLO MR. WHITE"
print(phrase[3])
print(phrase[0:6])

score[0]=30
print(score)

score.extend(frined)

print(score)

#列表後面加一個值
score.append(30)
print(score)

score.insert(1,100)
print(score)

score.remove(80)
print(score)

score.clear()
print(score)

#移除列表最後一位
score.pop()
print(score)

#由小到大排列
score.sort()
print(score)

#列表反轉
score.reverse

#函數位子
print(score.index(100))

#有幾個60
print(score.count(60))