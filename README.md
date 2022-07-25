欢迎来的我的小院，跟着我每天学习一点点，让你不在枯燥，不在孤单......




# **前言 - 兴趣编程六步学习法**

曾经何时我也经历过学编程的痛苦过程，不断的语法学习，所谓高级的知识点的学习，结果大多根本用不到，然后被忘的一干二净。

![joshua-earle-ICE__bo2Vws-unsplash.jpg](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b44176c5e90e4e38ad5fa16d2e9fe580~tplv-k3u1fbpfcp-zoom-1.image "joshua-earle-ICE__bo2Vws-unsplash.jpg")

编程对于大多初学者是一门耗时长，枯燥，无法坚持的技术。 我在计算机互联网行业混迹了20年，不能说是超级大牛吧，但也小有所成。做过程序员，项目经理，咨询顾问，到现在互联网创业，重要的是我一直对编程教育非常感兴趣，喜欢帮助一些新手快速上路。

![npzTh6Jv2zJoh3PbF91hqA.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/641995ab04574b2aa97d230200bfbc48~tplv-k3u1fbpfcp-zoom-1.image "npzTh6Jv2zJoh3PbF91hqA.png")

所以在不断研究探索的路上， 总结了一套入门学习的编程的理论，核心概念很简单，就是要源于兴趣，坚持实践。 也就是所谓的兴趣编程，我将会在这里教大家怎样编程，跟着我每天学习一点点，从你的兴趣点出发，坚持实践，可以让你拥有意想不到的效果！

大概得学习逻辑就是下面的六步法，点击这里可以了解更多。

<https://developer.aliyun.com/article/924592?spm=a2c6h.13148508.setting.16.eef04f0eGPPIhB>

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/690d14bdc8f6446fa0f2befb286b3c33~tplv-k3u1fbpfcp-zoom-1.image "image")




#

# **Python初学者：搭建开发环境**

欢迎来的我的小院儿，这里会用兴趣编程方法跟大家一起学习编程。这个视频来学习Python初学者案例-VS Code环境搭建，教大家快速搭建Python开发环境，快速进入实战。跟着我一起学习，不在枯燥，不在孤单......

-   下载Visual Studio Code安装，<https://code.visualstudio.com/>

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28bc3b0fdc74489fbc1eeae8df02f231~tplv-k3u1fbpfcp-zoom-1.image "image")

-   下载Python，<https://www.python.org/downloads/>

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2cdc321b4574eae9c0d814b61424f06~tplv-k3u1fbpfcp-zoom-1.image "image")

-   安装vs code的基本插件

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc31f82702254030af1290dff39a4a64~tplv-k3u1fbpfcp-zoom-1.image "image")

-   配置Python环境变量。可以点击左侧的小齿轮，然后点击Extension Settings，在红框中输入你的Python安装地址，如果打开已经存在则忽略这一步。

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5995c1fd8514303a4b6a9731ad6140c~tplv-k3u1fbpfcp-zoom-1.image "image")

-   Python安装包操作，镜像源更换

这里主要是把国外网站的地址换成阿里云的，这样国内开发时候速度比较有保障。

建议直接把全局变量换成阿里云地址。

进入C:Users你的系统用户名pippip.ini，把下面代码替换全部复制进去。

```
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```




注意：如果没有上面的pip文件夹，则直接创建一个pip文件夹，并且在下面创建pip.ini文件，把内容复制进去即可。

记住pip install 都需要在系统cmd中输入。右键点击左下角开始菜单，在弹出菜单中选择

Windows PowerShell（管理员)

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/572e50df28ae413ebb9e604f015b14f9~tplv-k3u1fbpfcp-zoom-1.image "image")

如果想临时用阿里云则按如下操作：

```
pip install -i https://mirrors.aliyun.com/pypi/simple/ 包名
```




以后都使用阿里云的源

```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```




取消设置

```
pip3 config unset global.index-url
```




-   开始你的第一个Python代码

到这里可以试着在vs code中试着创建一个hello wold 的代码文件，运行调试感受下代码的魅力。如果不知道怎么操作，可以看看微软官方这篇文章是否可以跟着做起来，加油。

<https://code.visualstudio.com/docs/python/python-tutorial>

<https://code.visualstudio.com/docs/languages/python>




