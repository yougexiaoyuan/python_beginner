from tkinter import * 
class YouLikeMe:
    def __init__(self):
        window=Tk()
        label=Label(window,text='���ǲ���ϲ���ң�')
        self.btyes=Button(window,text='����',height=1,width=6)
        self.btno=Button(window,text='�ǵ�',height=1,width=6)
        label.place(x=60,y=70)
        self.btyes.place(x=40,y=130)
        self.btno.place(x=120,y=130)
        self.btyes.bind('<Enter>',self.event1)#����ť������¼��󶨣�<Enter>��ָ�������밴ť����
        self.btno.bind('<Enter>',self.event2)
        window.mainloop()
    def event1(self,event):#�л���ť����
        self.btyes['text']='�ǵ�'
        self.btno['text']='����'
    def event2(self,event):
        self.btyes['text']='����'
        self.btno['text']='�ǵ�'
        
YouLikeMe()
window=Tk()
label=Label(window,text='�رմ���Ҳ�ı䲻����ϲ���ҵ���ʵ')
label.place(x=2,y=80)
button=Button(window,text='ȷ��',command=window.destroy)
button.place(x=80,y=150)
window.mainloop()
