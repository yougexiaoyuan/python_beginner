#小院里的霍大侠 - 兴趣编程
#案例 - 问答游戏
#学习点： 
#def：def是声明一个函数方法的语法。函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。
#while：循环判断的语法，后面跟着判断的调节，当不满足条件则退出循环
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("答案正确。")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("答案错误了，请重试。")
            attempt = attempt + 1
    if attempt == 3:
        print("正确答案是：",answer )
    
score = 0
print("请回答下面问题：")
guess1 = input("你觉得学编程有好处吗？ ")
check_guess(guess1, "有")
guess2 = input("你觉得学编程容易吗？ ")
check_guess(guess2, "容易")
guess3 = input("你觉得多长时间可以入门Python？")
check_guess(guess3, "1个月")
print("你的分数为："+ str(score))