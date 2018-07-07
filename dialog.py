#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.3 on Sat Jul  7 23:35:36 2018
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MyDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLOSE_BOX
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((370, 170))
        self.button_1 = wx.Button(self, wx.ID_ANY, "Download from GitHub")
        self.button_2 = wx.Button(self, wx.ID_ANY, "Remind me later", style=wx.BU_AUTODRAW)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyDialog.__set_properties
        self.SetTitle("PySpy Update")
        self.SetSize((370, 170))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyDialog.__do_layout
        sizer_main = wx.BoxSizer(wx.VERTICAL)
        sizer_bottom = wx.BoxSizer(wx.HORIZONTAL)
        sizer_top = wx.BoxSizer(wx.HORIZONTAL)
        sizer_top_right = wx.BoxSizer(wx.VERTICAL)
        logo = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("/Users/JPK/Dropbox/Python Projects/pyspy/assets/pyspy_small.png", wx.BITMAP_TYPE_ANY))
        sizer_top.Add(logo, 0, wx.ALIGN_CENTER | wx.ALL, 10)
        header = wx.StaticText(self, wx.ID_ANY, "New version released.", style=wx.ALIGN_LEFT)
        header.SetFont(wx.Font(13, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        sizer_top_right.Add(header, 1, wx.ALIGN_BOTTOM | wx.BOTTOM | wx.TOP, 10)
        body = wx.StaticText(self, wx.ID_ANY, "Version <LATEST_VER> is now available at <LINK>. You are running version <CUR_VER>. ", style=wx.ALIGN_LEFT)
        sizer_top_right.Add(body, 1, wx.EXPAND, 0)
        sizer_top.Add(sizer_top_right, 1, wx.ALL | wx.EXPAND, 0)
        sizer_main.Add(sizer_top, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 10)
        sizer_bottom.Add(self.button_1, 1, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_bottom.Add(self.button_2, 1, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 10)
        sizer_main.Add(sizer_bottom, 1, wx.ALIGN_CENTER | wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 10)
        self.SetSizer(sizer_main)
        self.Layout()
        # end wxGlade

# end of class MyDialog


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("frame")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        self.Layout()
        # end wxGlade

# end of class MyFrame


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
