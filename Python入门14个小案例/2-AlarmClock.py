#小院里的霍大侠 - 兴趣编程
#案例 - 定时播报
#学习点： 
#from 方法类名字 import 类库 这个通常在开头声明代表调用这个类库中的内容   
#字符串分割取值：alarm_time[0:2]代表获取字符串的前2个字符
#datetime.now()：代表获取当前的系统时间
#now.strftime("%H")：代表获取当前时间的小时，%M是获取分钟，%S获取秒
#while True:：while代表要下面代码循环；连起来True就是一直循环的意思，知道break然后跳出中断
#playsound('music.mp3')：代表播放这个音乐，头部已经导入了这个类库

from datetime import datetime   
from playsound import playsound
alarm_time = input("请设置定时播报的时间:HH:MM:SS\n")
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