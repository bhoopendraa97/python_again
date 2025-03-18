
'''
property
1) inheritance -----> parent,child relat
'''
# MRO->mathod resolution order
#Single Level Inheitance-------------------->init hi consector hotaa hai------------>
'''class P:
     def __init__(self,p_name):
          self.x=p_name

     def p_properties (self,home,bank):
          self.h=home
          self.b=bank

class C(P):
     def c_prpperty(self,qualification):
          self.q=qualification
          print(self.x)
          print(self.h)
          print(self.b)
          print(self.q)
                    
obj=C("Neeraj")
obj.p_properties("Bhopal","Sbi")
obj.c_prpperty("M.Tech")'''

  ####################mathod overloding#############################>
'''class parent:
    x=10
    def home(self):
        parent("parent home")

class Child(parent):
    y=10
    def home(self):
        super().home()
        print("child car")

obj=Child()
obj.home()   '''     


'''class parent1:
    def home(self):
        print("parent1 home")


class parent2:
    def home(self):
        print("parent2 home")


class Child(parent1,parent2):
    def car(self):
        print("child car") 

obj=Child()
obj.car() '''              


#####################################################>
'''class Parent:
       def __init__(self,p_home,p_bank):
              self.p_h=p_home
              self.p_b=p_bank

class Chaild(Parent):
       def c_property(self,c_home,c_bank):
               self.c_h=c_home
               self.c_b=c_bank

       def show_detail(self): 
              print(self.p_h)
              print(self.p_b)
              print(self.c_h)
              print(self.c_b)

obj=Chaild("indore","Sbi")
obj.c_property("bhopal","Pnb")
obj.show_detail()  '''                                 


#Multi Level Inharitance-------------------------->
'''class Gf:
    def name(self,name):
        self.n1=name
class P(Gf):
    def __init__(self,P_name):
        self.x=P_name
    def p_properties(self,name,bank):
        self.n=name
        self.b=bank

class C(P):
    def c_property(self,qualification):
        self.q=qualification
        print(self.x)
        self.p_properties("Indore","SBI")
        print(self.n)
        print(self.b)
        
        print(self.q)
        self.name("Dada")
        print(self.n1)
obj=C("Neeraj") 
#obj.p_properties('bhopal','hdfc')
obj.c_property('B-Tech')'''
#####################################################>
'''class GF:
      def __init__(self,gf_name):
              self.gf_n=gf_name

class Father(GF):
       def f_property(self,f_name):
               self.f=f_name

class Child(Father):
        def c_property(self,c_name):
               self.c=c_name

        def Show_detail(self):  
               print(self.gf_n)
               print(self.f)
               print(self.c)

obj=Child("mr.Damoder")
obj.f_property("raj malhotra")     
obj.c_property("mohan das")
obj.Show_detail()   '''           


#Multiple Inharitance-------------------------->

'''class Father:
     def property(self,f_name,f_bank):
          self.n1="f_name"
          self.b="f_bank"
          print(self.n1)
          print(self.b)

class Mather:
     def property1(self,m_name,m_bank):
               self.n1="m_name"
               self.b="m_bank"
               print(self.n1)
               print(self.b)

class Son(Father,Mather):
      pass

obj=Son()
obj.property("rahul","sbi")
obj.property1("raj","sci")'''
###################################################################
'''class Father:
      def __init__(self,f_name):
            self.f_n=f_name

class Mother:
      def m_property(self,m_name):
            self.m_n=m_name

class Son(Father,Mother):
      def s_property(self,s_name):
            self.s_name=s_name

      def show_detail(self):
            print(self.f_n)
            print(self.m_n)
            print(self.s_name)

obj=Son("sunny")
obj.m_property("sajal")
obj.s_property("raj")
obj.show_detail()'''
            
'''class Father:
      def property(self,f_name, f_bank):
              self.n1=f_name
              self.b= f_bank
              print(self.n1)
              print(self.b)

class Mother:
       def property1(self,m_name,m_bank):
               self.n1=m_name
               self.b=m_bank
               print(self.n1)
               print(self.b)

class Son(Father,Mother):
         pass

obj=Son()
obj.property("raj","sbi")
obj.property1("meena","pnb")'''


#hybrid inharitance------------------->
'''class A:

class B(A):

class C:

class D(B,C)

class E(D):'''
#Hierarchical Inharitence---------------------------------------------------------------------------->
'''class Parent:
      def home(self):
            print("from parent class")

class Child1(Parent):
      def home1(self):
           # print("from child1 class")
            super().home()

class child2 (Parent):
      def home2(self):
            print("from child2 class")

obj1=Child1()
obj1.home()
obj2=child2()
obj2.home()  '''



# Hybrid Inharitance---------------------------------------------------------------------------------------->
'''class Bike:
      def company(self,hero,honda):
            self.h="hero"
            self.h1="honda"
            print(self.h)
            print(self.h1)

class Car(Bike):
         def company1(self,suzki,mahindra):
               self.s="suzki"
               self.m="mahindra"
               print(self.s)
               print(self.m)

class Bus:
       def company3(self,tata,eicher):
             self.t="tata"
             self.m="eicher"
             print(self.t)
             print(self.m)

class Plane(Car,Bus):
     def company4(self,indego,qatar):
            self.i="indego"
            self.q="qatar"
            print(self.i)
            print(self.q)

class Countary(Plane):
       def company5(self,india,england):
              self.i="india"
              self.e="england"
              print(self.i)
              print(self.e)

obj=Countary()
obj.company("splender","cd")
obj.company1("ciaz","thar")
obj.company3("gf","jh")
obj.company4("dr","fg")
obj.company5("se","sd")'''

'''class A:
     def __init__(self,a_bank):
          self.a_b=a_bank

class B(A):
     def b_property(self,b_bank):
          self.b_b=b_bank

class C:
     def c_property(self,c_bank):
           self.c_b=c_bank

class E(C,B):
     def e_property(self,e_bank):
          self.e_b=e_bank

     def show_property(self):
          print(self.a_b)
          print(self.b_b)
          print(self.c_b)
          print(self.e_b)
obj=E("Sbi")
obj.b_property("Pnb")
obj.c_property("Boi") 
obj.e_property("Dsi") 
obj.show_property()   '''          

#(child__mro__)
#Mathord overloding----------------------------------->
#polymorphisham same =function with different argument
#overloding ko avoid karne ke liye hum sing * ka use karte hai------


# overloding ------------------------->   
'''class A:
      def add(self,x,y):
           return x+y

      def add(self, x,y,z):
          return x+y+z

obj=A()
obj.add(10,20,7)                         
x=obj.add(2,4)
print(x)'''

'''class A:
      def add(self,*n):
            sum=0
            for i in n:
                  sum=sum+i
            return sum

obj=A()
x=obj.add(10,20)
print(x)
y=obj.add(10,2,5)
print(y)'''

    #python support hai------>overRiding mathod----->
    #class mein function nahi hai
    #pthon overloding support nahi karta hai
    #args variable length orgument tuple(*)---->
    # kwars(**)







