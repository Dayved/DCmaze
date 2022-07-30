import wx
import wx.grid as grid


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 600))

        # self.panel = wx.Panel (self)

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self). __init__(parent)

        madrid = grid.Grid(self)
        madrid.CreateGrid(40, 8)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(madrid, 1, wx.EXPAND)
        self.SetSizer(sizer)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Test Grid")
        self.frame.Show()
        return True


app = MyApp()
app.MainLoop()
