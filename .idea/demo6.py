
import os;
from tkinter import *
import tkMessageBox
#print(os.listdir())
""""
dir = os.listdir();

for x in dir :
    print(x)
"""


root = Tk();

#label = Label(root,text='python　script is best language');
#label.pack()

#label = Message(root,text='数据验证错误');

#label.pack();

def alerts():
    tkMessageBox.showinfo("操作提示", "是否要删除？");


button = Button(root,text='删除',command=alerts);
button.pack();
root.mainloop();