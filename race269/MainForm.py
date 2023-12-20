import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._name1 = System.Windows.Forms.TextBox()
		self._name2 = System.Windows.Forms.TextBox()
		self._name3 = System.Windows.Forms.TextBox()
		self._time1 = System.Windows.Forms.TextBox()
		self._time2 = System.Windows.Forms.TextBox()
		self._time3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._place1 = System.Windows.Forms.Label()
		self._place2 = System.Windows.Forms.Label()
		self._place3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label13 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# name1
		# 
		self._name1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._name1.Location = System.Drawing.Point(93, 93)
		self._name1.Name = "name1"
		self._name1.Size = System.Drawing.Size(100, 22)
		self._name1.TabIndex = 0
		# 
		# name2
		# 
		self._name2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._name2.Location = System.Drawing.Point(93, 131)
		self._name2.Name = "name2"
		self._name2.Size = System.Drawing.Size(100, 22)
		self._name2.TabIndex = 1
		# 
		# name3
		# 
		self._name3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._name3.Location = System.Drawing.Point(93, 171)
		self._name3.Name = "name3"
		self._name3.Size = System.Drawing.Size(100, 22)
		self._name3.TabIndex = 2
		# 
		# time1
		# 
		self._time1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._time1.Location = System.Drawing.Point(215, 93)
		self._time1.Name = "time1"
		self._time1.Size = System.Drawing.Size(100, 22)
		self._time1.TabIndex = 3
		# 
		# time2
		# 
		self._time2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._time2.Location = System.Drawing.Point(215, 131)
		self._time2.Name = "time2"
		self._time2.Size = System.Drawing.Size(100, 22)
		self._time2.TabIndex = 4
		# 
		# time3
		# 
		self._time3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._time3.Location = System.Drawing.Point(215, 171)
		self._time3.Name = "time3"
		self._time3.Size = System.Drawing.Size(100, 22)
		self._time3.TabIndex = 5
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 93)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(74, 23)
		self._label1.TabIndex = 6
		self._label1.Text = "runner1"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 131)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(74, 23)
		self._label2.TabIndex = 7
		self._label2.Text = "runner2"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 171)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(74, 23)
		self._label3.TabIndex = 8
		self._label3.Text = "runner3"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(93, 56)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 9
		self._label4.Text = "name"
		self._label4.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(215, 56)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 34)
		self._label5.TabIndex = 10
		self._label5.Text = "finishing time in seconds"
		self._label5.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(93, 241)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(61, 23)
		self._label6.TabIndex = 11
		self._label6.Text = "1st place:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(93, 277)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(61, 23)
		self._label7.TabIndex = 12
		self._label7.Text = "2nd place:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(93, 316)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(61, 22)
		self._label8.TabIndex = 13
		self._label8.Text = "3rd place:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.Location = System.Drawing.Point(13, 210)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(74, 23)
		self._label9.TabIndex = 14
		self._label9.Text = "race results"
		# 
		# place1
		# 
		self._place1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._place1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._place1.Location = System.Drawing.Point(160, 241)
		self._place1.Name = "place1"
		self._place1.Size = System.Drawing.Size(100, 23)
		self._place1.TabIndex = 15
		self._place1.Text = " "
		# 
		# place2
		# 
		self._place2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._place2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._place2.Location = System.Drawing.Point(160, 277)
		self._place2.Name = "place2"
		self._place2.Size = System.Drawing.Size(100, 23)
		self._place2.TabIndex = 16
		self._place2.Text = " "
		# 
		# place3
		# 
		self._place3.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._place3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._place3.Location = System.Drawing.Point(160, 315)
		self._place3.Name = "place3"
		self._place3.Size = System.Drawing.Size(100, 23)
		self._place3.TabIndex = 17
		self._place3.Text = " "
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 370)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 45)
		self._button1.TabIndex = 18
		self._button1.Text = "calculate results"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(128, 370)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 45)
		self._button2.TabIndex = 19
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(240, 370)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 45)
		self._button3.TabIndex = 20
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label13
		# 
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(13, 13)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(310, 43)
		self._label13.TabIndex = 21
		self._label13.Text = "enter the three runner's names and finishing times"
		self._label13.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(335, 440)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._place3)
		self.Controls.Add(self._place2)
		self.Controls.Add(self._place1)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._time3)
		self.Controls.Add(self._time2)
		self.Controls.Add(self._time1)
		self.Controls.Add(self._name3)
		self.Controls.Add(self._name2)
		self.Controls.Add(self._name1)
		self.Name = "MainForm"
		self.Text = "race269"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button2Click(self, sender, e):
		self._name1.Text = ""
		self._name2.Text = ""
		self._name3.Text = ""
		self._time1.Text = ""
		self._time2.Text = ""
		self._time3.Text = ""
		self._place1.Text = ""
		self._place2.Text = ""
		self._place3.Text = ""

	def Button1Click(self, sender, e):
		time1 = int(self._time1.Text)
		time2 = int(self._time2.Text)
		time3 = int(self._time3.Text)
		name1 = str(self._name1.Text)
		name2 = str(self._name2.Text)
		name3 = str(self._name3.Text)
		place1 = str(self._place1.Text)
		place2 = str(self._place2.Text)
		place3 = str(self._place3.Text)
		
		if time1 > time2 > time3:
			place1 = str(name1)
			place2 = str(name2)
			place3 = str(name3)
			return
		elif time1 > time2 < time3:
			place1 = str(name1)
			place2 = str(name3)
			place3 = str(name2)
			
		if time2 > time3 > time1:
			place1 = str(name2)
			place2 = str(name3)
			place3 = str(name1)
		elif time2 > time3 < time1:
			place1 = str(name2)
			place2 = str(name1)
			place3 = str(name3)
			
		if time3 > time2 > time1:
			place1 = str(name3)
			place2 = str(name2)
			place3 = str(name1)
		elif time3 > time2 < time1:
			place1 = str(name3)
			place2 = str(name1)
			place3 = str(name2)

	def Button3Click(self, sender, e):
		Application.Exit()