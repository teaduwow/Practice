#if 判斷句

#1.
#如果 我肚子餓
#     我就去吃飯
hungry=True
if hungry:
    print("我就去吃飯")

#2.
#如果 今天下雨
#     我就開車去上班
#否則
#      我就走路去上班

rainy=False

if rainy:
    print("我就開車去上班")
else:
    print('我就走路去上班')


#3.
#如果 你考100
#    我給你1000元
#或是如果 你考80以上
#   我給你500
#或是如果 你考60以上
#   我給你100
#否則
#   你給我300
score=90
# ==意思是左邊右邊相等 就會變true 反之 flase
if score==100:
    print("我給你1000")
elif score>=80:
    print("我給你500")
elif score>=60:
    print("我給你100")
else:
    print("你給我300")

#4.
#如果 你考100 且 今天下雨
#   我給你1000
#否則
#   你給我100
score=100
rainy=False
if score==100 and rainy:
    print("我給你1000")
else:
    print('你給我100')

#5.
#如果 你考100 或 今天下雨
#   我給你1000
#否則
#   你給我100
score=100
rainy=False
if score==100 or rainy:
    print("我給你1000")
else:
    print('你給我100')

#6.
#如果 你沒有考100 或 沒有下雨
#   我給你1000
#否則
#   你給我100
score=90
rainy=True
if score!=100 or not rainy:
    print("我給你2000")
else:
    print('你給我100')

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
            return num1
    elif num2>=num1 and num2>=num3:
            return num2
    else:
            return num3
print(max_num(100,30,40))


