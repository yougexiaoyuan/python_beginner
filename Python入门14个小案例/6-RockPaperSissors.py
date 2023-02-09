#小院里的霍大侠 - 兴趣编程
#案例 - 石头剪刀布
#学习点： 
#random.choice()：根据随机数字，随机生成一个数值
#条件语法：学习通过if,else,elif的逻辑条件判断

import random
choices = ["剪刀","石头", "布"]
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("请输入- 石头, 布或者剪刀？").capitalize()
    computer = random.choice(choices)
    #这里说游戏的逻辑判断
    if player == computer:
        print("出的一样，重新来")
    elif player == "石头":
        if computer == "布":
            print("你输了哦！", computer, "包住了", player)
            cpu_score+=1
        else:
            print("很棒，你赢了！", player, "敲碎了", computer)
            player_score+=1
    elif player == "布":
        if computer == "剪刀":
            print("你输了哦！", computer, "剪坏了", player)
            cpu_score+=1
        else:
            print("很棒，你赢了！", player, "包住了", computer)
            player_score+=1
    elif player == "剪刀":
        if computer == "石头":
            print("你输了...", computer, "敲碎了", player)
            cpu_score+=1
        else:
            print("你赢了!", player, "剪坏了", computer)
            player_score+=1
    elif player=='查看分数':
        print("最终比分：")
        print(f"电脑分数：{cpu_score}")
        print(f"你的分数：{player_score}")
        break

input()

