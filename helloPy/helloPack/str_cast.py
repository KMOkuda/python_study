'''
Created on 2022/11/04

@author: User105

変数の中身を文字で出力したいときはstrでキャストする。
'''

apple = 350;
msg = ("リンゴは" + str(apple) + "円です。\n") * 3;

#msg = "リンゴは" + str(apple) + "円です。\n" * 3;
#↑これだと円ですのところだけ3回表示される。

print(msg);