![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49522f4ea7d74b0bbb08765bea03b27e~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例一：获取首字母**

欢迎来的我的小院儿，这里会用兴趣编程方法跟大家一起学习编程开发。这个视频可以学习到一些入门的python语法知识，逐步由浅入深，跟着我一起学习，不在枯燥，不在孤单......

## **案例：获取首字母**

获取输入内容的首字母。

## **演示**

我们输入I like you 回车，可以看到程序输出了ILY的开头大写字母。

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e70e75c335c2405094fa9dc120956293~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 获取单词首字母
user_input = str(input("请输入一串单词（用空格分割字母单词）: "))
text = user_input.split() #用空格来分割输入的内容
a = " " #声明一个变量
for i in text:  #一个循环语法，这里是根据上面输入文本分割后得到数量
    a = a+str(i[0]).upper() #分割后每个字符大写相连
print(a)  #输出结果
```

这里我先来梳理下代码，首先接受一个字符串用户输入，然后我使用 Python 中的 split() 函数来分割句子。接着声明了一个新变量“a”来存储短语的首字母缩写词。

最后，我在代表用户输入拆分的变量“文本”上运行 for 循环。在运行 for 循环时，我们存储拆分后每个单词的 str[0] 的索引值，并使用 upper() 函数将其转换为大写格式。

#学习点：

#str()：是把括号里面内容变成一段字母文字，转换成字符串

#split()：是将括号中字符分割成字符串，如果不指定则默认用空格分割

#print()：输出结果信息

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/faa4b0acce6e4e2881780561fd80716b~tplv-k3u1fbpfcp-zoom-1.image "image")

这是一个很棒的 python 程序来测试你的逻辑思维能力，学习编程会敲代码不是最重要的，最重要的是逻辑分析能力，和事务抽象的能力，跟着我学习慢慢你就明白了。




![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d89825940d35498c86cf79cac30d2f5f~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例二：定时播报**




欢迎来的我的小院儿，这里会用兴趣编程方法跟大家一起学习编程开发。这个视频可以学习到一些入门的python语法知识，逐步由浅入深，跟着我一起学习，不在枯燥，不在孤单......

## **案例：定时播报**

在规定的时间内播放一个音乐或者闹铃声音。

## **演示**

本案例首先让你输入一个时分秒和上下午标志的数值，我们输入一个数值，然后回车，程序出现正在设置定时播报，这里程序等待系统时间到达你指定时间后就播放你提前预设的音乐，我们听到我这里设置了一首爵士乐。

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28fbe410c7b241d192a12049403adc65~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 定时播报
from datetime import datetime   
from playsound import playsound
alarm_time = input("请设置定时播报的时间:HH:MM:SSn")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()#这里upper()是获取字符大写形式
print("正在设置定时播报......")
while True:
    now = datetime.now()
    current_hour = now.strftime("%H")#这里默认是24小时，I是12小时模式
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("开始播放")
                    playsound('music.mp3')
                    break
```

我们接着来分析源码，前2行是导入日期库和音乐库函数。DateTime 模块预装在 Python 编程语言中，因此您可以轻松地将其导入程序中。playsound 库可以使用 pip 命令轻松安装。

接着我们通过尖括号功能来取值字符串，其中0:2代表获取字符串前2个字符，我们分别获取了字符串时，分，秒和时间标志位。

当用户输入后，我们提示正字设置定制播报。

接下来通过一个while循环来判断是否系统时间到达了我们预设输入的时间。如果到达了，我们就打印开始播放文字，然后播放指定音乐，音乐播放完毕通过break跳出程序。

#学习点：

#from 库名字 import 库函数 这个通常在开头声明代表调用这个类库中的内容

#字符串分割取值：alarm_time[0:2]代表获取字符串的前2个字符

#datetime.now()：代表获取当前的系统时间

#now.strftime("%H")：代表获取当前时间的小时，%M是获取分钟，%S获取秒

#while True:：while代表要下面代码循环；连起来True就是一直循环的意思，知道break然后跳出中断

#playsound('music.mp3')：代表播放这个音乐，头部已经导入了这个类库

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbe0e62b035749a8904f06b656f719f3~tplv-k3u1fbpfcp-zoom-1.image "image")

播放音乐，播放视频，这些都是可以通过编码来实现的，到这里你是不是会发现你平时手机闹铃的工作原理也是如此，来试着自己编写一个定时播报功能，来提醒你的生活和工作吧。




