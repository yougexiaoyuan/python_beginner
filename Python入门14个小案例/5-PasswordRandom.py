#小院里的霍大侠 - 兴趣编程
#案例 - 随机生成密码
#学习点： 
#random.sample(s,passlen )：根据输入的数值，随机抓取s字符串的字符，组成输入值长度的数组
#str.join(sequence)：用于将序列中的元素以指定的字符连接生成一个新的字符串。

import random
passlen = int(input("请输入你要生成的密码长度："))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen ))
print(p)

input()

