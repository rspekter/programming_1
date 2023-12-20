require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.Location = System::Drawing::Point.new(13, 4)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(259, 248)
		@label1.TabIndex = 0
		@label1.Text = "label1"
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(284, 261)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "tes"
		self.ResumeLayout(false)
	end

	def Label1Click(sender, e)
		@label.Text = "What"\n "what"\n
	end
end

