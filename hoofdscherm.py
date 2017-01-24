#!/usr/bin/python

"""
Scriptname: hoofdscherm.py
Author: Jasper van Dalum & Soad Eldeb
Date: 24/1/2017
Version: 2.5
"""

import wx
from bruikbaar_methode import BoxVorm
import startscherm
import eindscherm
import helpscherm
import sys


class Hoofdscherm(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(800, 400))
        self.paneelA = startscherm.Input(self, -1)
        self.paneelB = eindscherm.Input(self, -1)
        self.paneelC = helpscherm.Input(self, -1)
        self.box = wx.BoxSizer()
        self.box.Add(self.paneelA, 1, wx.EXPAND)
        self.box.Add(self.paneelB, 1, wx.EXPAND)
        self.box.Add(self.paneelC, 1, wx.EXPAND)
        self.SetSizer(self.box)
        self.paneelB.Hide()
        self.paneelC.Hide()
        self.knoppenBinden()
        self.Centre()
        self.Show(True)

    def knoppenBinden(self):
        """Deze knoppen bind de knoppen uit een aantal schermen met
        verschillende events.
        """
        self.paneelA.knopstart.Bind(wx.EVT_BUTTON, self.onStart)
        self.paneelA.knopstop.Bind(wx.EVT_BUTTON, self.onStop)
        self.paneelC.knopterug.Bind(wx.EVT_BUTTON, self.onTerug)
        self.paneelA.knophelp.Bind(wx.EVT_BUTTON, self.onHelp)

    def onStart(self, event):
        """Deze functie gaat op zoek naar de primers als de calculate knop
        ingedrukt wordt.
        """
        DNA, Start, Stop, PCRLen = self.getInput()
        primers1, primers2, prodLen1, prodLen2 = self.results(DNA, Start,
                                                              Stop, PCRLen)
        self.printResults(primers1, primers2, prodLen1, prodLen2)
        self.paneelA.Hide()
        self.paneelB.Show()
        self.Layout()

    def printResults(self, primers1, primers2, prodLen1, prodLen2):
        """Deze functie haalt de resultaten op en vult de textctrl widgets met
        de resultaten
        """
        primers1 = primers1.split(';')
        primers2 = primers2.split(';')
        self.paneelB.Revprim1.SetValue("5'" + primers1[1] + "'3")
        self.paneelB.Forprim1.SetValue("5'" + primers1[0] + "'3")
        self.paneelB.Revprim2.SetValue("5'" + primers2[1] + "'3")
        self.paneelB.Forprim2.SetValue("5'" + primers2[0] + "'3")
        self.paneelB.pcrprod1.SetValue(str(prodLen1))
        self.paneelB.pcrprod2.SetValue(str(prodLen2))

    def getInput(self):
        """Deze functie slaat de input van de gebruiker uit de textctrl widgets
        op in variabelen
        """
        DNA = self.paneelA.dnainput.GetValue()
        Start = self.paneelA.startinput.GetValue()
        Stop = self.paneelA.stopinput.GetValue()
        PCRLen = self.paneelA.pcrlen.GetValue()
        return str(DNA), int(Start), int(Stop), int(PCRLen)

    def results(self, DNA, Start, Stop, PCRLen):
        """Deze functie roept de functies aan die de primers zoeken en vangt de
        gevonden primers op.
        """
        primers1, prodLen1 = self.setPrimerLocs(DNA, Start, Stop, PCRLen, '')
        primers2, prodLen2 = self.setPrimerLocs(DNA, Start, Stop, PCRLen,
                                                primers1)
        return primers1, primers2, prodLen1, prodLen2

    def setPrimerLocs(self, DNA, Start, Stop, PCRLen, FoundPrimers):
        """Deze functie berekend de startlocaties voor het zoeken naar de
        primers.
        """
        if Stop - Start < PCRLen:
            StartFprimer, StopFprimer, StartRprimer, StopRprimer = Start - 1, \
                Start + 20, Stop - 22, Stop - 1
        else:
            StartFprimer, StopFprimer, StartRprimer, StopRprimer = Start - 1, \
                Start + 29, Start + PCRLen - 31, Start + PCRLen - 1
        primers, prodLen = self.getPrimers(DNA, StartFprimer, StopFprimer,
                                           StartRprimer, StopRprimer,
                                           FoundPrimers)
        return primers, prodLen

    def getPrimers(self, DNA, StartFprimer, StopFprimer, StartRprimer,
                   StopRprimer, FoundPrimers):
        """Deze functie loopt door een loop heen die de lengte van de primer
        bepaalt en er wordt gecontroleerd of de gevonden primers correct zijn.
        """
        correct = 'Nee'
        while correct == 'Nee':
            for primerlen in range(30, 16, -1):
                Fprimer, Rprimer = self.selectPrimers(DNA, StartFprimer,
                                                      StopFprimer,
                                                      StartRprimer,
                                                      StopRprimer)
                correct, Rprimer = self.checkPrimer(DNA, Fprimer, Rprimer,
                                                    FoundPrimers)
                if correct == 'Nee':
                    StartFprimer, StopFprimer, StartRprimer, StopRprimer = \
                        self.changeLoc(StartFprimer, StopFprimer,
                                       StartRprimer, StopRprimer, primerlen)
        primers = Fprimer + ';' + Rprimer
        prodLen = StopRprimer - StartFprimer
        return primers, prodLen

    def checkPrimer(self, DNA, Fprimer, Rprimer, Blacklist):
        """Deze functie roept de functies aan die de primers controleren.
        Daarna wordt gecontroleerd of de primer goed is of niet.
        """
        score, resultaat = 0, 'Nee'
        resultaat1, resultaat6 = self.checkUnique(DNA, Fprimer), \
            self.checkUnique(DNA, Rprimer)
        Rprimer = self.getComp(Rprimer)
        Rprimer = Rprimer[::-1]
        resultaat2, resultaat7 = self.checkGC(Fprimer), self.checkGC(Rprimer)
        resultaat3, resultaat8 = self.checkTM(Fprimer), self.checkTM(Rprimer)
        resultaat4, resultaat9 = self.checkEnd(Fprimer), self.checkEnd(Rprimer)
        resultaat5, resultaat10 = self.checkFound(Fprimer, Blacklist), \
            self.checkFound(Rprimer, Blacklist)
        resultaten = [resultaat1, resultaat2, resultaat3, resultaat4,
                      resultaat5, resultaat6, resultaat7, resultaat8,
                      resultaat9, resultaat10]
        for res in resultaten:
            if res != 'Nee':
                score += 1
        if score == 10:
            resultaat = 'Ja'
        return resultaat, Rprimer

    def checkFound(self, primer, Blacklist):
        """Deze primer controleerd of de primer al een keer eerder gevonden
        is zodat er geen dubbele primers als resultaat zijn.
        """
        if primer in Blacklist:
            return 'Nee'
        return 'Ja'

    def checkUnique(self, DNA, primer):
        """Deze functie controleerd of de primer op 1 plek past zodat
        ze specifiek zijn.
        """
        i, Start, Stop = 0, 0, 29
        while len(DNA[Start:Stop]) == 30:
            if primer in DNA[Start:Stop]:
                i += 1
            if i > 1:
                return 'Nee'
            Start += 1
            Stop += 1
        return 'Ja'

    def checkEnd(self, primer):
        """Deze functie controleerd of het 3' eind van een primer
        eindigt met een G of een C
        """
        if primer[-1:] == 'G' or primer[-1:] == 'C':
            return 'Ja'
        return 'Nee'

    def checkGC(self, primer):
        """Deze functie controleerd of het GC percentage tussen de
        50 en 60% ligt.
        """
        score = 0.0
        for nuc in primer:
            if nuc.upper() in 'GC':
                score += 1
        perc = (score / len(primer) * 100)
        if int(perc) >= 50 and int(perc) <= 60:
            return 'Ja'
        return 'Nee'

    def checkTM(self, primer):
        """Deze functie controleerd of de smelttemperatuur (Tm) tussen de
        55 en 65 graden celcius ligt.
        """
        TM, GC, AT = 0, 0, 0
        for nuc in primer:
            if nuc.upper() in 'GC':
                GC += 1
            elif nuc.upper() in 'AT':
                AT += 1
        TM = (GC * 4) + (AT * 2)
        if TM >= 55 or TM <= 65:
            return 'Ja'
        return 'Nee'

    def getComp(self, Rprimer):
        """Deze functie maakt voor een stuk DNA de
        complementaire strand.
        """
        basen = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
        comp = ''
        for nuc in Rprimer:
            comp += basen[nuc.upper()]
        return comp

    def changeLoc(self, StartFprimer, StopFprimer, StartRprimer, StopRprimer,
                  primerlen):
        """Deze functie past de primerlocaties aan. De stop locaties worden
        continu aangepast door de primerlen, de start locaties worden
        aangepast als de primerlengte 30 is.
        """
        if primerlen == 30:
            StartFprimer += 1
            StartRprimer -= 1
        StopFprimer = StartFprimer + primerlen
        StopRprimer = StartRprimer + primerlen
        return StartFprimer, StopFprimer, StartRprimer, StopRprimer

    def selectPrimers(self, DNA, StartFprimer, StopFprimer, StartRprimer,
                      StopRprimer):
        """Deze functie kiest met behulp van de start en stop locaties
        een primer uit het DNA.
        """
        Fprimer = DNA[StartFprimer:StopFprimer]
        Rprimer = DNA[StartRprimer:StopRprimer]
        return Fprimer, Rprimer

    def onStop(self, event):
        """Als er op de stop knop gedrukt wordt,
        sluit het programma af.
        """
        sys.exit()

    def onTerug(self, event):
        """Deze knop zorgt ervoor dat de gebruiker teruggestuurd wordt naar
        het scherm waar de gegevens ingevoerd kunnen worden
        """
        self.paneelC.Hide()
        self.paneelA.Show()
        self.Layout()

    def onHelp(self, event):
        """Deze knop laat het helpscherm zien.
        """
        self.paneelA.Hide()
        self.paneelC.Show()
        self.Layout()

if __name__ == "__main__":
    app = wx.App()
    Hoofdscherm(None, -1, "Primer Design")
    app.MainLoop()
