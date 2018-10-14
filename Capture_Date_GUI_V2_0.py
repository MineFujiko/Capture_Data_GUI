# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"FPGA编号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		m_comboBox1Choices = [ u"BBFPGA", u"IFFPGA0", u"IFFPGA1" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"BBFPGA", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		self.m_comboBox1.SetSelection( 0 )
		bSizer4.Add( self.m_comboBox1, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"抓数点", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		m_comboBox2Choices = [ u"调制前", u"调制后", u"AC补偿后" ]
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"调制前", wx.DefaultPosition, wx.DefaultSize, m_comboBox2Choices, 0 )
		self.m_comboBox2.SetSelection( 0 )
		bSizer5.Add( self.m_comboBox2, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Slot号", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Catch Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"20181014测试版", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer7.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer7, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer8.Add( self.m_dirPicker1, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Save Data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button1, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, 0, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_comboBox1.Bind( wx.EVT_COMBOBOX, self.ComboboxFpgaNum )
		self.m_comboBox2.Bind( wx.EVT_COMBOBOX, self.ComboboxCaptureNode )
		self.m_button2.Bind( wx.EVT_BUTTON, self.ButtionClickCatchData )
		self.m_button1.Bind( wx.EVT_BUTTON, self.ButtionClickSaveData )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ComboboxFpgaNum( self, event ):
		FpgaNumStr = self.m_comboBox1.GetValue()
		self.m_statusBar1.SetStatusText(FpgaNumStr)
		event.Skip()
	
	def ComboboxCaptureNode( self, event ):
		FpgaNumStr = self.m_comboBox2.GetValue()
		self.m_statusBar1.SetStatusText(FpgaNumStr)
		event.Skip()
	
	def ButtionClickCatchData( self, event ):
		SlotNum = self.m_textCtrl1.GetValue()
		self.m_statusBar1.SetStatusText(SlotNum)
		event.Skip()
	
	def ButtionClickSaveData( self, event ):
		DirSaveFile = self.m_dirPicker1.GetPath()
		self.m_statusBar1.SetStatusText(DirSaveFile)
		event.Skip()
	
app = wx.App(False)
frame = wx.Frame(None,title="抓数工具 By Neo",size=(1000,800))
panel = MyFrame1(frame)
panel.Show()
app.MainLoop()

