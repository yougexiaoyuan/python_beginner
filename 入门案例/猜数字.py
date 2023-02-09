import random
import easygui

# 产生一个随机数
n = random.randint(1,100)
m = int(easygui.enterbox('请输入一个1-100之间的数字',title='猜数字小游戏'))
i = 1 # 统计一共猜了几次

while n!=m:
    if n<m:
        m = int(easygui.enterbox('猜大了,请重新猜!',title='猜数字小游戏'))
    else:
        m = int(easygui.enterbox('猜小了,请重新猜!',title='猜数字小游戏'))
    # 每猜一次，i的值加1
    i += 1
# 循环结束--猜对啦
easygui.msgbox('恭喜您在第'+str(i)+'次,猜对啦!')
