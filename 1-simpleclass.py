#syntax
#class classname:
# 'Optional class documentation string'
# class_suite

#1_simple class.py
class Student:
    " Common base class for all students "
    studentcount = 0
    def __init__(self,rollno,name,course):
             self.rollno= rollno
             self.name= name
             self.course=course
             Student.studentcount+= 1

    def displayCount(self):
             print("Total Number of Students =",Student.studentcount)
    def displayStudent(self):
             print(" Roll Number:", self.rollno)
             print(" Name:", self.name)
             print(" Course:", self.course)
            
            
std1=Student(1,"ram","b.tech")
std2=Student(7," raj","m.tech")
std1.displayStudent()
std2.displayStudent()
print("Total Number of Students :",Student.studentcount)

              
              



             
