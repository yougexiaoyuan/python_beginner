
![BMI计算器-竖(1)-封面.jpg](https://cdn.nlark.com/yuque/0/2022/jpeg/34388852/1669772135628-2eefb9d3-0676-41c0-83c1-eda5a756a082.jpeg#averageHue=%23e4f1e5&clientId=u446dc9a6-a29b-4&crop=0&crop=0&crop=1&crop=1&from=ui&id=uad936e19&margin=%5Bobject%20Object%5D&name=BMI%E8%AE%A1%E7%AE%97%E5%99%A8-%E7%AB%96%281%29-%E5%B0%81%E9%9D%A2.jpg&originHeight=1920&originWidth=1080&originalType=binary&ratio=1&rotation=0&showTitle=false&size=135769&status=done&style=none&taskId=ub6ba8884-eeb8-47fe-8f03-97e12d9ff3d&title=)
<a name="oxzy6"></a>
# **案例介绍**

欢迎来到我的小院，我是霍大侠，恭喜你今天又要进步一点点了！<br />我们来用Python相关知识，做一个BMI计算器的案例。你可以通过控制台的提示信息，输入身高和体重，注意单位，系统会自动计算出BMI值，然后判断您的健康状况。
<a name="by1ir"></a>
# **案例演示**

运行程序后，我们可以看到控制台输出的提示信息，按要求输入身高体重后，系统自动计算BMI值，然后将判断结果输出。

![](https://cdn.nlark.com/yuque/0/2022/png/34388852/1668995595417-b562b1eb-705c-4cd2-9cda-6f9d38fba201.png#averageHue=%23232323&clientId=u1d899c85-3a87-4&crop=0&crop=0&crop=1&crop=1&from=paste&id=ue08a61b3&margin=%5Bobject%20Object%5D&originHeight=778&originWidth=2299&originalType=url&ratio=1&rotation=0&showTitle=false&status=done&style=none&taskId=u5d620c92-5a50-437d-a06a-be48ed8e4be&title=)
<a name="Po78Y"></a>
# **源码学习**

进入核心代码学习，首先了解到这是一个循环实战，所以使用while循环语句可以实现BMI计算器的重复使用。根据提示信息输入身高体重,float() 函数用于将整数和字符串转换成浮点数。然后程序会用str()函数返回一个对象的string格式。最后根据计算公式得出BMI的数值，用if()函数进行判断，将结果输出给用户。

```python
while True:
    height= (float(input('请输入您的身高(cm):'))/100)
    print('您的身高:'+str(height)+'m')
    weight=(float(input('请输入您的体重(g):'))/2)
    print('您的体重:'+str(weight)+'kg')
    BMI=weight/(height*height)
    print('您的BMI指数为:'+str(BMI))
    if BMI<18.5:
        print('你太苗条了,快吃肉!')
    elif BMI>=18.5 and BMI <24.9:
        print('嗯哼,魔鬼身材,继续保持哦!')
    elif BMI>=24.9 and BMI <29.9:
        print('你的体重有点超标，注意合理饮食哦!')
    else:
        print('你太胖了,快减肥!!!')
        break
```





关注我，跟着我每天学习一点点，让你不在枯燥，不在孤单..
<a name="pVq7i"></a>
# **学会BMI计算器，我瘦了30斤，你信不信?**

**全网可搜：小院里的霍大侠， 免费获取简单易懂的实战编程案例。编程/就业/副业/创业/资源。**<br />私微信：huodaxia_xfeater<br />二维码： [http://www.yougexiaoyuan.com/images/weixin_huodaxia.jpg](http://www.yougexiaoyuan.com/images/weixin_huodaxia.jpg)<br />公众号：有个小院（微信公众号：yougexiaoyuan）<br />github：yougexiaoyuan (视频源码免费获取)<br />（部分素材来源于互联网，如有保护请联系作者）
