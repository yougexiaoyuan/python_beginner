# 有个小院-兴趣编程

while True:
    height=(float(input('请输入您的身高(cm):'))/100)
    print('您的身高:'+str(height)+'m')
    weight=(float(input('请输入您的体重(g)'))/2)
    print('您的体重:'+str(weight)+'kg')
    BMI=weight/(height*height)
    print('您的BMI指数为:'+str(BMI))
    if BMI<18.5:
        print('你太苗条了，快吃肉!')
    elif BMI>=18.5 and BMI<24.9:
        print('嗯哼，魔鬼身材，继续保持哦!')
    elif BMI>=24.9 and BMI<29.9:
        print('你的体重有点超标，注意合理饮食哦！')
    else :
        print('你太胖了，快减肥!!!')
        break
