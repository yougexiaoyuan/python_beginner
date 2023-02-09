#小院里的霍大侠 - 兴趣编程
#案例 - 邮箱分割器
#学习点： 
#strip()：strip 函数来删除空格
#.index("@")：是对字符串中@字符进行分割
# (f"hi,"{xxx})：其中f代表对括号中字符串格式化，里面的大括号可以用变量替换，这样就可以动态输出内容了

email = input("请输入你的Email地址: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"您的邮箱用户名： '{username}' ， 您的邮箱域名：'{domain_name}'")
print(format_)
input()

