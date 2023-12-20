import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Palatino Linotype", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(301, 8)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(277, 46)
		self._label1.TabIndex = 0
		self._label1.Text = "Multiples of 3"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Palatino Linotype", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 16
		self._listBox1.Location = System.Drawing.Point(301, 74)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(277, 212)
		self._listBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(65, 379)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(213, 39)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(328, 379)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(213, 39)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(593, 379)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(213, 39)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Palatino Linotype", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(301, 293)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(277, 39)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(866, 445)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog152a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Mult. 3"
		self._listBox1.Items.Add(heading)
		tre = 0
		for tick in range (1, 3225):
			line = str(tick) + "\t\t" + str(int(tre))
			self._listBox1.Items.Add(line)
			tre = tick *+ 3
			sum = 9669 * 1612
			self._label2.Text = str("Sum = " + str(sum))

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()