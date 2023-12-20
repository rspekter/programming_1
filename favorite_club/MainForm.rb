require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Microsoft Tai Le", 24, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(316, 12)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(223, 80)
		@button1.TabIndex = 0
		@button1.Text = "favorite club"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# label1
		# 
		@label1.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label1.Font = System::Drawing::Font.new("MS PGothic", 36, System::Drawing::FontStyle.Bold | System::Drawing::FontStyle.Italic, System::Drawing::GraphicsUnit.Point, 0)
		@label1.ForeColor = System::Drawing::SystemColors.ButtonHighlight
		@label1.Location = System::Drawing::Point.new(275, 191)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(314, 134)
		@label1.TabIndex = 1
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(356, 120)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(134, 42)
		@button2.TabIndex = 2
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::SystemColors.ActiveCaptionText
		self.ClientSize = System::Drawing::Size.new(860, 441)
		self.Controls.Add(@button2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "favorite_club"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "World Building"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

