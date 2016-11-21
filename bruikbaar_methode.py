import wx
 
# Het in het midden plaaten van een StaticText op een paneel
def center(centreer):
    hbox = wx.BoxSizer()
    hbox.Add(centreer, 1, wx.ALIGN_CENTRE)
    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox, 1, wx.ALIGN_CENTRE)
    return vbox
 
# Het plaatsten van iets rechtonder van de box
def Ronder(ronder):
    hbox = wx.BoxSizer()
    hbox.Add((0,0), 1, wx.ALL)
    hbox.Add(ronder, 0, wx.ALIGN_BOTTOM)
    return hbox
     
# De vormen van de boxen maken dmv een lijst met de
# horizontaal/verticaal, window, verhoudingen
def BoxVorm(orient, widget, verhouding):
    boxje = wx.BoxSizer(orient)
    for x in range(0, len(widget)):
        boxje.Add(widget[x], verhouding[x], wx.EXPAND)
    return boxje
 
# De BoxVorm methode met met het meegeven van een flag, en een standaard
# orientatie die horizontaal is 
def BoxVormFlag(widget, verhouding, flags, orient=wx.HORIZONTAL):
    boxje = wx.BoxSizer(orient)
    for x in range(0, len(widget)):
        boxje.Add(widget[x],verhouding[x], flags[x])
    return boxje
