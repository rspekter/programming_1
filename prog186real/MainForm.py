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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(161, 38)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(178, 29)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(161, 204)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(178, 29)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(161, 116)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(178, 29)
		self._textBox3.TabIndex = 2
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(63, 41)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(92, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Class A"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(63, 116)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(92, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Class B"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(63, 204)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(92, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Class C"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label4.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(448, 8)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "Class A:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label5.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(448, 80)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Class B:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label6.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(448, 164)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 8
		self._label6.Text = "Class C:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label7.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(448, 240)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 9
		self._label7.Text = "Total:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label8.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(576, 240)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(208, 23)
		self._label8.TabIndex = 13
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label9.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(576, 164)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(208, 23)
		self._label9.TabIndex = 12
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label10.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(576, 80)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(208, 23)
		self._label10.TabIndex = 11
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label11.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(576, 8)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(208, 23)
		self._label11.TabIndex = 10
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(148, 308)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(172, 47)
		self._button1.TabIndex = 14
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(351, 308)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(159, 47)
		self._button2.TabIndex = 15
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(535, 308)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(166, 47)
		self._button3.TabIndex = 16
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(863, 367)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog186real"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		classa = int(self._textBox1.Text)
		classb = int(self._textBox3.Text)
		classc = int(self._textBox2.Text)
		self._label11.Text = "{num:.2f}".format(num = float(classa) * 15)
		self._label10.Text = "{num:.2f}".format(num = float(classb) * 12)
		self._label9.Text = "{num:.2f}".format(num = float(classc) * 9)
		sum = float(self._label11.Text) + float(self._label10.Text) + float(self._label9.Text)
		self._label8.Text = "{num:.2f}".format(num = float(sum))

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label11.Text = ""
		self._label10.Text = ""
		self._label9.Text = ""
		self._label8.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()