![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4a2a2da2eac4cafb832df6949445f5a~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例三：邮箱分割器**

欢迎来的我的小院儿，这里会用兴趣编程方法跟大家一起学习编程开发。这个视频可以学习到一些入门的python语法知识，逐步由浅入深，跟着我一起学习，不在枯燥，不在孤单......

## **案例：邮箱分割器**

这个案例主要是把邮箱地址分割出用户名，和使用邮箱的域名地址。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fff5d891a32140858f856712408cbadb~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 邮箱分割器
email = input("请输入你的Email地址: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"您的邮箱用户名： '{username}' ， 您的邮箱域名：'{domain_name}'")
print(format_)
input()
```




上面的代码非常简单易懂。我们接受用户输入并同时使用 strip 函数来删除空格（如果有的话）。然后我们找到用户输入的'@'符号的索引。然后我们将索引存储到一个名为 domain_name 的变量中，以将电子邮件分成两部分；用户名和域。

最后，我们只是格式化以打印输出。根据您的需要，可以通过更多想法来增强上面的代码。

#学习点：

#strip()：strip 函数来删除空格

#.index("@")：是对字符串中@字符进行分割

# (f"hi,"{xxx})：其中f代表对括号中字符串格式化，里面的大括号可以用变量替换，这样就可以动态输出内容了

**思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32bae40ab1514e1aa2885e039133213c~tplv-k3u1fbpfcp-zoom-1.image "image")

作为初学者，您必须尝试这些类型的程序来提高您的编码技能。从长远来看，它还将帮助您构建算法并提高您的逻辑思维能力。




![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee1a65b2de6a424a8035da89e92f6fc7~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例四：故事机**

欢迎来的我的小院儿，我会用兴趣编程的方法论跟大家一起学习编程开发。这个视频可以学习到一些入门的python语法知识，逐步由浅入深，跟着我一起学习，不在枯燥，不在孤单......

## **案例：故事机**

提前写好一些故事片段，然后通过随机数的代码功能，把故事串联整合起来，形成一个完成的故事。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/542c823f89ed4a64ab0f95589bf9dafa~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 故事机
#学习点： 
#random：导入随机类
#random.choice()：用随机函数随机生成字符
import random
when = ['20年前', '昨天', '前天晚上', '很久很久之前','在未来的某一天']
who = ['美女', '老人', '帅哥', '小孩','老外']
name = ['张三', '李四','王五', '赵六', '孙七']
residence = ['北京','上海', '广州', '深圳', '重庆']
went = ['图书馆', '电影院','公园', '餐厅', '商场']
happened = ['捡到一分钱','下起了大雨', '发现了一个秘密', '帮助了一个老人', '摔了一个跟头']
print(random.choice(when) + '，一个来自'+ random.choice(residence) +'，叫'+random.choice(name)+'的人'  + ', 去了' + random.choice(went) + ' ，在去的路上'+ random.choice(happened)+'。')
input()
```




本案例主要是通过导入random的类库，通过把故事结构分拆，然后定义每个分拆片段的内容，通过随机的概念，组成一个小故事。代码很容易理解，我就在这里多说了。

#学习点：

#random：导入随机类

#random.choice()：用随机函数随机生成字符

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96be6ce608464aa3a0a55789482ceb12~tplv-k3u1fbpfcp-zoom-1.image "image")

是不是很有趣哦，这样一个随机故事就生成了。应该可以体会到从程序自动化的魅力了吧，现在很多大数据分析等等，都是类似的道理，通过大量数据，多种算法和逻辑来落地到不同的行业，帮助人们自动化处理各种业务。

通过这个案例，能启发到你嘛？你是不是见过某些APP有类似的场景！







![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83392c54e41044df80ee3d122f955aa8~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例五：随机生成密码**

欢迎来的我的小院儿，我会用兴趣编程的方法论跟大家一起学习编程开发。这个视频可以学习到一些入门的python语法知识，逐步由浅入深，跟着我一起学习，不在枯燥，不在孤单........

## **案例：随机生成密码**

本案例通过提取指定的一堆数字，字母，符号中随机生成指定长度的数值的字符作为密码。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47f1d320243a4deeab6c15827cad3360~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 随机生成密码
import random
passlen = int(input("请输入你要生成的密码长度："))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(s,passlen))
print(p)
input()
```




在上面的代码中，我首先在 Python 中导入了 random 模块，然后我要求用户输入密码的长度。然后我存储了在生成密码时要考虑的字母、数字和特殊字符。然后我通过加入密码长度和变量 s 进行随机抽样，最终生成一个随机密码。

#学习点：

#random.sample(s,passlen )：根据输入的数值，随机抓取s字符串的字符，组成输入值长度的数组

#str.join(sequence)：用于将序列中的元素以指定的字符连接生成一个新的字符串。

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1a211f69d9140918f92f9a8afaf2580~tplv-k3u1fbpfcp-zoom-1.image "image")

这样生成密码的方式，是不是很不错！思考下你知道的密码生成方式，有多少种，有兴趣的朋友可以深入学习下密码学，包括现在区块链技术跟密码学都有很大的关系。







![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fffe454bd364b56972071ef1c81baac~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例六：石头剪刀布**

欢迎来的我的小院儿，我会用兴趣编程的方法论跟大家一起学习编程开发。这个视频可以学习到一些入门的python语法知识，逐步由浅入深，跟着我一起学习，不在枯燥，不在孤单......

## **案例：石头剪刀布**

本案例实现了一个石头剪刀布的输入小游戏，用户可以在其中选择石头剪刀布，如果用户获胜，则添加分数，最后当用户完成时游戏，分数显示给用户。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bf2b13686c04486a960f93822516513~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 石头剪刀布
import random
choices = ["剪刀","石头", "布"]
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("请输入- 石头, 布或者剪刀？").capitalize()
    computer = random.choice(choices)
    #这里说游戏的逻辑判断
    if player == computer:
        print("出的一样，重新来")
    elif player == "石头":
        if computer == "布":
            print("你输了哦！", computer, "包住了", player)
            cpu_score+=1
        else:
            print("很棒，你赢了！", player, "敲碎了", computer)
            player_score+=1
    elif player == "布":
        if computer == "剪刀":
            print("你输了哦！", computer, "剪坏了", player)
            cpu_score+=1
        else:
            print("很棒，你赢了！", player, "包住了", computer)
            player_score+=1
    elif player == "剪刀":
        if computer == "石头":
            print("你输了...", computer, "敲碎了", player)
            cpu_score+=1
        else:
            print("你赢了!", player, "剪坏了", computer)
            player_score+=1
    elif player=='查看分数':
        print("最终比分：")
        print(f"电脑分数：{cpu_score}")
        print(f"你的分数：{player_score}")
        break
input()
```




![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c02d5707f5d430397df00c97998adf1~tplv-k3u1fbpfcp-zoom-1.image "image")




要使用 Python 创建石头剪刀布游戏，我们需要获取用户的选择，然后我们需要将其与使用 Python 中的随机模块从选择列表中获得的计算机选择进行比较，如果用户获胜那么分数将增加1。总结下就是代码中通过条件语句和循环语句来对整体游戏逻辑判断，来增加游戏者的分数。

#学习点：

#random.choice()：根据随机数字，随机生成一个数值

#条件语法：学习通过if,else,elif的逻辑条件判断

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/122dd69d336643bb84fdd944c0a03d63~tplv-k3u1fbpfcp-zoom-1.image "image")

