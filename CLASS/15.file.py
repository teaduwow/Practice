#讀取檔案  寫入

# open("檔案路徑",mode="開啟模式")
#絕對路徑 
#箱對路徑

#mode="r"讀取
#mode="w"覆寫
#mode="a"在原先的資料後寫東西

# file = open("C:/Users/ray155093/Desktop/python file/123.txt", mode="r")
# file = open("123.txt", mode="r")
# print(file.readline())


# for line in file:
    #  print(line)

# print(file.readlines())     

from os import write


# file=open("123.txt",mode="w",encoding="utf-8")
# file.write("hi\n你好")


# file.close()

with open("123.txt",mode="w",encoding="utf-8") as file:
    file.write("\ns你好呀")
