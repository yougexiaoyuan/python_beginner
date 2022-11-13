<a name="pMIWY"></a>
# **Python算法入门 - 数学平均数**
欢迎来的我的小院，跟着我每天学习一点点，让你不再枯燥，不再孤单......<br />关注我，学习更多简单易懂的编程实战案例。进主页获取更多编程/就业/副业/创业/资源。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/209450/1668305932204-f3f9c66c-9d82-4b0e-a88a-f44b2ab902ce.png#averageHue=%230c0c0c&clientId=u31a439f6-de8f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=635&id=uda9522b4&margin=%5Bobject%20Object%5D&name=image.png&originHeight=635&originWidth=1144&originalType=binary&ratio=1&rotation=0&showTitle=false&size=37607&status=done&style=none&taskId=ub7632074-cdd8-46c2-a8bb-eb0fb73c953&title=&width=1144)
<a name="zi6jK"></a>
## **案例：数学平均数**
平均值、中位数和众数是我们处理数字的几乎每个领域中使用的统计基础。Python是用于数值计算的最佳编程语言之一。因此，您应该知道如何在不使用任何内置 Python 库或模块的情况下使用 Python 计算均值、中位数和众数。因此，在本文中，我将带您了解如何使用 Python 计算均值、中位数和众数。<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/209450/1668306005937-4cb086fa-6fa9-4bda-b91a-39f421e02f94.png#averageHue=%2399aa6c&clientId=u31a439f6-de8f-4&crop=0&crop=0&crop=1&crop=1&from=paste&height=644&id=u9669dbd0&margin=%5Bobject%20Object%5D&name=image.png&originHeight=644&originWidth=1152&originalType=binary&ratio=1&rotation=0&showTitle=false&size=152297&status=done&style=none&taskId=uc271f5be-d119-49ed-91ae-dfa152e4a4e&title=&width=1152)
<a name="rC6cP"></a>
## **演示**
下面代码运行后生成数值如图<br />![image.png](https://cdn.nlark.com/yuque/0/2022/png/209450/1668305852728-a99d23ee-ff75-48e4-a0a8-adb953dc4bfd.png#averageHue=%23212121&clientId=u31a439f6-de8f-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ue72152aa&margin=%5Bobject%20Object%5D&name=image.png&originHeight=50&originWidth=152&originalType=url&ratio=1&rotation=0&showTitle=false&size=661&status=done&style=none&taskId=u8cd5a94b-5073-483a-8050-2ee7178531d&title=)
<a name="QJAZA"></a>
## **学习**
这个案例对初学者有点难度，首先要理解几个数学数值的含义。然后理解通过python代码编程的方式怎样去使用这些数值。<br />#学习点： <br />#sum(),len()：sum是数字求和；len是数组长度<br />#.sort()：代表对应数组按顺序排列<br />#3//2的//：是整除的意思，3//2等于1<br />#max()：是数组最大值
```python
#小院里的霍大侠 - 兴趣编程
#案例 - 数学平均数，通过对平均数，中位数和众数理解python对数学的编程模式

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
```
<a name="SUGBW"></a>
## **思考**
![image.png](https://cdn.nlark.com/yuque/0/2022/png/209450/1668306101330-6c8aa70a-2e8f-4887-875f-de2882fb7add.png#averageHue=%239be0e0&clientId=u31a439f6-de8f-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u54a0f1fc&margin=%5Bobject%20Object%5D&name=image.png&originHeight=787&originWidth=1280&originalType=url&ratio=1&rotation=0&showTitle=false&size=1144964&status=done&style=none&taskId=ud068f9bd-67fb-47d2-b2f6-8868eb10f84&title=)<br />再次感受到了数学的博大精深，同时你是否发现数学中的一些问题，可以用编程很好的实现求值。python目前是对数学算法支持最好的，有着庞大的类库，如果你以后要学习机器学习，大数据，一定要好好理解这个初级的代码哦。<br />试着用代码实现一起其他的数学问题......<br />![结尾LOGO卡通版.png](https://cdn.nlark.com/yuque/0/2022/png/209450/1668306167002-84458c68-d551-4f07-a5c8-7f411cd3d217.png#averageHue=%23525252&clientId=u31a439f6-de8f-4&crop=0&crop=0&crop=1&crop=1&from=drop&id=uf3105d26&margin=%5Bobject%20Object%5D&name=%E7%BB%93%E5%B0%BELOGO%E5%8D%A1%E9%80%9A%E7%89%88.png&originHeight=1080&originWidth=1920&originalType=binary&ratio=1&rotation=0&showTitle=false&size=68002&status=done&style=none&taskId=ua432adbe-e604-4c6c-a165-9a5937e8eed&title=)


