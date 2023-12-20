import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(35, 61)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(266, 23)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(35, 195)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(266, 23)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Cursor = System.Windows.Forms.Cursors.Arrow
		self._label1.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(92, 337)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(152, 49)
		self._label1.TabIndex = 2
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(130, 28)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(54, 30)
		self._label2.TabIndex = 3
		self._label2.Text = "Num1"
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(130, 151)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(54, 30)
		self._label3.TabIndex = 4
		self._label3.Text = "Num2"
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(35, 237)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 30)
		self._button1.TabIndex = 5
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(130, 237)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 30)
		self._button2.TabIndex = 6
		self._button2.Text = "-"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(226, 237)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 30)
		self._button3.TabIndex = 7
		self._button3.Text = "="
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(35, 282)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(75, 30)
		self._button4.TabIndex = 8
		self._button4.Text = "^"
		self._button4.UseVisualStyleBackColor = True
		# 
		# button5
		# 
		self._button5.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(130, 282)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(75, 30)
		self._button5.TabIndex = 9
		self._button5.Text = "/"
		self._button5.UseVisualStyleBackColor = True
		# 
		# button6
		# 
		self._button6.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(226, 282)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(75, 30)
		self._button6.TabIndex = 10
		self._button6.Text = "//"
		self._button6.UseVisualStyleBackColor = True
		# 
		# button7
		# 
		self._button7.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(35, 395)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(75, 30)
		self._button7.TabIndex = 11
		self._button7.Text = "Clear"
		self._button7.UseVisualStyleBackColor = True
		# 
		# button8
		# 
		self._button8.Font = System.Drawing.Font("MS PGothic", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(226, 395)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(75, 30)
		self._button8.TabIndex = 12
		self._button8.Text = "Exit"
		self._button8.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(335, 449)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog140"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		def plus = int(textBox.Text1) + int(textBox.Text2)
		if eq:
			self._label1 = str(plus)
		else pass
			

	def Button2Click(self, sender, e):
		def min = int(textBox.Text1) - int(textBox.Text2)

	def Button3Click(self, sender, e):
		def eq = 