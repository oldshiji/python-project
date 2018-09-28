import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):


        menuBar = wx.MenuBar()  #创建一个菜单条

        fileMenu = wx.Menu()  #创建一个菜单

        fileMenu.Append(wx.ID_NEW,'新建')　#往这个菜单里添加菜单项　　菜单id　菜单id使用wx内置的属性　　菜单名称　　菜单名称可加&符号实现快捷键功能
        fileMenu.Append(wx.ID_OPEN,'打开')
        fileMenu.Append(wx.ID_CLOSE,'关闭')
        fileMenu.AppendSeparator()   #菜单分隔符

        imp = wx.Menu()
        imp.Append(wx.ID_ANY,'导入word')
        imp.Append(wx.ID_ANY,'导入excel')
        imp.Append(wx.ID_ANY,'导入pdf')

        fileMenu.AppendMenu(wx.ID_ANY,'I&mport',imp)　　#给fileMenu添加一个子菜单


        qmi = wx.MenuItem(fileMenu,wx.ID_EXIT,'&Quit\tCtrl+W')　　#使用wx.MenuItem方法创建一个菜单　　并设置快捷键
        fileMenu.AppendItem(qmi)   #给fileMenu添加一个菜单项　　为qmi


        menuBar.Append(fileMenu,'&文件')  #给菜单条添加菜单　　并设置快捷

        self.SetMenuBar(menuBar)  #将菜单绑定到当前窗口
        self.Bind(wx.EVT_MENU,self.OnQuit,qmi)  #给qmi菜单项设置菜单事件　　产生事件时关闭应用程序


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