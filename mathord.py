#constractor mein self intance mathord----------
#mathord:----
#intance mathord:-1

'''class A:
      def new(self):
            print("1 st mathord")
      def new1(self):
            self.new()
            print("2 nd methord")

obj=A()
#obj.new()
obj.new1()   '''         
                 
#class mathord:-2.                      --------------->
#static variable kio modify karne ke liye hum class mathord ka use kartye hai--------

class Book:
     price=150

     def __init__(self,author,pages):
           self.author=author
           self.pages=pages
     @classmethod  

     def update_price(cls,price):
             cls.price=price
     def show_details(self):
           print(self.author)
           print(self.price)
           print(self.pages)

obj=Book("neeraj",450)
obj.show_details()   
obj.update_price(200)
obj.show_details()        
                        




























