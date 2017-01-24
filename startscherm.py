#!/usr/bin/python

"""
Scriptname: startscherm.py
Author: Jasper van Dalum & Soad Eldeb
Date: 24/1/2017
Version: 2.0
"""

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
        #Deze functie maakt de knoppen aan
        self.knopstart = wx.Button(self, -1, "Calculate")
        self.knopstop = wx.Button(self, -1, "End")
	self.knophelp = wx.Button(self, -1, "Help")

    def TekstMaken(self):
        #Deze functie maakt de statictext aan
        self.tekst1 = wx.StaticText(self, -1, "DNA invoer:")
        self.tekst2 = wx.StaticText(self, -1, "Start:")
        self.tekst3 = wx.StaticText(self, -1, "Stop:")
        self.tekst4 = wx.StaticText(self, -1, "Max lengte:")

    def TextCtrl(self):
        """Deze functie maakt tekstvakken aan die gevuld kunnen worden
        door de gebruiker.
        """
        self.dnainput = wx.TextCtrl(self)
        self.startinput = wx.TextCtrl(self)
        self.stopinput = wx.TextCtrl(self)
        self.pcrlen = wx.TextCtrl(self)

    def BoxMaken(self):
        """Deze functie maakt boxen aan zodat alle widgets op de juiste
        posities geplaatst worden.
        """
        hbox1 = center(self.tekst1)
        hbox2 = BoxVorm(wx.HORIZONTAL, [self.dnainput], [1])
        hbox3 = BoxVorm(wx.HORIZONTAL, [center(self.tekst2), self.startinput,
                                        center(self.tekst3), self.stopinput,
                                        center(self.tekst4),
                                        self.pcrlen], [1, 2, 1, 2, 1, 2])
        hbox4 = BoxVorm(wx.HORIZONTAL, [self.knopstop, self.knopstart,
                                        self.knophelp], [1, 1, 1])
        vbox1 = BoxVorm(wx.VERTICAL, [hbox1, hbox2, hbox3, hbox4],
                        [1, 4, 2, 1])
        return vbox1


if __name__ == "__main__":
    class Schermpje (wx.Frame):
            def __init__(self, parent, id, title):
                wx.Frame.__init__(self, parent, id, title, size=(800, 400))
                boxje = wx.BoxSizer()
                boxje.Add(Input(self, id), 1, wx.EXPAND | wx.ALL, 1)
                self.SetSizer(boxje)
                self.Centre()
                self.Show(True)

    app = wx.App()
    Schermpje(None, -1, "Primer Designer")
    app.MainLoop()
