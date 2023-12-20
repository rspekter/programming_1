require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@label5 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label1.Location = System::Drawing::Point.new(187, 55)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(376, 44)
		@label1.TabIndex = 0
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label2
		# 
		@label2.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label2.Location = System::Drawing::Point.new(187, 99)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(100, 23)
		@label2.TabIndex = 1
		@label2.Click { |sender, e| self.Label2Click(sender, e) }
		# 
		# label3
		# 
		@label3.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label3.Location = System::Drawing::Point.new(187, 145)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(100, 23)
		@label3.TabIndex = 2
		@label3.Click { |sender, e| self.Label3Click(sender, e) }
		# 
		# label4
		# 
		@label4.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label4.Location = System::Drawing::Point.new(187, 200)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(100, 23)
		@label4.TabIndex = 3
		@label4.Click { |sender, e| self.Label4Click(sender, e) }
		# 
		# label5
		# 
		@label5.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label5.Location = System::Drawing::Point.new(187, 252)
		@label5.Name = "label5"
		@label5.Size = System::Drawing::Size.new(100, 23)
		@label5.TabIndex = 4
		@label5.Click { |sender, e| self.Label5Click(sender, e) }
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button1.Location = System::Drawing::Point.new(187, 332)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(189, 53)
		@button1.TabIndex = 5
		@button1.Text = "show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button2.Location = System::Drawing::Point.new(459, 332)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(199, 53)
		@button2.TabIndex = 6
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ButtonHighlight
		self.ClientSize = System::Drawing::Size.new(820, 433)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label5)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "phone_numbers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Culvers - (608) 756-2611"
		@label2.Text = "Dairy Queen - (608) 754-3095"
		@label3.Text = "Taco Bell - (608) 758-2050"
		@label4.Text = "Jimmy John's - (608) 755-0055"
		@label5.Text = "Citrus Cafe - (608) 754-9006"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
		@label2.Text = ""
		@label3.Text = ""
		@label4.Text = ""
		@label5.Text = ""
	end

	def Label1Click(sender, e)
		
	end

	def Label2Click(sender, e)
		
	end

	def Label3Click(sender, e)
		
	end

	def Label4Click(sender, e)
		
	end

	def Label5Click(sender, e)
		
	end
end

