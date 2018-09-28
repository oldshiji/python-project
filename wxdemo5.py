import wx
import time

App = wx.App()

Frame = wx.Frame(None,-1,time.strftime('%Y-%m-%d',time.localtime(time.time())))

Frame.Show()

App.MainLoop()
