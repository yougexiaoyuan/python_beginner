
<a name="XY9gI"></a>
# **案例介绍**
欢迎来的我的小院，我是霍大侠，恭喜你今天又要进步一点点了！<br />我们来用Python编程实战案例，做一个简易的随机提问器。随机提问器主要实现随机，乱序，提取的功能。通过实战我们将学会Python内置tkinter的语法知识。
<a name="ysDmJ"></a>
# **案例演示**
我们点击“开始”，学生名字开始滚动；点击“停”，被抽中的学生将“中奖”<br />![](https://cdn.nlark.com/yuque/0/2022/png/34403478/1669780365391-6cf69334-539c-40c6-b204-57e4627f0e3a.png#averageHue=%23efefef&clientId=u982fa827-bdd0-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ue9ddddbe&margin=%5Bobject%20Object%5D&originHeight=263&originWidth=323&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u674a3c0a-85f0-4664-bce2-eb7a7123a6b&title=)<br />![](https://cdn.nlark.com/yuque/0/2022/png/34403478/1669780364475-7a229c1d-83ab-4932-9a6d-cb4d5da1c8bf.png#averageHue=%23f3f2f2&clientId=u982fa827-bdd0-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ub5f8f943&margin=%5Bobject%20Object%5D&originHeight=462&originWidth=334&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ufa303d87-7f0d-42bb-9b82-26f362d33d1&title=)
<a name="ibEIy"></a>
# **案例设计**
[Python实战案例-随机提问](https://docs.qq.com/mind/DRUVkemJwTGZHV0t4)<br />我们来看此案例的思维导图设计，包括案例描述，页面设计和源码学习。<br />其中源码学习包含了random，time，tkinter三部分代码。<br />![](https://cdn.nlark.com/yuque/0/2022/png/34403478/1669780364390-8a83cf48-8860-4872-b531-d67f19967325.png#averageHue=%23d8e9d2&clientId=u982fa827-bdd0-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ueea99aeb&margin=%5Bobject%20Object%5D&originHeight=692&originWidth=1531&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=ub5d15088-9d13-45e7-b781-ba2639557eb&title=)
<a name="TwBEK"></a>
# **源码学习**
进入核心代码学习，我们先来看利用random的核心代码。该段代码首先创建了学生列表，再利用赋值将该列表的值赋值给t，最后利用random.shuffle()函数对该列表进行乱序。
```python
students = ['张三', '李四', '王五', '赵六', '周七', '钱八']

# 变量，用来控制是否滚动显示学生名单

root.flag = False

def switch():

    root.flag = True    

    while root.flag:

        # 随机打乱学生名单

        t = students[:]

        random.shuffle(t)

        t = itertools.cycle(t)
```
然后我们来编写核心的tkinter代码，通过btnStop.place用来滚动显示学生名单的3个Label组件，然后利用红色Label组件，表示中奖名单。
```python
def btnStopClick():

    # 单击“停”按钮结束滚动显示

    root.flag = False

    time.sleep(0.3)

    tkinter.messagebox.showinfo('恭喜', '本次中奖：'+lbSecond['text'])

btnStop = tkinter.Button(root, text='停', command=btnStopClick)

btnStop.place(x=150, y=10, width=80, height=20)

# 用来滚动显示学生名单的3个Label组件

# 可以根据需要进行添加，但要修改上面的线程函数代码

lbFirst = tkinter.Label(root, text='')

lbFirst.place(x=80, y=60, width=100, height=20)

# 红色Label组件，表示中奖名单

lbSecond = tkinter.Label(root, text='')

lbSecond['fg'] = 'red'

lbSecond.place(x=80, y=90, width=100, height=20)

lbThird = tkinter.Label(root, text='')

lbThird.place(x=80, y=120, width=100, height=20)

# 启动tkinter主程序

root.mainloop()

```
<a name="NLlOQ"></a>
# **总结思考**
**学习点**<br />1、time.sleep(secs)：位于 time 模块中的 sleep (secs) 函数，可以实现令当前执行的线程暂停 secs 秒后再继续执行
```python
 # 单击“停”按钮结束滚动显示

    root.flag = False

    time.sleep(0.3)

    tkinter.messagebox.showinfo('恭喜', '本次中奖：'+lbSecond['text'])

```
2、threading：提供了一个比thread模块更高层的API来提供线程的并发性，这些线程并发运行并共享内存
```python
# 每次单击“开始”按钮启动新线程

    t = threading.Thread(target=switch)

    t.start()

```
3、Itertools：Python中，迭代器（Iterator）是常用来做惰性序列的对象，只有当迭代到某个值的时候，才会进行计算得出这个值
```python
t = itertools.cycle(t)

        # 滚动显示

```


**问答**<br />1、time.sleep(secs）可以实现令当前执行的线程暂停 secs 秒后再继续执行对吗？<br />2、threading是用来实现并发操作的吗？

关注我，跟着我每天学习一点点，让你不再枯燥，不再孤单..

**全网可搜：小院里的霍大侠， 免费获取简单易懂的实战编程案例。编程/就业/副业/创业/资源。**<br />私微信：huodaxia_xfeater<br />二维码： [http://www.yougexiaoyuan.com/images/weixin_huodaxia.jpg](http://www.yougexiaoyuan.com/images/weixin_huodaxia.jpg)<br />公众号：有个小院（微信公众号：yougexiaoyuan）<br />github：yougexiaoyuan (视频源码免费获取)<br />（部分素材来源于互联网，如有保护请联系作者）
