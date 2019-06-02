from tkinter import *


class Application(Frame):
    def say_hi(self):
        print("hi there, everyone!")

    def createWidgets(self):

        self.L1=Label(self)
        self.L1["text"]="* 核算账簿"
        self.L1.pack()
        self.E1=Entry(self)
        self.E1["show"]=None
        self.E1.pack()

        self.L2=Label(self)
        self.L2["text"]="* 凭证类别编码"
        self.L2.pack()
        self.E2=Entry(self)
        self.E2["show"]=None
        self.E2.pack()

        self.L3=Label(self)
        self.L3["text"]="* 凭证号"
        self.L3.pack()
        self.E3=Entry(self)
        self.E3["show"]=None
        self.E3.pack()

        self.L4=Label(self)
        self.L4["text"]="* 制单人编码"
        self.L4.pack()
        self.E4=Entry(self)
        self.E4["show"]=None
        self.E4.pack()

        self.L5=Label(self)
        self.L5["text"]="* 制单日期"
        self.L5.pack()
        self.E5=Entry(self)
        self.E5["show"]=None
        self.E5.pack()

        self.L6=Label(self)
        self.L6["text"]="* 人民币"
        self.L6.pack()
        self.E6=Entry(self)
        self.E6["show"]=None
        self.E6.pack()

        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({'side':'left'})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.get_text
        self.hi_there.pack({'side':'right'})

    def get_text(self):

        y1 = Label(root,
                   font=("微软雅黑", 10),
                   text='核算账簿:' + self.E1.get() + '\r'
                        '凭证类别编码:' + self.E2.get() + '\r'
                        '凭证号:' + self.E3.get() + '\r'
                        '制单人编码:' + self.E4.get() + '\r'
                        '制单日期:' + self.E5.get() + '\r'
                        '币种:' + self.E6.get())
        y1.pack()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
root.title("谭诗乐需求系列")
root.geometry('300x500+500+200')
app = Application(master=root)
app.mainloop()
root.destroy()