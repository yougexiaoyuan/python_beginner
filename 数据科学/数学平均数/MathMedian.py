
#小院里的霍大侠 - 兴趣编程
#案例 - 数学平均数，通过对平均数，中位数和众数理解python对数学的编程模式
#学习点： 
#sum(),len()：sum是数字求和；len是数组长度
#.sort()：代表对应数组按顺序排列
#3//2的//：是整除的意思，3//2等于1
#max()：是数组最大值

# 平均数：平均值是数据集中所有值的平均值。
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
mean = sum(list1)/len(list1)
print(mean)

# 中位数：统计学中的专有名词，是按顺序排列的一组数据中居于中间位置的数，
# 代表一个样本、种群或概率分布中的一个数值，其可将数值集合划分为相等的上下两部分。
# 对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。
# 如果观察值有偶数个，通常取最中间的两个数值的平均数作为中位数。
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
list1.sort()

if len(list1) % 2 == 0:#==0代表偶数，否则为奇数
    m1 = list1[len(list1)//2]
    m2 = list1[len(list1)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list1[len(list1)//2]
print(median)

# 众数：众数是所有值中出现频率最高的值。
list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}
for i in list1:
    frequency.setdefault(i, 0)#给数组所有值赋值为0
    frequency[i]+=1#相同索引对应的值加1，这样目的就是频率多的值就最大了

frequent = max(frequency.values())#获取到这个字典类型最大的值
for i, j in frequency.items():#循环判断字典键值是否等于刚才最大的频率值，最大则输出
    if j == frequent:
        mode = i
print(mode)