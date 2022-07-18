#小院里的霍大侠 - 兴趣编程
#案例 - 投掷骰子
#学习点： 
#random.randint()：根据我们指定的开始和结束返回一个随机整数。
#while：循环判断的语法，后面跟着判断的调节，当不满足条件则退出循环

import random
#定义掷骰子的最小值是 1，最大值是 6
min_val = 1
max_val = 6
#定义是否需要循环的标志
roll_again = "是"
#l循环判断
while roll_again == "是" or roll_again == "y":
    print("旋转骰子...")
    print("骰子数字为：")
    #输出随机的数字
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    roll_again = input("是否继续投掷骰子？请输入：") 
