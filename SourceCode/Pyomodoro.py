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
import time

class GUI (wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, 
                          None,
                          -1, 
                          u"Pyomodoro v1", 
                          size=(300, 300),
                          style=wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.Colour(180, 180, 180))
        self.timer = wx.Timer(self)
        self.time_remaining = 0
        self.is_running = False
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        timerlist = ['5', '15', '25'] 
        self.timerbox = wx.RadioBox(self, 
                                label = 'Time in minutes',
                                pos = (100,150), 
                                choices = timerlist,
                                majorDimension = 1,
                                style = wx.RA_SPECIFY_ROWS)
        self.start_button = wx.Button(self, 
                                   wx.ID_ANY, 
                                   u"Start", 
                                   wx.Point(20,215))
        self.stop_button = wx.Button(self, 
                                   wx.ID_ANY, 
                                   u"Stop", 
                                   wx.Point(110,215))
        self.reset_button = wx.Button(self, 
                                   wx.ID_ANY, 
                                   u"Reset", 
                                   wx.Point(200,215))
        # self.start_button.Bind(wx.EVT_BUTTON, self.compile_fun)
        # create wx.Font object
        font = wx.Font(69, family = wx.FONTFAMILY_MODERN, style = 0, weight = 90,underline = False, faceName ="", encoding = wx.FONTENCODING_DEFAULT)
        self.st = wx.StaticText(self, id = 1, label ="59:59", pos =(5, 20),size = wx.DefaultSize, style = wx.ST_ELLIPSIZE_MIDDLE, name ="statictext")
        # set font for the statictext
        self.st.SetFont(font)
        self.Bind(wx.EVT_BUTTON, self.OnStart, self.start_button)
        self.Bind(wx.EVT_BUTTON, self.OnReset, self.reset_button)
        
    # def compile_fun(self,e):
    #     # code = self.text.GetValue()        
    #     # pyfiledir  = os.path.dirname( __file__ )
    #     # os.chdir(pyfiledir)
    #     userTime = self.timerbox.GetStringSelection()
    #     if userTime == '5':
    #         #Timer for 5min
    #         self.st.SetLabel("05:00")
    #         self.timeremaining = 5
    #     elif userTime == '15':
    #         #Timer for 15min
    #         self.st.SetLabel("15:00")
    #         self.timeremaining = 15
    #     elif userTime == '25':
    #         #Timer for 25min
    #         self.st.SetLabel("25:00")
    #         self.timeremaining = 25
    #     else:
    #         print("Error")
    #     self.run_timer(self.timeremaining)

    # def run_timer(self,timevalue):
    #     if timevalue == 0:
    #         self.st.SetLabel("00:00")
    #         wx.Bell()
    #     else:
    #         minutes = timevalue // 60
    #         seconds = timevalue % 60
    #         self.st.SetLabel(f"{minutes:02}:{seconds:02}")
    #         timevalue -= 1
    #         time.sleep(1)

    def OnStart(self, event):
        if not self.is_running:
            self.is_running = True
            self.time_remaining = int(self.timerbox.GetStringSelection())*60
            self.timer.Start(1000)

    def OnTimer(self, event):
        if self.is_running:
            self.time_remaining -= 1
            if self.time_remaining >= 0:
                minutes = int(self.time_remaining // 60)
                seconds = int(self.time_remaining % 60)
                self.st.SetLabel(f"{minutes:02}:{seconds:02}")
            else:
                self.st.SetLabel("00:00")
                self.is_running = False
                self.timer.Stop()
                wx.Bell()
                print("*********************End*************")
        
    def OnReset(self, event):
        if self.is_running:
            self.is_running = False
            self.timer.Stop()
            self.st.SetLabel("00:00")
        # self.time_remaining = self.time_remaining
        # self.st.SetLabel(str(self.time_remaining) + ":00")
        
        
if __name__ == '__main__':
    app = wx.App(False) 
    app_gui = GUI(None) 
    app_gui.Show(True)      
    app.MainLoop()  

