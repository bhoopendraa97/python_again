
# filter() higher order function ----------------
'''my_list=[60,10,70,90,55,75,10,20,40]
def fun(n):
    if n>=60:
      return True
x=filter(fun , my_list)
print(list(x))'''


'''def even(number):
       if number%2==0:
               return True
       else:
               return False
numbers=[1,2,3,4,5,6,7,8]
even_number=filter(even,numbers)
print(list(even_number))'''


'''my_list=[1,2,3,4,5,6,7,8,9]
def is_prime(n):
     if n<2:
        return False
     for i in range(2,int(n**0.5)+1):    
        if n%i==0:
            return False
     return True

x=filter(is_prime,my_list)
print(list(x)) '''            

             

      





               
                  















  



      













    

       








     
     

          
      






'''def odd(number):
       if number%2!=0:
              return True
       else:
              return False

number=[1,3,4,6,5,7]
odd_numbers=filter(odd,number)
print(list(odd_numbers)) '''          
            
                


