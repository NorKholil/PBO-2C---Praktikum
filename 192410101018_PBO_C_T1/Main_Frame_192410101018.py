import wx
from Frame_192410101018 import FrameKholil

class Identitas (FrameKholil):
    def __init__(self, parent):
        FrameKholil.__init__(self, parent)
        self.SetTitle("Tugas1 PBO2C - Praktikum")
        # self.SetIcon(wx.Icon("unej.ico"))

app = wx.App()
frame = Identitas(parent=None)
frame.Show()
app.MainLoop()