
<a name="msYIG"></a>
# **案例介绍**
欢迎来到我的小院，我是霍大侠，恭喜你今天又要进步一点点了！<br />我们来用Python编程实战案例，做一个羊了个羊小游戏。输入序号，三个相同的序号会自动消除，消除所有的序号，完成游戏。
<a name="womDK"></a>
# **案例演示**
用户对在槽位中输入小羊对应的序号，七个槽位，每三个相同的序号自动消除，当所有的序号被消除后，游戏通关。<br />![](https://cdn.nlark.com/yuque/0/2022/png/34403478/1669606348342-7bc86ea7-594e-45b6-a752-31e4ebd68b78.png#averageHue=%23131a2c&clientId=u6dc6cf94-ec39-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ua4dc4540&margin=%5Bobject%20Object%5D&originHeight=233&originWidth=439&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u9a55ca24-07ca-4d5f-aeb2-5500282c28c&title=)
<a name="F9iBa"></a>
# **源码学习**
进入核心代码学习，我们先来看初始界面的核心代码。
```python
def play(self):
    self.check()
    while True:
        lay = f'''
            欢迎来到我的小院
            让我们一起来玩"羊了个羊"吧
            ====================
            1.{self.l1[-1] if len(self.l1) != 0 else '[      ]'}\t 2.{self.l2[-1] if len(self.l2) != 0 else '[      ]'}\t 3.{self.l3[-1] if len(self.l3) != 0 else '[      ]'}
            4.{self.l4[-1] if len(self.l4) != 0 else '[      ]'}\t 5.{self.l5[-1] if len(self.l5) != 0 else '[      ]'}\t 6.{self.l6[-1] if len(self.l6) != 0 else '[      ]'}
            7.{self.l7[-1] if len(self.l7) != 0 else '[      ]'}\t 8.{self.l8[-1] if len(self.l8) != 0 else '[      ]'}\t 9.{self.l9[-1] if len(self.l9) != 0 else '[      ]'}
            ====================
            空槽位：{self.space_l}
            ====================
            请输入1~9将相应的羊放入空槽位:
            '''
        ch = input(lay)
        if ch == '1':
            self.select(self.l1)
```
然后再让我们来看选择界面的核心代码，l为一个列表，通过列表的长度来判断选择是否合理。
```python
def select(self, l: list):
        if len(l) == 0:
            print('当前位置已经没有羊了，请重新选择！')
            return
        tmp_l = l.pop()
        if tmp_l not in self.space_l:
            self.space_l[self.space_l.index([])] = tmp_l
        else:
            self.space_l.insert(self.space_l.index(tmp_l), tmp_l)
            self.space_l.pop()
        if self.space_l.count(tmp_l) == 3:
            for i in range(3):
                self.space_l.remove(tmp_l)
                self.space_l.append([])

```
让我们来编写核心的生成代码，首先运用面向对象编程，创建‘Yang’类，再通过pool列表创建所有的小羊，利用random函数随机选择小羊放入牌局供玩家选择。
```python
class Yang:
    space_l = [[], [], [], [], [], [], []]

    def __init__(self) -> None:
        self.generate()
        self.check()

    def generate(self):
        '''生成牌局'''

        pool = ['白羊', '黑羊', '黄羊', '蓝羊', '花羊', '粉羊', '大羊', '小羊']

        self.l1 = [random.choices(pool) for i in range(3)]
        self.l2 = [random.choices(pool) for i in range(3)]
        self.l3 = [random.choices(pool) for i in range(3)]
        self.l4 = [random.choices(pool) for i in range(3)]
        self.l5 = [random.choices(pool) for i in range(3)]
        self.l6 = [random.choices(pool) for i in range(3)]
        self.l7 = [random.choices(pool) for i in range(3)]
        self.l8 = [random.choices(pool) for i in range(3)]
        self.l9 = [random.choices(pool) for i in range(3)]

    def check(self):
        '''判断：如果出现无解的情况则重新洗牌'''
        x = True

        while x:
            x = False

            sum_l = self.l1 + self.l2 + self.l3 + self.l4 + \
                    self.l5 + self.l6 + self.l7 + self.l8 + self.l9
            for i in sum_l:
                if sum_l.count(i) % 3 != 0:
                    x = True
                    self.generate()
                    break

```

记得关注我，每天学习一点点
<a name="gIjCj"></a>
# **你觉得这个系统核心还能做什么？**

**全网可搜：小院里的霍大侠， 免费获取简单易懂的实战编程案例。编程/就业/副业/创业/资源。**<br />私微信：huodaxia_xfeater<br />二维码： [http://www.yougexiaoyuan.com/images/weixin_huodaxia.jpg](http://www.yougexiaoyuan.com/images/weixin_huodaxia.jpg)<br />公众号：有个小院（微信公众号：yougexiaoyuan）<br />github：yougexiaoyuan (视频源码免费获取)<br />（部分素材来源于互联网，如有保护请联系作者）
