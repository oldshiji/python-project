import wx

""""
app = wx.App()
frame = wx.Frame(None,-1,'文本')
frame.Show(True)
app.MainLoop()


app = wx.App()
frame = wx.Frame(None,style=wx.MAXIMIZE_BOX | wx.RESIZE_BORDER
	| wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)

frame.Show(True)

app.MainLoop()
app = wx.App()
frame = wx.Frame(None,title='文本',size=(500,550));
frame.Show(True)
app.MainLoop()
app = wx.App()
frame = wx.Frame(None,title='文本',size=(500,550))
frame.Maximize()
frame.Move(0,0)
frame.Show(True)

app.MainLoop()
app = wx.App()
frame = wx.Frame(None,title='查询',size=(300,500))
frame.Center()
frame.Show(True)
app.MainLoop()
app = wx.App()

frame = wx.Frame(None,title='Menu',size=(450,550));
frame.Center()

Menubar = wx.MenuBar()
fileMenu = wx.Menu()
fileMenu.Append(wx.ID_EDIT,'Quit','exit application')

Menubar.Append(fileMenu,'&File')

frame.SetMenuBar(Menubar)

frame.Show(True)

app.MainLoop()

"""

def close():
    frame.Close()
app = wx.App()

frame = wx.Frame(None,title='文本',size=(300,500))
frame.Center()

MenuBar = wx.MenuBar()
OpenMenu = wx.Menu()
OpenMenu.Append(wx.ID_OPEN,'打开','打开文件')
CloseMenu = wx.Menu()
CloseMenu.Append(wx.ID_CLOSE,'关闭','退出')


MenuBar.Append(OpenMenu,'&文件')
MenuBar.Append(CloseMenu,'&文件')

frame.SetMenuBar(MenuBar)

#frame.Bind(wx.EVT_MENU,frame.Close,CloseMenu)

frame.Show(True)

app.MainLoop()