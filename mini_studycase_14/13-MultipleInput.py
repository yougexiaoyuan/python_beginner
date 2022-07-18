#小院里的霍大侠 - 兴趣编程
#案例 - 用户多次输入
#学习点： 
#while：while 循环，这是 Python 最通用的循环语句。
#break：break 语句用于立即退出 while 循环语句。
while True:
    reply = input("请输入文本：")
    if reply == '停止': break
    print(reply)
input()
