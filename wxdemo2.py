import wx

App = wx.App(False)

Frame = wx.Frame(None,style=wx.MINIMIZE_BOX  |wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN)

Frame.Show(True)

App.MainLoop()

