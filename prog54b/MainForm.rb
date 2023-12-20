require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@label3 = System::Windows::Forms::Label.new()
		@label4 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.Font = System::Drawing::Font.new("MingLiU-ExtB", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox1.Location = System::Drawing::Point.new(404, 70)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 42)
		@textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		@textBox2.Font = System::Drawing::Font.new("MingLiU-ExtB", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox2.Location = System::Drawing::Point.new(404, 161)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(100, 42)
		@textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		@textBox3.Font = System::Drawing::Font.new("MingLiU-ExtB", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox3.Location = System::Drawing::Point.new(404, 249)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(100, 42)
		@textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		@textBox4.Font = System::Drawing::Font.new("MingLiU-ExtB", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@textBox4.Location = System::Drawing::Point.new(404, 339)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(100, 42)
		@textBox4.TabIndex = 3
		# 
		# label1
		# 
		@label1.Font = System::Drawing::Font.new("MS Gothic", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(505, 116)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(98, 23)
		@label1.TabIndex = 4
		@label1.Text = "Sum"
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# label2
		# 
		@label2.Font = System::Drawing::Font.new("MS Gothic", 18, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(505, 298)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(110, 35)
		@label2.TabIndex = 5
		@label2.Text = "Average"
		# 
		# label3
		# 
		@label3.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label3.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label3.Location = System::Drawing::Point.new(609, 118)
		@label3.Name = "label3"
		@label3.Size = System::Drawing::Size.new(131, 38)
		@label3.TabIndex = 6
		# 
		# label4
		# 
		@label4.BorderStyle = System::Windows::Forms::BorderStyle.Fixed3D
		@label4.Font = System::Drawing::Font.new("Microsoft Sans Serif", 15.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label4.Location = System::Drawing::Point.new(609, 301)
		@label4.Name = "label4"
		@label4.Size = System::Drawing::Size.new(131, 39)
		@label4.TabIndex = 7
		# 
		# button1
		# 
		@button1.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(86, 116)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(139, 40)
		@button1.TabIndex = 8
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(86, 209)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(139, 40)
		@button2.TabIndex = 9
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.Font = System::Drawing::Font.new("Modern No. 20", 17.9999981, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button3.Location = System::Drawing::Point.new(86, 300)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(139, 40)
		@button3.TabIndex = 10
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(865, 445)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label4)
		self.Controls.Add(@label3)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "prog54b"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		num1 = int(@textBox1.Text)
		num2 = int(@textBox2.Text)
		num3 = int(@textBox3.Text)
		num4 = int(@textBox4.Text)
		sum = num1 + num2 + num3 + num4
		average = sum / 4
		@label3.Text = "" + str(sum)
		@label4.Text = "" + str(average)
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@textBox4.Text = ""
		@label3.Text = ""
		@label4.Text = ""
	end

	def Button3Click(sender, e)
		Application.Exit()
	end
end

