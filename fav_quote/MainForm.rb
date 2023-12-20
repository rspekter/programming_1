require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.LightCoral
		@label1.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label1.Font = System::Drawing::Font.new("Poor Richard", 26.25, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(181, 87)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(483, 238)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 21.7499981, System::Drawing::FontStyle.Bold, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(306, 328)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(220, 70)
		@button1.TabIndex = 1
		@button1.Text = "favorite quote"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(364, 51)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(105, 33)
		@button2.TabIndex = 2
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.Firebrick
		self.ClientSize = System::Drawing::Size.new(858, 444)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "fav_quote"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "You've met with a terrible fate, haven't you?"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

