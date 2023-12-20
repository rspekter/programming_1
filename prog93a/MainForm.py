import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
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
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Segoe Marker", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(16, 366)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(231, 67)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Segoe Marker", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(296, 366)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(250, 67)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Segoe Marker", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(591, 366)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(245, 67)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Segoe Marker", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(296, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(250, 41)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(211, 105)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 33)
		self._label1.TabIndex = 4
		self._label1.Text = "BaseRate:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(211, 158)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(114, 33)
		self._label2.TabIndex = 5
		self._label2.Text = "Surcharge:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(211, 205)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 33)
		self._label3.TabIndex = 6
		self._label3.Text = "CityTax:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(211, 251)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(126, 33)
		self._label4.TabIndex = 7
		self._label4.Text = "PayAmount"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(211, 299)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(166, 33)
		self._label5.TabIndex = 8
		self._label5.Text = "After May20th"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label6.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(459, 105)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(266, 33)
		self._label6.TabIndex = 13
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.White
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label7.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(459, 158)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(266, 33)
		self._label7.TabIndex = 12
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.White
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label8.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(459, 205)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(266, 33)
		self._label8.TabIndex = 11
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.White
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label9.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(459, 251)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(266, 33)
		self._label9.TabIndex = 10
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.White
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
		self._label10.Font = System.Drawing.Font("Segoe Marker", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(459, 299)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(266, 33)
		self._label10.TabIndex = 9
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gainsboro
		self.ClientSize = System.Drawing.Size(865, 445)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog93a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		kwattu = float(self._textBox1.Text)
		baser = kwattu * 0.0475
		scharge = baser / 10
		ctax = scharge / 3.3239
		self._label6.Text = str(baser)
		self._label7.Text = str(scharge)
		self._label8.Text = str(ctax)

	def Button2Click(self, sender, e):
		pass	

	def Button3Click(self, sender, e):
		Application.Exit()