我们学习到了一个稍微难一点的案例，加入了条件的逻辑判断，大家可以改造代码练习一些案例，然后会发现条件判断其实很简单哦。比如，你可以做一个龟兔赛跑的小例子，动起手来试试看。




![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f1bf7e671694fe0a0a821ee8a747222~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例七：投掷骰子**

欢迎来的我的小院，跟着我一起学习，不在枯燥，不在孤单......

## **案例：投掷骰子**

本案例是一个投掷骰子的模拟器，程序直接输出结果内容。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af0475c28063409086873a59707529c1~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 投掷骰子
import random
#定义掷骰子的最小值是 1，最大值是 6
min_val = 1
max_val = 6
#定义是否需要循环的标志
roll_again = "是"
#l循环判断
while roll_again == "是" or roll_again == "y":
    print("旋转骰子...")
    print("骰子数字为：")
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    roll_again = input("是否继续投掷骰子？请输入：")
```




我们通过这个案例很好的学到了循环的语法，python的循环等语法要记住缩进模式哦，如果之前会其他语言的话可能会觉得别扭。代码中首先定义骰子最大最小的值，然后通过while循环判断，如果用户不断进行，只要输入是即可，然后会输出随机的数值。

#学习点：

#random.randint()：根据我们指定的开始和结束返回一个随机整数。

#while：循环判断的语法，后面跟着判断的调节，当不满足条件则退出循

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f75730a2079452e905859530f75b361~tplv-k3u1fbpfcp-zoom-1.image "image")

想一想，你还能用循环语法做点什么小案例那？如果你的游戏是一副扑克，你应该怎样设计程序那？







![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/653c5089c144429d8a4138155e2093f6~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例八：问答游戏**

欢迎来的我的小院，跟着我一起学习，不在枯燥，不在孤单......

## **案例：问答游戏**

本案例的游戏是向玩家询问有关问题。他们有 3 次机会回答您不想让测验太难的每个问题。每个正确答案都会得分。游戏结束时，程序会显示玩家的最终得分。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/636cced3deb44897aeed50db46dfb4a4~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 问答游戏
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("答案正确。")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("答案错误了，请重试。")
            attempt = attempt + 1
    if attempt == 3:
        print("正确答案是：",answer )
    
score = 0
print("请回答下面问题：")
guess1 = input("你觉得学编程有好处吗？ ")
check_guess(guess1, "有")
guess2 = input("你觉得学编程容易吗？ ")
check_guess(guess2, "容易")
guess3 = input("你觉得多长时间可以入门Python？")
check_guess(guess3, "1个月")
print("你的分数为："+ str(score))
```




这个问答游戏使用一个函数功能，它是具有执行特定任务的名称的代码块。一个函数允许您多次使用相同的代码，而不必每次都键入所有内容。Python 有很多内置函数，但它也允许您创建函数。

我们通过提取定义一个检查游戏结果的函数。通过用户输入的结果来调用函数，函数完成检查，输出结果，完成游戏过程。

#学习点：

#def：def是声明一个函数方法的语法。函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

deffunctionname(parameters):

"函数的逻辑代码"

return[expression]

#while：循环判断的语法，后面跟着判断的调节，当不满足条件则退出循环。

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/552d22ecebf2463a9147ce01465ed50e~tplv-k3u1fbpfcp-zoom-1.image "image")

