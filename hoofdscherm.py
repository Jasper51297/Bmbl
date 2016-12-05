import wx

from bruikbaar_methode import BoxVorm
import startscherm
import eindscherm
import sys

class Hoofdscherm(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800, 400))
        self.paneelA = startscherm.Input(self, -1)
        self.paneelB = eindscherm.Input(self, -1)
        self.box = wx.BoxSizer()
        self.box.Add(self.paneelA, 1, wx.EXPAND)
        self.box.Add(self.paneelB, 1, wx.EXPAND)
        self.SetSizer(self.box)
        self.paneelB.Hide()
        self.knoppenBinden()
        self.Centre()
        self.Show(True)

    def knoppenBinden(self):
        self.paneelA.knopstart.Bind(wx.EVT_BUTTON, self.onStart)        
        self.paneelA.knopstop.Bind(wx.EVT_BUTTON, self.onStop)

    def onStart(self, event):
        #Roep functies aan om primer te bepalen, en weergeef de resultaten
        results = self.getResults()
        self.paneelA.Hide()
        self.paneelB.Show()
        self.Layout()

    def getResults(self):
        DNA, Start, Stop, Lengte = self.getInput()
        compDNA = self.getComp(DNA)
        primers = []
        for i in range(2):
            primers.append(getPrimers(DNA, compDNA, Start, Stop, Lengte))
        return primers


    def getPrimers(self, DNA, compDNA, Start, Stop, Lengte):
        pass


    def checkGC(self, primer):
        score = 0
        length = len(primer)
        for nuc in primer:
            if nuc.upper() in 'GC':
                score += 1
        perc = (length/score) * 100
        if perc >= 50 and perc <= 60:
            return primer
        return False


    def checkTM(self, primer):
        TM = 0
        GC = 0
        AT = 0
        for nuc in primer:
            if nuc.upper() in 'GC':
                GC += 1
            elif nuc.upper() in 'AT':
                AT += 1
        TM = GC * 4 + AT * 2
        if TM >= 55 or TM <= 60:
            return primer
        return False


    def getComp(self, dna):
        basen = {'A':'T', 'G':'C', 'C':'G', 'T':'A'}
        comp = ''
        for nuc in dna:
            comp += basen[nuc.upper()]
        return comp
            

    
    def getInput(self):
        DNA = self.paneelA.dnainput.GetValue()
        Start = self.paneelA.startinput.GetValue()
        Stop = self.paneelA.stopinput.GetValue()
        Lengte = self.paneelA.pcrlen.GetValue()
        return DNA, Start, Stop, Lengte
        
    def onStop(self, event):
        sys.exit()

if __name__ == "__main__":
    app = wx.App()
    Hoofdscherm(None, -1, "Primer Design")
    app.MainLoop()
