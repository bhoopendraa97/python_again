
'''
opps :---------->
class:-class is a blue print of an object------>
object:--object intance of a class------------->physical exitence of a class

1.property--->variable
2.action/behaviour-->methord


property of oops:-->
1.Abtraction----->
2.Encapsalaction  ---->#data-protection

3.Inharitance------->
4.poiymorphism  -------->code reuseblity--->function,mathord

5.contractor --->boject ko intilize karne ke liye

properties of an object-----
variable :---1.
  intance variable
  static variable/class variable
  local variable

bahaviours/action of an object:--2.
    mathods:--
        constractor
        intance mathod
        class mathod
        static mathod  
        self-current class ka current object ka address hold karega --------------------------->
        self is refrence variable the hodl is current class and 
Intance of intance variable
declertion of intance varible--------->        
1.in-side class:-------
      a.thought constructor
      b.thought intance mathod
2. outside class
      a.thought object

calling of intance varible:------------------>
1.in-side class
     a.used self
     b.instance mathord
2. out-side class
  a.use object         

basic syntex:-->class Class_name:
                           doc string
                           varable
                           methord
                           object=class name
                           print(obj.methord)
                            print(obj.varable
'''




# class  student:
#       "student information"
#       name="neeraj"
#       age=37
    

#       def add(a,b):
#           return a+b
# print(dir(student))   
# print(student,'__doc__')   
# print(student,'__dict__')   

# obj=student
# print(obj.name)
# print(obj.age)
# x=obj.add(5,6)
# print(x)


class Student:
    "student information"
    def __init__(self):
        print("constractor called")
        print("self:" ,id(self))

#obj=Student
obj=Student()  #constoractor call response
print(id(obj))















# class Student:
#       "students imformation"
#       name="Mohan"
#       quli="M.Trech"

# print(dir (Student))
# print(Student.__doc__)  
# obj=Student
# print(obj)    





#  With Constructor slove------------------------------------>
class Student:
       def __init__(self,name,age,rollno,garde):
              self.n=name
              self.a=age
              self.r=rollno
              self.g=garde

       def show_detail(self):   
              print(self.n)
              print(self.a)
              print(self.r)
              print(self.g)

obj=Student("neeraj",38,121,"A")                  
obj.show_detail()

               
#  Without Constructor slove------------------------------------>
'''class Student:
         "student information"
         name="Rahul"
         Rollno=121
         Grage="A"
         Age=24

obj=Student
print(obj.name)
print(obj.Rollno)
print(obj.Age)
print(obj.Grage)'''


'''class  student:
      "student information"
      def __init__(self,name,age):
           self.name=name
           self.age=age
      def show_detail(self):
            print(self.name)
            print(self.age)
obj=student("neeraj",37)
obj.show_detail()
obj1=student("rahul",35)
obj1.show_detail()'''


#inside class decleartion and colling-------------->
'''class student:
      def __init__(self,name,age):
                self.name=name
                self.age=age       #declaration
                print(self.name)

      def     add(self,school):
              self.school=school    #declaration
              print(self.name)
      def show_detail(self):
              print(self.name)   #calling
              print(self.age)      #colling
              print(self.school)   #colling
              print(self.city)
obj=student("neeraj",37)
obj.add("shsc")
print(obj.name)   #calling
obj.city="bhopal"
obj.show_detail()     '''  

#inside class decleartion and inside colling-------------->
'''class student:
    def __init__(self,name,age):
         self.name=name
         self.age=age
         print(self.name)
         print(self.age)

    def add(self,school):
         self.school=school
         print(self.school)

obj=student("raj",35)
obj.add("SHCH")'''

#inside class decleartion and colling outside-------------->
'''class student:
     def __init__(self,name,age):
          self.name=name
          self.age=age
     def add(self,school):
           self.school=school
      
obj=student("raj",37)
print(obj.name)
print(obj.age)
obj.add("SCHI")
print(obj.school)'''


# class Student:
#       "student information"
#       def __init__(self,name,rol,marks):
#             self.x=name
#             self.y=rol
#             self.z=marks

#       def __init__(self):
#             print("constractor called")


# obj=Student()
# obj. __init__()     #called outside kar sakte hai----------------------->       










# decleartion inside and calling insind to all varibles------------------->
'''class  student:
      def __init__(self,name,age,school):
            self.name=name
            self.age=age
            self.school=school

      def show_detail(self):
            print(self.name)
            print(self.age)
            print(self.school)

obj=student("name",34,"SCHI")
obj.show_detail()'''



                  
            






          









































