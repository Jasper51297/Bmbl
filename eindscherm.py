import wx
 
from bruikbaar_methode import BoxVorm
from bruikbaar_methode import center
 
class Input(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
        self.KnopMaken()
        self.TekstMaken()
        self.TextCtrl()
        finalbox = self.BoxMaken()
        self.SetSizer(finalbox)
 
    def KnopMaken(self):
        pass
        
 
    def TekstMaken(self):
        self.tekst1 = wx.StaticText(self, -1, "Primer 1:")
        self.tekst2 = wx.StaticText(self, -1, "Forward primer:")
        self.tekst3 = wx.StaticText(self, -1, "Reversed primer:")
        self.tekst4 = wx.StaticText(self, -1, "Primer 2:")
        self.tekst5 = wx.StaticText(self, -1, "PCR Prod Length:")
        self.tekst6 = wx.StaticText(self, -1, "Forward primer:")
        self.tekst7 = wx.StaticText(self, -1, "Reversed primer:")
        self.tekst8 = wx.StaticText(self, -1, "PCR Prod Length:")

 
    def TextCtrl(self):
        self.Revprim1 = wx.TextCtrl(self)
        self.Revprim2 = wx.TextCtrl(self)
        self.Forprim1 = wx.TextCtrl(self)
        self.Forprim2 = wx.TextCtrl(self)
        self.pcrprod1 = wx.TextCtrl(self)
        self.pcrprod2 = wx.TextCtrl(self)
 
    def BoxMaken(self):
        hbox1 = BoxVorm(wx.HORIZONTAL, [center(self.tekst2), center(self.tekst3), center(self.tekst5)], [2,2,1])
        hbox2 = BoxVorm(wx.HORIZONTAL, [self.Forprim1, self.Revprim1, self.pcrprod1], [2,2,1])
        hbox3 = BoxVorm(wx.HORIZONTAL, [self.Forprim2, self.Revprim2, self.pcrprod2], [2,2,1])
        hbox4 = BoxVorm(wx.HORIZONTAL, [center(self.tekst6), center(self.tekst7), center(self.tekst8)], [2,2,1])
        vbox1 = BoxVorm(wx.VERTICAL, [center(self.tekst1), hbox1, hbox2, center(self.tekst4), hbox4, hbox3], [1,1,3,1,1,3])
        return vbox1
 
 
if __name__=="__main__":
    class Schermpje (wx.Frame):
            def __init__(self, parent, id, title):
                wx.Frame.__init__(self, parent, id, title, size=(800,400))
                boxje = wx.BoxSizer()
                boxje.Add(Input(self, id), 1, wx.EXPAND | wx.ALL, 1)
                self.SetSizer(boxje)
                self.Centre()
                self.Show(True)
                 
    app = wx.App()
    Schermpje(None, -1, "Primer Designer - Resultaten")
    app.MainLoop()
