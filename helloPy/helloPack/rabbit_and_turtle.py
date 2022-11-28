'''
Created on 2022/11/04

@author: User105

'''

import random
import time

a = 0
b = 0
goal = 100

user = input("どっちが勝つか予想しよう！ a or b:");

print("競争開始！")

while (a < goal) and (b < goal):
    a = a + random.randint(0, 10)
    b = b + random.randint(0, 10)
    print()
    print("a:"  + "*" * a + "@")
    print("b:"  + "*" * b + "@")
    time.sleep(1);

print()

if a == b:
    winner = "even"
elif a > b:
    winner = "a"
else:
    winner = "b"
    
if (winner == "even") or (winner == user):
    print("あたり！")
else:
    print("はずれ！")