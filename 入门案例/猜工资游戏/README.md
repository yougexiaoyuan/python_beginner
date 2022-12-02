
![猜薪资-竖-封面.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/34388852/1669772634748-344dc4f4-4821-4b7a-b153-9fb0efef1d5f.jpeg#averageHue=%23e9f6e9&clientId=uacfe83da-8aa1-4&crop=0&crop=0&crop=1&crop=1&from=ui&id=u7c027415&margin=%5Bobject%20Object%5D&name=%E7%8C%9C%E8%96%AA%E8%B5%84-%E7%AB%96-%E5%B0%81%E9%9D%A2.jpg&originHeight=1920&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=102569&status=done&style=none&taskId=u9ae169f7-efd8-49b4-8514-8900b75ef6e&title=)
<a name="fovq7"></a>
# **案例介绍**

欢迎来到我的小院，我是霍大侠，恭喜你今天又要进步一点点了！<br />我们来用Python相关属性知识，做一个猜数字的案例。你可以通过控制台的提示信息，输入1-100之间的随机数，输入的数字与随机生成的数字做对比，输出提示信息。
<a name="phntZ"></a>
# **案例演示**

运行程序后，我们可以看到控制台输出的提示信息，按要求输入数字，根据提示信息改变数字的大小，直至成功。

![](https://cdn.nlark.com/yuque/0/2022/png/34388852/1668995516073-f0f784d6-5816-4e7a-ab56-f86bd8ac3143.png#averageHue=%231f1f1f&clientId=u864c8dd7-6f91-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=u80a2f788&margin=%5Bobject%20Object%5D&originHeight=1161&originWidth=2283&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u850997c8-4864-432f-8033-3c6df8d95cc&title=)
<a name="XxoKH"></a>
# **源码学习**

进入核心代码学习， 要想使用随机数，需先导入随机数模块。通过random.randrange(1,100)<br />获取1-100范围内的随机数。定义控制台输入的次数counter，通过while循环实现反复猜测的效果，每循环一次counter加一。if函数对随机数和输入的数进行判断，根据提示信息，不断改变所猜数的范围，直至成功。

```
import random

def guessnum():
   n=random.randrange(1,100)
   print('请在1-100之间猜一个数字:')
   counter=0
   while True:
       counter+=1
       guess=int(input())
       if n<guess:
         print('猜大了！！！')
       elif n>guess:
         print('猜小了！！！')
       elif n==guess:
         print('恭喜你,下个月涨薪资!!!')
         print('你总共猜了%d次'  %counter)
         break
   if counter>=8:
        print('很遗憾，涨薪资的机会渺茫!!!')
print('>>>>>=====-游戏开始-=====<<<<<')
guessnum()
while True:
    option=input('还想再闯关一次吗?（回答y或n)\n')
    yes='y'
    no='n'
    if option==yes:
     guessnum()
    elif option==no:
      print('>>>>>=====-游戏结束-=====<<<<<')
      break
    else:
        print('您的回答超出大脑!')
        print('>>>>>=====-游戏结束-=====<<<<<')
```




关注我，跟着我每天学习一点点，让你不在枯燥，不在孤单..
<a name="J3B4h"></a>
# **职场工作学点编程还能加薪，你还等什么？**

**全网可搜：小院里的霍大侠， 免费获取简单易懂的实战编程案例。编程/就业/副业/创业/资源。**<br />私微信：huodaxia_xfeater<br />二维码： [http://www.yougexiaoyuan.com/images/weixin_huodaxia.jpg](http://www.yougexiaoyuan.com/images/weixin_huodaxia.jpg)<br />公众号：有个小院（微信公众号：yougexiaoyuan）<br />github：yougexiaoyuan (视频源码免费获取)<br />（部分素材来源于互联网，如有保护请联系作者）
