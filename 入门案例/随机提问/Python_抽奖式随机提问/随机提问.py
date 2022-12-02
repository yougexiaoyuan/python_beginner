import tkinter

import tkinter.messagebox

import random

import threading

import itertools

import time

root = tkinter.Tk()

#窗口标题

root.title('随机提问')

#窗口初始大小和位置

root.geometry('260x180+400+300')

#不允许改变窗口大小

root.resizable(False, False)

#关闭程序时执行的函数代码，停止滚动显示学生名单

def closeWindow():

    root.flag = False

    time.sleep(0.1)

    root.destroy()

root.protocol('WM_DELETE_WINDOW', closeWindow)

# 模拟学生名单，可以加上数据库访问接口，从数据库中读取学生名单

students = ['张三', '李四', '王五', '赵六', '李八', '白九']

# 变量，用来控制是否滚动显示学生名单

root.flag = False

def switch():

    root.flag = True    

    while root.flag:

        # 随机打乱学生名单

        t = students[:]

        random.shuffle(t)

        t = itertools.cycle(t)





        

        lbFirst['text'] = lbSecond['text']        

        lbSecond['text'] = lbThird['text']

        lbThird['text'] = next(t)

        time.sleep(0.1)

        

def btnStartClick():

    # 每次单击“开始”按钮启动新线程

    t = threading.Thread(target=switch)

    t.start()

btnStart = tkinter.Button(root, text='开始', command=btnStartClick)

btnStart.place(x=30, y=10, width=80, height=20)

def btnStopClick():
    #单击“停”按钮结束滚动显示
    root.flag=False
    time.sleep(0.3)
    tkinter.messagebox.showinfo('恭喜','本次中奖：'+lbSecond['text'])
btnStop=tkinter.Button(root,text='停',command=btnStopClick)
btnStop.place(x=150,y=10,width=80,height=20)
#用来滚动显示学生名单的3个Label组件
#可以根据需要进行添加，但要修改上面的线程函数代码
lbFirst=tkinter.Label(root,text='')
lbFirst.place(x=80,y=60,width=100,height=20)
#红色Label组件，表示中奖名单
lbSecond=tkinter.Label(root,text='')
lbSecond['fg']='red'
lbSecond.place(x=80,y=90,width=100,height=20)
lbThird=tkinter.Label(root,text='')
lbThird.place(x=80,y=120,width=100,height=20)
#启动tkinter主程序
root.mainloop()