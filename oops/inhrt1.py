### multilevel inheritance....

class person:
	def f1(self):
		print("Class person")

class student(person):
    def f2(self):
     	print("Class student") 

class engStudent(student):
 	def f3 (self):
 		print("Class engStudent ")

ob=engStudent()
ob.f1()
ob.f2()
ob.f3()