函数方法是编程的核心点，通过定义函数，调用函数可以更好组织代码，你觉得函数对于编程都有哪些好的体现？代码便于阅读？代码更好的组织？

你可以试试定义2个函数，每个函数实现相反的逻辑功能，然后通过随机数来调用2个不同函数，这样是不是很有趣哪！







![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/158b50da9e6e46d6a985d0ab3b8b0ccb~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例九：生成二维码**

欢迎来的我的小院，跟着我一起学习，不在枯燥，不在孤单......

## **案例：生成二维码**

本案例相信大家都很熟悉，其英文名称为QR是 Quick Response 的缩写。今天教大家怎样用代码生成二维码，因为平台限制二维码原因，这里不展示具体图形。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/961eaa96f92f48279c0bda75389cfd7d~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 生成二维码
 
# 二维码其实都是一个网络地址生成的
s = "https://www.xfeater.com"
# 这个是二维码类库的创建二维码方法
url = pyqrcode.create(s) 
# 生成图形文件保存，可以是png,jpg等
url.svg("my_qr_code.png", scale = 8) 
print("一个my_qr_code.png的二维码图片文件已经生成到你的代码目录")
input()
```




代码中主要是通过调用二维码类库，创建二维码链接，然后保存为本地图片。

#学习点：

#pyqrcode：生成二维码的函数库

#import：导入类库语法可以用import,和from ... import

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad38376f5f3d4aa78b6df7686f76d742~tplv-k3u1fbpfcp-zoom-1.image "image")

二维码现实生活中有很多用处：

1 扫码支付

2 扫码下载APP

3 扫码加好友

4 扫码填表格

5 扫码进网站

......

太多了，这些都是基于一个逻辑实现的，就是二维码其实就是网络的一个地址，二维码主人就是这个地址的邀请人，明白了吧。

你觉得二维码还有那些应用，还能做什么？







![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99b0ca8409b24a2087f3ee3e07746f14~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）










# **Python初学者案例十：打印彩色文本**

欢迎来的我的小院，跟着我一起学习，不在枯燥，不在孤单......

## **案例：打印彩色文本**

本案例使用Colorama颜色类库来输出彩色的文本内容。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d640ab6d8bdd4e1eb2ec5eb8726ae91c~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 打印彩色文本
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)#初始化，设置自动恢复
print(Fore.BLUE+Back.YELLOW+"大家好，我的名字叫霍大侠。 "+ Fore.YELLOW+ Back.GREEN+"我梦想有个小院，院子里有一群朋友为了共同兴趣学习交流。")
print(Back.LIGHTBLUE_EX+"今天在我的小院，希望有兴趣朋友和我一起学习编程")
print(Fore.RED + Back.RED+ "和大家一起，每天学习一点点，编程改变自己，改变世界！")
input()
```




使用 Colorama 模块，我们可以使用 Python 打印彩色文本。我们可以使用它并调用它的内置变量，这些变量是所需 ANSI 代码的别名。这使我们的代码更具可读性，并且在脚本开始处调用 colorama.init() 后与 Windows 命令提示符一起工作得更好。

Colorama 模块提供三个主要格式选项：前、后和样式。这些允许我们更改前景或背景文本的颜色和样式。可用于前景和背景的颜色有黑色、红色、绿色、黄色、蓝色、洋红色、青色和白色。

#学习点：

#colorama：这个模块类库主要功能是显示字体不同的颜色和背景

#Fore, Back, Style：Fore是针对字体颜色，Back是针对字体背景颜色，Style是针对字体格式

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdc1c5bd3ba546c3a066228afa6e657c~tplv-k3u1fbpfcp-zoom-1.image "image")

