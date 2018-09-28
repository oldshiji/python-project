import wx


class MyApplication(wx.Frame):
    def __init__(self,parent,title):
        self(parent,title=title,size=(300,200))
        self.Move((500,200))
        self.Show(True)


App = wx.App(False)

MyApplication(None,'python')

App.MainLoop()

