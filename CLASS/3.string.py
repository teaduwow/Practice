#如何使用字串、字串用法
print("hello \nMr.white")
print("hello \n \"mr.white\"")
#hello" mr. white
print("hello " + "mr.white")
phrase = "hello"
print(phrase + " mr. white")

# 函式 fuction
phrase = "HELLO MR. wHITE"

#字母變小寫 /檢查字母是否都是小寫
print(phrase.lower().islower())

#字母變大寫
print(phrase.upper())
print(phrase.islower())

#檢查字母是否大寫
print(phrase.isupper())

#第幾個字母
print(phrase[4])

#字母位子在第幾個
print(phrase.index("M"))

#字母替換
print(phrase.replace("M","Z"))
