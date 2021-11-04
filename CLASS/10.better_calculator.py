#建立計算機
num1=float(input("請輸入第一數:"))
op=input("請輸入運算符號:")
num2=float(input("請輸入第二數:"))


if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("不支援的運算")