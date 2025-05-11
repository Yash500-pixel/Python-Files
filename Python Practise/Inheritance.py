#Single Inheritance #Multiple Inheritance #Multilevel Inheritance # Super Method # Super Method #Instance method #Staticmethod #classmethod #Dunder Functions

# Lecture (9)


class student:
  def __init__(self,phy,chem,maths):
    self.phy = phy
    self.chem = chem
    self.maths = maths
  @property
  def percent(self):
    self.percentage = str((self.phy+self.chem+self.maths)/3)
    return self.percentage


s1 = student(100,200,300)
#print(s1.percent())

s1.maths = 20
print(s1.percent)

class complex():
  def __init__(self,real,img):
    self.real = real
    self.img = img
  def shownum(self):
    self.add = self.real,self.img
    print(self.add)
num1 = complex(3,5)
num1.shownum()


class circle:
  def __init__(self,radius,pi = 3.14):
    self.radius = radius
    self.pi = pi
  def Area(self):
    self.area = (self.pi*self.radius*self.radius)
    print(self.area)
  def perimeter(self):
    self.perimeter = 2*(self.pi*self.radius*self.radius)
    return self.perimeter
c1 = circle(5)
print(c1.Area())
print (c1.perimeter())

class Employee:
  def __init__(self,role,department,salary):
    self.role = role
    self.department = department
    self.salary = salary
  def showdetails(self):
    print(self.role, 
    self.department, 
    self.salary)

#e1 = Employee("SD","IT",50000)
#print(e1.showdetails())
class Engineer(Employee):
  def __init__(self,name,age):
    self.name = name
    self.age = age
    super().__init__("SD","IT",50000)
  

e1 = Engineer("Yash","22")
print(e1.showdetails())

class order:
  def __init__(self,order,price):
    self.order = order
    self.price = price
  def show(self):
    print( self.order,self.price)
  def __gt__(self,a2):
    return self.price>a2.price
a1 = order("butter",77)
a2 = order("Cream",89)
print(a1<a2)



