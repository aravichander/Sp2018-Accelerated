from math import pi 


#Creating class to represent circle object 
class Circle:
	def __init__(self,radius):
		if radius == 0:
			raise ValueError
		elif radius < 0:
			raise ValueError
		else:
			self.radius = float(radius)
			#print("Circle with radius {0:.6f}".format(radius))
	
	def __str__(self):
		return "Circle with radius {0:.6f}".format(self.radius)

	def __repr__(self):
		return "Circle({})".format(self.radius)
	
	@property
	def diameter(self):
		return self.radius*2.0

	@diameter.setter
	def diameter(self,diameter):
		self.radius = (diameter)/2.0

	@property
	def area(self):
		return pi*(self.radius**2)
		#print("Area of circle is {0:.2f}".format(area))

	#not fully understanding this but hoping I did this correctly!

	@classmethod
	def from_diameter(cls, diameter):
		return Circle(diameter / 2.0)

	#being able to add 2 new circles together
	def __add__(self,newcircle):
		if isinstance(newcircle,Circle):
			return Circle(self.radius + newcircle.radius)
		else:
			return Circle(self.radius + newcircle)

	def __mul__(self,factorint):
		return Circle(self.radius*factorint)

	def __eq__(self,other):
		return self.radius == other.radius

	def __lt__(self,other):
		return self.radius < other.radius

	def __gt__(self,other):
		return self.radius > other.radius



circlelist = []
Continue2 = True
while Continue2 == True:
  x = int(input("Input circle radius. Enter 0 to stop.\n"))
  if x < 0:
    Continue2 = False
  elif x == 0:
  	Continue2 = False
  else:
  	c = Circle(x)
  	circlelist.append(c)
print(circlelist)

c =Circle(3)
# print(c)
# print(repr(c))
c2 = Circle(4)
# print(repr(c+c2))
# print(c*2)


#Some statements to ensure comparators are working
print(c == c2)
print(c < c2)
print(c > c2)
print(c == Circle(5))




