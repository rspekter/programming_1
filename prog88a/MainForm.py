﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
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
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(72, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(201, 32)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Mongolian Baiti", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(347, 12)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(201, 32)
		self._textBox2.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(57, 394)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(144, 39)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(232, 394)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(144, 39)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Mongolian Baiti", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(413, 394)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(144, 39)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label1.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(57, 56)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(240, 29)
		self._label1.TabIndex = 5
		self._label1.Text = "Sum:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label2.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(57, 101)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(240, 29)
		self._label2.TabIndex = 6
		self._label2.Text = "Difference:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label3.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Location = System.Drawing.Point(57, 156)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(240, 29)
		self._label3.TabIndex = 7
		self._label3.Text = "Product:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label4.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Location = System.Drawing.Point(57, 205)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(240, 29)
		self._label4.TabIndex = 8
		self._label4.Text = "Average:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label5.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Location = System.Drawing.Point(57, 254)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(240, 29)
		self._label5.TabIndex = 9
		self._label5.Text = "Abs. Difference:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label6.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.Location = System.Drawing.Point(57, 308)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(240, 29)
		self._label6.TabIndex = 10
		self._label6.Text = "Max:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label7.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label7.Location = System.Drawing.Point(57, 354)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(240, 29)
		self._label7.TabIndex = 11
		self._label7.Text = "Min:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label8.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label8.Location = System.Drawing.Point(317, 354)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(240, 29)
		self._label8.TabIndex = 18
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label9.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label9.Location = System.Drawing.Point(317, 308)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(240, 29)
		self._label9.TabIndex = 17
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label10.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label10.Location = System.Drawing.Point(317, 254)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(240, 29)
		self._label10.TabIndex = 16
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label11.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label11.Location = System.Drawing.Point(317, 205)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(240, 29)
		self._label11.TabIndex = 15
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label12
		# 
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label12.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label12.Location = System.Drawing.Point(317, 156)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(240, 29)
		self._label12.TabIndex = 14
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label13
		# 
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label13.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label13.Location = System.Drawing.Point(317, 101)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(240, 29)
		self._label13.TabIndex = 13
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label14
		# 
		self._label14.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label14.Font = System.Drawing.Font("Mongolian Baiti", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label14.Location = System.Drawing.Point(317, 56)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(240, 29)
		self._label14.TabIndex = 12
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.Desktop
		self.ClientSize = System.Drawing.Size(622, 445)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Diff = num1 - num2
		Avg = Sum / 2
		Prd = num1 * num2
		# TODO: finish product and avg
		AbsDiff = abs(Diff)
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:  # otherwise...
			Max = num2
		
		if Max == num1:
			Min = num2
		else:
			Min = num1
			
		self._label9.Text = str(Max)
		self._label8.Text = str(Min)
		self._label14.Text = str(Sum)
		self._label13.Text = str(Diff)
		self._label10.Text = str(AbsDiff)
		self._label11.Text = str(Avg)
		self._label12.Text = str(Prd)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()