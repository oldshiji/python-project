import wx


App = wx.App(False)

Frame = wx.Frame(None,size=(800,650),title='Hello')
#Frame.Move((500,200))
#Frame.Move((0,0))
Frame.Center()
Frame.Show(True)
#Frame.Maximize()

App.MainLoop()
