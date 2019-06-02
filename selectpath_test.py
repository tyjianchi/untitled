# _*_ coding:utf-8 _*_

import tkinter
from tkinter import filedialog

class gui_test():
    def openfiles2(self,root):
        s2fname = filedialog.askopenfilename(title='打开Excel文件', filetypes=[('xlsx', '*.xlsx'), ('All Files', '*')])
        l1 = tkinter.Label(root,
                           font=("微软雅黑", 10),
                           text=s2fname)
        l1.pack()

    def getlable(self,root,e1,e2,e3,e4,e5,e6):
        y1 = tkinter.Label(root,
                           font=("微软雅黑", 10),
                           text='核算账簿:'+e1.get()+','
                                '凭证类别编码:'+e2.get()+','
                                '凭证号:'+e3.get()+','
                                '制单人编码:'+e4.get()+','
                                '制单日期:'+e5.get()+','
                                '币种:'+e6.get())
        y1.pack()

    def gui_model(self):
        root = tkinter.Tk()
        root.title("谭诗乐需求系列")
        root.geometry('500x500+500+200')

        btn1 = tkinter.Button(root,
                              text='打开Excel文件',
                              font=("微软雅黑", 10, 'bold'),
                              width=13, height=1, command=self.openfiles2(root))
        btn1.pack()

        l1=tkinter.Label(root,text='* 核算账簿')
        l1.pack()
        e1=tkinter.Entry(root,show=None)
        e1.pack()


        l2=tkinter.Label(root,text='* 凭证类别编码')
        l2.pack()
        e2=tkinter.Entry(root,show=None)
        e2.pack()


        l3=tkinter.Label(root,text='* 凭证号')
        l3.pack()
        e3=tkinter.Entry(root,show=None)
        e3.pack()


        l4=tkinter.Label(root,text='* 制单人编码')
        l4.pack()
        e4=tkinter.Entry(root,show=None)
        e4.pack()

        l5=tkinter.Label(root,text='* 制单日期')
        l5.pack()
        e5=tkinter.Entry(root,show=None)
        e5.pack()

        l6=tkinter.Label(root,text='* 币种')
        l6.pack()
        e6=tkinter.Entry(root,show=None)
        e6.pack()

        btn2 = tkinter.Button(root,
                              text='Refersh',
                              font=("微软雅黑", 10, 'bold'),
                              width=13, height=1, command=self.getlable(root,e1,e2,e3,e4,e5,e6))
        btn2.pack()


        root.mainloop()


tt=gui_test()
tt.gui_model()
