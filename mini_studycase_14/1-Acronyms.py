
#小院里的霍大侠 - 兴趣编程
#案例 - 获取首字母
#学习点： 
#str()：是把括号里面内容变成一段字母文字，转换成字符串
#split()：是将括号中字符分割成字字符串，不指定默认用空格分割
#print()：输出结果信息

user_input = str(input("请输入一串单词（用空格分割字母单词）: "))
text = user_input.split() #用空格来分割输入的内容
a = " " #声明一个变量
for i in text:  #一个循环语法，这里是根据上面输入文本分割后得到数量
    a = a+str(i[0]).upper() #分割后每个字符大写相连
print(a)  #输出结果

input()