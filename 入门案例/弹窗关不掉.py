from tkinter import * 
class YouLikeMe:
    def __init__(self):
        window=Tk()
        label=Label(window,text='你是不是喜欢我？')
        self.btyes=Button(window,text='不是',height=1,width=6)
        self.btno=Button(window,text='是的',height=1,width=6)
        label.place(x=60,y=70)
        self.btyes.place(x=40,y=130)
        self.btno.place(x=120,y=130)
        self.btyes.bind('<Enter>',self.event1)#将按钮与鼠标事件绑定，<Enter>是指鼠标光标进入按钮区域
        self.btno.bind('<Enter>',self.event2)
        window.mainloop()
    def event1(self,event):#切换按钮文字
        self.btyes['text']='是的'
        self.btno['text']='不是'
    def event2(self,event):
        self.btyes['text']='不是'
        self.btno['text']='是的'
        
YouLikeMe()
window=Tk()
label=Label(window,text='关闭窗口也改变不了你喜欢我的事实')
label.place(x=2,y=80)
button=Button(window,text='确定',command=window.destroy)
button.place(x=80,y=150)
window.mainloop()
