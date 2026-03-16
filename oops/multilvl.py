class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def show_person(self):
		print("Name :",self.name)
		print("Age :",self.age)

class Student(Person):
	def __init__(self,name,age,roll):
		super().__init__(name,age)
		self.roll=roll

	def show_student(self):
	    print("Roll No :",self.roll)

class EnggStudent(Student):
    def __init__(self,name,age,roll,branch):
    	super().__init__(name,age,roll)          #calling student constructor
    	self.branch=branch                       #property
    def show_engg(self):
        print("branch :",self.branch)

e =EnggStudent("anish",21,1,"computer science")
e.show_person()
#Calling methods
e.show_student()
e.show_engg()
