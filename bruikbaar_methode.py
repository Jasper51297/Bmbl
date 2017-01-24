#!/usr/bin/python

"""
Scriptname: bruikbaar_methode.py
Author: Jasper van Dalum & Soad Eldeb
Date: 24/1/2017
Version: 1.1
"""

import wx


def center(centreer):
    #Het in het midden plaaten van een StaticText op een paneel
    hbox = wx.BoxSizer()
    hbox.Add(centreer, 1, wx.ALIGN_CENTRE)
    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox, 1, wx.ALIGN_CENTRE)
    return vbox


def Ronder(ronder):
    #Het plaatsten van iets rechtonder van de box
    hbox = wx.BoxSizer()
    hbox.Add((0, 0), 1, wx.ALL)
    hbox.Add(ronder, 0, wx.ALIGN_BOTTOM)
    return hbox


def BoxVorm(orient, widget, verhouding):
    """De vormen van de boxen maken dmv een lijst met de
    horizontaal/verticaal, window, verhoudingen
    """
    boxje = wx.BoxSizer(orient)
    for x in range(0, len(widget)):
        boxje.Add(widget[x], verhouding[x], wx.EXPAND)
    return boxje


def BoxVormFlag(widget, verhouding, flags, orient=wx.HORIZONTAL):
    """De BoxVorm methode met met het meegeven van een flag, en een standaard
    orientatie die horizontaal is
    """
    boxje = wx.BoxSizer(orient)
    for x in range(0, len(widget)):
        boxje.Add(widget[x], verhouding[x], flags[x])
    return boxje
