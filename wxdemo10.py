import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):


        menuBar = wx.MenuBar()  #创建一个菜单条

        fileMenu = wx.Menu()  #创建一个菜单

        fileMenu.Append(wx.ID_NEW,'&新建')
        fileMenu.Append(wx.ID_OPEN,'&打开')
        fileMenu.Append(wx.ID_CLOSE,'&关闭')
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY,'&导入word')
        imp.Append(wx.ID_ANY,'&导入excel')
        imp.Append(wx.ID_ANY,'&导入pdf')

        fileMenu.AppendMenu(wx.ID_ANY,'I&mport',imp)


        qmi = wx.MenuItem(fileMenu,wx.ID_EXIT,'&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)


        menuBar.Append(fileMenu,'&文件')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU,self.OnQuit,qmi)


        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()


if __name__ == '__main__':
    main()