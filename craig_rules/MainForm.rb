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
		@label1.BackColor = System::Drawing::Color.LightSkyBlue
		@label1.BorderStyle = System::Windows::Forms::BorderStyle.FixedSingle
		@label1.Font = System::Drawing::Font.new("MingLiU_HKSCS-ExtB", 24, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(214, 100)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(417, 186)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.SlateGray
		@button1.Font = System::Drawing::Font.new("Perpetua Titling MT", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.ForeColor = System::Drawing::Color.Transparent
		@button1.Location = System::Drawing::Point.new(214, 289)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(417, 46)
		@button1.TabIndex = 1
		@button1.Text = "truth"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(388, 341)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 2
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.LightBlue
		self.ClientSize = System::Drawing::Size.new(858, 444)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "craig_rules"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Craig Rules!"
	end

	def Label1Click(sender, e)
		
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

