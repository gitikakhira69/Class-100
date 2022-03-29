class Student(object):
    def _init_(self,name,age,gender,level,grade=None):
        self.name = name
        self.age = age 
        self.gender = gender
        self.level = level
        self.grade = grade or {}
    
    def setgrade(self,course,grade):
        self.grade[course] = grade

    def getgrade(self,course):
        return self.grade[course]

Gitika = Student("GITIKA",17,"Female",1,{"Maths":3})
Neeraj = Student("NEERAJ",13,"Male",2,{"Science":8})

       