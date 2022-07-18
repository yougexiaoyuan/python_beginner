#小院里的霍大侠 - 兴趣编程
#案例 -  BMI计算器
#学习点： 
#BMI：体重指数的计算方法是将一个人的体重（公斤）除以身高（米），然后再除以他们的身高。
#float：代表对范围数值进行浮点求值
#if,else,elif：条件逻辑判断，一定要理解哦。
Height=float(input("请输入你的身高（厘米）: "))
Weight=float(input("请输入你的身高（公斤）:"))
Height = Height/100
BMI=Weight/(Height*Height)
print("你的身体BMI指数为：",BMI)
if(BMI>0):
	if(BMI<=16):
		print("你的身体很棒哦，继续加油")
	elif(BMI<=18.5):
		print("你的BMI不错，在健康范围内")
	elif(BMI<=25):
		print("你身体BMI刚刚好")
	elif(BMI<=30):
		print("你有点超重了，要注意哦")
	else: print("你已经验证超重了，注意饮食，多锻炼呀！")
else:("输入的数值错误，请重试。")