有了颜色，世界都丰富多彩了，是吧！

通过本案例学习，大家可以通过颜色来渲染输出文字图形的颜色。

快来制作你的颜色程序吧！










![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a2e7078963245c196703d897c173c5d~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例十一：BMI计算器**

欢迎来的我的小院，跟着我一起学习，不在枯燥，不在孤单......

## **案例：BMI计算器收**

BMI是基于个人的体重和身高的相对体重的量度。今天，体重指数通常用于将人分类为体重不足、超重，甚至肥胖。此外，它被各国采用以促进健康饮食。

BMI可以被认为是直接测量体脂的替代方法。此外，BMI 是一种廉价且易于执行的筛查可能导致健康问题的体重等级的方法。

体重指数的计算方法是将一个人的体重（公斤）除以身高（米），然后再除以他们的身高。

今天我们来做一个BIM计算器。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d27d57dbd18f4035823a8226eb89f0bc~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 -  BMI计算器
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
```




代码中根据用户输入的身高和体重参数，进行BMI公式运算后，逻辑判断得出数值是否正常。

相信大家都能看懂代码，记住依次顺序为获取参数，公式计算，逻辑判断，得出结果。

#学习点：

#BMI：体重指数的计算方法是将一个人的体重（公斤）除以身高（米），然后再除以他们的身高。

#float：代表对范围数值进行浮点求值

#if,else,elif：条件逻辑判断，一定要理解哦。

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/960c0204615f49d0814c9f998a961ca5~tplv-k3u1fbpfcp-zoom-1.image "image")

BMI计算器是不是很简单，想想你能做出什么计算器？你是否可以编写一个计算血压，血脂，或者饮食健康的计算器那？







![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a38f3b7447eb4981b69b42dc73d04c88~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# **Python初学者案例十二：温度单位转换**




欢迎来的我的小院，跟着我一起学习，不在枯燥，不在孤单......

## **案例：温度单位转换**

本案例使用 Python 编程语言将华氏温度转换为摄氏温度。用户输入华氏度，输出摄氏度。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2162e38463604c0ca3d727c1207383a8~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 温度单位转换
def convert(s):
    f = float(s)
    c = (f - 32) * 5/9#摄氏温标（°C）和华氏温标（°F）之间的换算关系为：F=C×1.8+32；C=(F-32)÷1.8
    return c
con = input("请输入要兑换的华氏度：") 
print(convert(con))
input()
```




世界上大多数国家都使用摄氏度来表示温度，但美国仍然使用华氏度。在本文中，我将带您完成一个非常简单的程序，适合初学者使用 Python 编程语言将华氏温度转换为摄氏温度。

计算温度转换很简单。我们必须转换温度，因为摄氏和华氏的起点不同；0摄氏度是32华氏度。因此，要将华氏温度转换为摄氏度，我们只需要从华氏温度中减去 32。

有时单位的大小也不同。摄氏将水的冰点和沸点之间的温度范围划分为 100 度，而华氏则将此范围划分为 180 度，所以我还将该值乘以 5/9 以将 180 度转换为 100。

#学习点：

#def：def是声明一个函数方法的语法。函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

#float()：函数用于将整数和字符串转换成浮点数。

#摄氏温标（°C）和华氏温标（°F）之间的换算关系为：F=C×1.8+32；C=(F-32)÷1.8

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/702d43ef18554c5fa90dd1600166b121~tplv-k3u1fbpfcp-zoom-1.image "image")

