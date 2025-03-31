
'''x=lambda x,y,z,p,q,r: x+y-z/p%q//r
print(x(1,2,3,4,5,6))

y=lambda x:x**2
print("5 qure=",y(5))

y=lambda x:x-2
print(y(5))'''


'''my_list=[10,15,20,25,30,35,40,45,50]
x=list(filter(lambda x: x%2==0,my_list))  #print even number--------------->
print("even number=",x)


my_list=[10,15,20,25,30,35,40,45,50]
x=list(filter(lambda x: x%2!=0,my_list))   #print odd number--------------------->
print("odd number=",x)'''

from functools  import reduce

'''my_list=[10,15,20,25,30,35,40,45,50]
x=list(filter(lambda x: x%2!=0,my_list)) 
y=reduce(lambda x,y: x+y,x)
print("total=",y)'''











'''my_list=[10,15,20,25,30,35,40,45,50]
x=list(filter(lambda x: x%2==0,my_list)) 
print("Even number=",x)

z=list(map(lambda x: x**2,x))
print("Even number squre=",z)

g=reduce(lambda x, y: x+y,z)
print("Total of even number squre=",g)'''

'''my_list=[10,15,20,25,30,35,40,45,50]
x=list(filter(lambda x: x%2==0,my_list)) 
print("Even number=",x)

y=reduce(lambda x,y:x+y,x)
print("sum of even number=",y)

z=map(lambda y: y**2,y)
print("sum of sqre=",z)'''



