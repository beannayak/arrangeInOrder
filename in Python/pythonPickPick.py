#!/usr/bin/python
import wx
from datetime import datetime
import random
import inspect, os

class MyFrame(wx.Frame):
    m_button=[]
    messageBoxShown = False
    for x in range(0, 18):
        m_button.append(object)

    def __init__(self, *args, **kwds):
        kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)

        y = randomTuple()
        #y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        for x in range(0, 18):
            if (x <= 14):
                self.m_button[x] = wx.Button(self, -1, str(y[x]))
            else:
                self.m_button[x] = wx.Button(self, -1, str(x))
            self.m_button[x].Bind(wx.EVT_BUTTON, self.onButton2)

        self.m_button[15].SetLabel(" ")
        self.m_button[16].SetLabel("&StartAgain")
        self.m_button[17].SetLabel("&Exit")

        self.__set_properties()
        self.__do_layout()

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)
        self.timer.Start(1000)

    def OnTimer(self, event):
        if (self.messageBoxShown == False):
            gameEnded = True
            for x in range (0, 16):
                if (self.m_button[x].GetLabel() != " "):
                    if (int(self.m_button[x].GetLabel()) != (x+1)):
                        gameEnded = False

            if (not(gameEnded)):
                gameEnded = True
                for x in range(0, 16):
                    if (self.m_button[x].GetLabel() != " "):
                        if (int(self.m_button[x].GetLabel()) != x):
                            return
                        
            if (gameEnded):
                self.messageBoxShown = True
                answer = wx.MessageBox("Congratulation! Play Again?", "pickpick", wx.YES_NO)
                if (answer == wx.YES):
                    self.startAgain()
                    self.messageBoxShown = False
                else:
                    self.timer.Start()
                    self.Close()
                
        else:
            print ("eventMessageShown")

    def startAgain(self):
        y = randomTuple()
        for x in range(0, 15):
            self.m_button[x].SetLabel(str(y[x]))
        self.m_button[15].SetLabel(" ")

    def onButton2(self, event):
        index = -1  
        for x in range(0, 18):
            if (event.GetId() == self.m_button[x].GetId()):
                index = x
                break

        if (index == 17):
           self.Close()
        elif (index == 16):
           self.startAgain()
        else:
           done = False
           rightMost = False
           leftMost = False
           if ((index % 4) == 0):
               leftMost = True
           elif ((index % 4) == 3):
               rightMost = True

           if ((index - 4) >= 0):
               if (self.m_button[index-4].GetLabel() == " "):
                   self.swapLabel(index, index-4)
                   done = True

           if ((index - 1) >= 0 and not(done) and not(leftMost)):
               if (self.m_button[index-1].GetLabel() == " "):
                   self.swapLabel(index, index-1)
                   done = True

           if ((index + 1) <= 15 and not(done) and not(rightMost)):
               if (self.m_button[index+1].GetLabel() == " "):
                   self.swapLabel(index, index+1)
                   done = True
           
           if ((index + 4) <= 15 and not(done)):
               if (self.m_button[index+4].GetLabel() == " "):
                   self.swapLabel(index, index+4)
                   done = True

    def swapLabel(self, index, index2):
        temp = self.m_button[index].GetLabel()
        self.m_button[index].SetLabel(self.m_button[index2].GetLabel())
        self.m_button[index2].SetLabel(temp)

    def __set_properties(self):
        self.SetTitle("Pickpick.pie")
        self.SetSize((356, 220))

    def __do_layout(self):
        object_1 = wx.BoxSizer(wx.VERTICAL)
        object_6 = wx.BoxSizer(wx.HORIZONTAL)
        object_5 = wx.BoxSizer(wx.HORIZONTAL)
        object_4 = wx.BoxSizer(wx.HORIZONTAL)
        object_3 = wx.BoxSizer(wx.HORIZONTAL)
        object_2 = wx.BoxSizer(wx.HORIZONTAL)
        object_2.Add(self.m_button[0], 0, wx.ALL, 5)
        object_2.Add(self.m_button[1], 0, wx.ALL, 5)
        object_2.Add(self.m_button[2], 0, wx.ALL, 5)
        object_2.Add(self.m_button[3], 0, wx.ALL, 5)
        object_1.Add(object_2, 0, 0, 5)
        object_3.Add(self.m_button[4], 0, wx.ALL, 5)
        object_3.Add(self.m_button[5], 0, wx.ALL, 5)
        object_3.Add(self.m_button[6], 0, wx.ALL, 5)
        object_3.Add(self.m_button[7], 0, wx.ALL, 5)
        object_1.Add(object_3, 0, 0, 5)
        object_4.Add(self.m_button[8], 0, wx.ALL, 5)
        object_4.Add(self.m_button[9], 0, wx.ALL, 5)
        object_4.Add(self.m_button[10], 0, wx.ALL, 5)
        object_4.Add(self.m_button[11], 0, wx.ALL, 5)
        object_1.Add(object_4, 0, 0, 5)
        object_5.Add(self.m_button[12], 0, wx.ALL, 5)
        object_5.Add(self.m_button[13], 0, wx.ALL, 5)
        object_5.Add(self.m_button[14], 0, wx.ALL, 5)
        object_5.Add(self.m_button[15], 0, wx.ALL, 5)
        object_1.Add(object_5, 0, 0, 5)
        object_6.Add(self.m_button[16], 0, wx.ALL, 5)
        object_6.Add(self.m_button[17], 0, wx.ALL, 5)
        object_1.Add(object_6, 0, wx.ALIGN_RIGHT, 5)
        self.SetSizer(object_1)
        self.Layout()

def randomTuple():
    x = datetime.now()
    tt = x.timetuple()
    random.seed(tt[3]*3600+tt[4]*60+tt[5])
    hasPrev = False
    temp = 0
    myVal = []
    for x in range (0, 15):
        myVal.append(0)

    for x in range(0,15):
        a = random.randint(1,15)
        condition = True
        while (condition):
            for y in range(0, x):
                hasPrev = False
                if (a == myVal[y]):
                    hasPrev = True
                    break

            if (hasPrev):
                if (a<=14):
                    a+=1
                else:
                    a = 1
            else:
                myVal[x] = a
                break
            condition = (x <= 14)
    return myVal

if __name__ == "__main__":
    app = wx.App(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Centre()
    frame_1.Show()
    app.MainLoop()

