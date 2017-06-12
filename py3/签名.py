from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='姓名',font=("微软雅黑",20),fg="red",bg="#00ff00",width=10,height=20)
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
# 初始化
app = Application()
# 设置窗口标题:
app.master.title('python签名设计')
# 主消息循环:
app.mainloop()
