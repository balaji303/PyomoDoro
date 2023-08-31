'''
Pyomodoro v0.1
-------------------------------------------------------------
@balaji303
'''

import wx.xrc
import wx.aui
import wx.richtext
import os
import subprocess


class GUI (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, 
                          None,
                          -1, 
                          u"Pyomodoro v1", 
                          size=(500, 500),
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.Colour(180, 180, 180))
        timerlist = ['5', '15', '25'] 
        self.timerbox = wx.RadioBox(self, 
                                label = 'Time in minutes',
                                pos = (150,5), 
                                choices = timerlist,
                                majorDimension = 1,
                                style = wx.RA_SPECIFY_ROWS)
        self.start_button = wx.Button(self, 
                                   wx.ID_ANY, 
                                   u"Start", 
                                   wx.Point(210,425))
        self.stop_button = wx.Button(self, 
                                   wx.ID_ANY, 
                                   u"Stop", 
                                   wx.Point(300,425))
        self.start_button.Bind(wx.EVT_BUTTON, self.compile_fun) 
    def compile_fun(self,e):
        code = self.text.GetValue()        
        pyfiledir  = os.path.dirname( __file__ )
        os.chdir(pyfiledir)
        userTime = self.timerbox.GetStringSelection()
        if userTime == '5':
            #Timer for 5min
            print("5")
        elif userTime == '15':
            #Timer for 15min
            print("15")
        elif userTime == '25':
            #Timer for 25min
            print("25")
        else:
            print("Error")
        
if __name__ == '__main__':
    app = wx.App(False) 
    app_gui = GUI(None) 
    app_gui.Show(True)      
    app.MainLoop()  
