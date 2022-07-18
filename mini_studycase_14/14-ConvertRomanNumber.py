#小院里的霍大侠 - 兴趣编程
#案例 - 罗马数字转阿拉伯数字
#学习点： 
#for：for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
#range：range返回一个序列的数; len() 返回列表的长度，即元素的个数。
#str(x)：str把数值转换成字符串输出。
tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # 如需要更多可以往下写
}
#定义一个转换函数
def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):  #循环的遍历方式是通过索引
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum

while True:
    temp = input("请输入罗马字符：")
    if temp == '退出': break
    print("对应阿拉伯数字为："+str(RomanNumeralToDecimal(temp)))
input()
