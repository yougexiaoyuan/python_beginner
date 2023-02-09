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