生活中还有那些换算单位很让你头疼，你可以编一个小程序试试看，解决下你的烦恼。







![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10c6462f6ca1454f9483545178562dc2~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）










# **Python初学者案例十三：用户多次输入**

欢迎来的我的小院，跟着我一起学习，不在枯燥，不在孤单......

## **案例：用户多次输入**

本案例用户通过多次输入输出文字展示，输入“停止”汉字退出。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b2efdef26f84b02b1a23115d8087f6a~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 用户多次输入
while True:
    reply = input("请输入文本：")
    if reply == '停止': break
    print(reply)
input()
```




该代码利用 Python while 循环，这是 Python 最通用的循环语句。内置输入函数在这里用于一般控制台输入，它打印其可选参数字符串作为提示，并将用户输入的响应作为字符串返回。

此处还出现了一个使用嵌套块的特殊规则的单行 if 语句。if 语句的主体出现在冒号后面的标题行上，而不是在下面的新行上缩进。

最后，Python break 语句用于立即退出 while 循环语句。它只是跳出while循环语句，程序在循环后继续。如果没有这个退出语句，while 将永远循环，因为它的测试仍然为真。

#学习点：

#while：while 循环，这是 Python 最通用的循环语句。

#break：break 语句用于立即退出 while 循环语句。

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d418f994889a4f82ac6cd7f1101739fd~tplv-k3u1fbpfcp-zoom-1.image "image")

你是否可以利用用户多次输入，循环写一个分析程序，根据多次输入的结果，判断他的人格，然后给出一个分析展示，比如他是外向，内向等等。




![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da9e0206917e4c16b84ce2c349927809~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）







# Python初学者案例十四：数字转换

欢迎来的我的小院，跟着我一起学习，不在枯燥，不在孤单......

## **案例：数字转换**

本案例通过预设映射关系的字符库，把罗马数字转换成阿拉伯数字。首先输入罗马字符，比如V，D，VII等，看看结果会出现什么。

## **演示**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a94bbda17279498abd3f73db75a45cac~tplv-k3u1fbpfcp-zoom-1.image "image")

## **学习**

```
#小院里的霍大侠 - 兴趣编程
#案例 - 罗马数字转阿拉伯数字
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
```




所以我们需要按照上面的逻辑编写一个程序，用 Python 将罗马数字转换为小数。那么我们来看看罗马数字转小数的过程：

1.  从左到右遍历罗马数字字符串，一次检查两个相邻的字符。如果需要，您还可以指定循环的方向，但只要相应地实施比较就没有关系。
1.  如果左侧的值高于右侧的值，则从最终值中减去该位置的计数。否则，只需添加它。
1.  该过程完成后，最终值是与罗马数字等效的十进制值。

这是一个综合案例，结合了定义函数；调用函数；循环判断；数组；字符格式等语法知识。

#学习点：

#for：for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

#range：range返回一个序列的数; len() 返回列表的长度，即元素的个数。

#str(x)：str把数值转换成字符串输出。

## **思考**

![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b14ede1d5c47cba6779e829b2da5cb~tplv-k3u1fbpfcp-zoom-1.image "image")

本次案例综合了之前的很多语法知识，学到这里，你都能跟上吗，是不是感觉自己很厉害了，学无止境，继续加油。

通过十四个小案例，我们学会了基础的python语法知识，也明白了一些编程对我们生活的含义。

有兴趣的朋友可以继续跟着我学习，在我的小院里，我会逐步由浅入深地带着大家一点一点学习编程，只要你坚持不懈，相信3-6个月你就能基本掌握Python这门编程语言，而且能了解到编程的更多知识，包括互联网技术，逻辑知识，甚至可以开始用编程技术改善生活。

我们后续会不断推出多门编程语言的入门学习和实战案例，还有怎样编程赚钱等等。

非常适合有兴趣的初学者，或者在校学生，或者想通过编程求职高薪的朋友们。




![image](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9db85120ed2e43fd9aacbde7fc0291e0~tplv-k3u1fbpfcp-zoom-1.image "image")

（部分素材来源于互联网，如有保护请联系作者）
