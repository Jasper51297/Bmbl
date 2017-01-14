import wx
 
from bruikbaar_methode import BoxVorm
from bruikbaar_methode import center
 
class Input(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, style=wx.BORDER_SUNKEN)
        self.KnopMaken()
        self.TekstMaken()
        finalbox = self.BoxMaken()
        self.SetSizer(finalbox)
 
    def KnopMaken(self):
        self.knopterug = wx.Button(self, -1, "Terug")

         
    def TekstMaken(self):
        inFile = open('README.md', 'r')
        inhoud = inFile.read()
        inFile.close()
        self.tekst1 = wx.StaticText(self, -1, inhoud)
        
 
    def BoxMaken(self):
        vbox1 = BoxVorm(wx.VERTICAL, [center(self.tekst1), self.knopterug], [7,1])
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
    Schermpje(None, -1, "Primer Designer")
    app.MainLoop()
