import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 51)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(91, 63)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Pay:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 158)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(103, 58)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay Periods Per Year:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 253)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(103, 61)
		self._label3.TabIndex = 2
		self._label3.Text = "Salary Pay Per Period:"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 390)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 46)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(109, 390)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 46)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(208, 390)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 46)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(109, 51)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(142, 38)
		self._textBox1.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(109, 158)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(142, 38)
		self._textBox2.TabIndex = 7
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label4.Font = System.Drawing.Font("Myanmar Text", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(109, 253)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(142, 28)
		self._label4.TabIndex = 8
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(295, 448)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog153"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sum = num1 / num2
		self._label4.Text = str(sum)

	def Button2Click(self, sender, e):
		self._textBox1.Text = " "
		self._textBox2.Text = " "
		self._label4.Text = " "

	def Button3Click(self, sender, e):
		Application.Exit()