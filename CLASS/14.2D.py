#2維列表、朝狀迴圈
#row=行
#colum=列

nums=[
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9]
    ]

print (nums[2][2])

for row in nums:
     for col in row:
         print(col)

for col in nums:
    for row in col:
        print(col)       