# waopp to show area and perimeter of rectangle

class rectangle:
	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
	def show(self):
		print("length = ", self.length)
		print("breadth = ", self.breadth)
	def area(self):
		ans = self.length * self.breadth
		print("area = ", round(ans,2))
	def perimeter(self):
		ans = 2 * (self.length + self.breadth)
		print("perimeter = ", round(ans,2))

length = float(input("enter length "))
breadth = float(input("enter breadth "))

r = rectangle(length, breadth)
r.show()
r.area()
r.perimeter()