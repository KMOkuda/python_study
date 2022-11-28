'''
Created on 2022/11/04

@author: User105

'''

num = int(input("入力する生徒の数は？："))
points = []
max = 0
min = 100
total = 0

for i in range(num):
    point = int(input(str(i + 1) + "人目の点数を入力して下さい："))
    points.append(point)
    total += point
    
    if max < point:
        max = point
    
    if min > point:
        min = point
        
print("平均点：" + str(float(total) / num))
print("最高点：" + str(max))
print("最低点：" + str(min))
