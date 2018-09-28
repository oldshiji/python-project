import wx

APP_EXIT = 1
class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        #menubar = wx.MenuBar()
        #filemenu = wx.Menu()

        #filemenu.Append(wx.ID_EXIT,'File','Quit')
        #qmi = wx.MenuItem(filemenu,APP_Menu_Id,"&File\tfiles+f");
        #qmi.SetBitmap(wx.Bitmap('file.png'))
        #filemenu.AppendItem(qmi)

        #menubar.Append(filemenu,'&File')

        #self.SetMenuBar(menubar)

        #self.Bind(wx.EVT_MENU, self.OnQuit, filemenu)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('file.png'))
        fileMenu.AppendItem(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)


        self.SetSize((300, 200))
        self.SetTitle('Menu')
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