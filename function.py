#pre difine 

# inbild function 
#1.print(),2 type, 3 id, list, set, dict, str, org, char------
#user define function 
#def  function(paremerter) 
# type of argument:--positional  o
'''x=10
print(x)
print(print(x))'''

'''def add(x,y,z):
    z=x+y+z
    return z
  #  print(z)
p=int(input("enter 1st value"))
q=int(input("enter 2rnd value"))
r=int(input("enter 3red value"))

x= add(p,q,r)
print(x)'''

'''def add(x,y,z):
    z=x+y+z
    return z
  #  print(z)
p=int(input("enter 1st value"))
q=int(input("enter 2rnd value"))
r=int(input("enter 3red value"))

x= add(y=r,x=p,z=q)
print(x)'''


'''def add(x,y,z):
  
    return x,y,z
  #  print(z)
p=int(input("enter 1st value"))
q=int(input("enter 2rnd value"))
r=int(input("enter 3red value"))

a,b,c= add(y=r,x=p,z=q)
print(a)
print(b)
print(c)'''

# varible_length argument (*, args)

'''def add(* n):
    print(n)
sum=0
for i in n:
	   sum=sum+i
     return sum
var=add(12,20,30,40,50)
print(var)'''

'''x=eval(input("Enter"))
2	print(type(x))
3	print(x)'''


# varible_length argument (**, kwargs)
'''def show (**kwargs):
      print(kwargs)
      for i, j in kwargs.items():
           print(i, "=", j)
show (name="Bhoopendra",age=24,quali="B.Tech")'''

'''x=10   # Global
def show():
        global y
        global z
        y=20
        z=40
        print(x)  #Local
        print(y)
show()
print(x)
print(y)  
print(z)'''

'''x=10   # Global
def show():
        global y
        y=10
        x=50
        print(x)
        print(globals()['x'])
     
     
        
show()
print(x)
print(y)'''

#map function------------------------------------>

'''my_list=[10,20,30,40,50]
def dec(x):
     return x-5
x=map(dec,my_list)
print(tuple(x))   '''


'''my_list=[10,20,30,40,50]
def dec(x):
     return x+5
x=map(dec,my_list)
print(tuple(x))'''

'''my_list=[10,20,30,40,50]
def dec(x):
     return x*5
x=map(dec,my_list)
print(tuple(x))'''

'''my_list=[10,20,30,40,50]
def dec(x):
     return x**2
x=map(dec,my_list) #squre----->
print(tuple(x))'''


'''my_tuple=(70,50,80,40,35)
def grater_50(x):
         if x>50:
           return x
x=list(filter(grater_50,my_tuple))
print(tuple(x)) '''          

'''my_tuple=(70,50,80,40,35)
def dec(x):
         if x%2==0:
           return x
x=list(filter(dec,my_tuple))
print(x) '''


'''my_tuple=(10,20,30,40,50)
def  max_digit(x,y):
            if x>y:
               return x    #find max value-------------->
            else:
              return y
x=reduce(max_digit,my_tuple)
print(x) '''                

'''my_tuple=(10,20,30,40,50)
def  mini_digit(x,y):
            if x<y:
               return x    #find mini value-------------->
            else:
              return y
x=reduce(mini_digit,my_tuple)
print(x) '''























































