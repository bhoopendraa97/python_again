
# Q.1) given the following structure------------>
'''data=[10,[2.5, "apple"], (3,4)]
print(data[1][1])  # "apple"------------>

#Q.2)  given the following structure------------>
mixed=[[1,2],  (3.5, "grape"), [4,5,6]]
print(mixed[1][0]) # 3.5

#Q.3)  given the following structure------------>

elements=[100, (200, 300), ["a", "b", "c"]]
print(elements[2][1]) # b

#Q.4)  given the following structure------------>
data=[[10,20], (30,40, 50)]
print(data[0][0]) # 10

#Q.5)  given the following structure------------>
values=[(1.5, 2.5), [3, 4], 5]
print(values[0][1])  # 2.5

#Q.6)  given the following structure------------>
numbers=[[5, 10], (15, 20)]
print(numbers[1][1]) # 20

#Q.7)  given the following structure------------>
shapes=["circle", (5, 10), [15, 20, 25]]
print(shapes[2][0]) # 15

#Q.8)  given the following structure------------>
matrix=[[1, 2,3], [4,5,6], [7,8,9]]
print(matrix[1][2]) # 6

#Q.9)  given the following structure------------>
data=[(1,2,3), [4,5,6]]
data[0][1]=10
print(data)  # "tuple" object not support item assignment

#Q.10)  given the following structure------------>
data=[[1,2], (3.5, 4.5)]
data[1][0]=7.5
print(data) # "tuple" object not support item assignment'''

# Topic:---slicing mathord--------->

#       0 1  2     3     4  5  6   7     8  9 10
'''lis1=[12,3,44, 'danish',56,7,88,'ankur',33,4,5]
#    -11 -10 -9   -8    -7 -6 -5   -4    -3 -2 -1

a=lis1[7:] #index number 7 and 7 ke baad wale number bhi print karyega----->
print(a)

b=lis1[2:]
print(b)

c=lis1[7:2:-1]
print(c)

#a=lis1[7:2:-1]
#print(a)
# a=lis1[-4:-9:-1]
# print(a)
# a= lis1[::-1]
# print(a)'''

#dictionary

'''d={1: "mom", 2: "tue", 3: "wed"}
d.update({4:"thus"})
d[5]="fri"
print(d)'''

#
'''d={1:["ajay", 23, "bhopal"] ,2:["danish", 23, "ujjain"]}
d[2][2]="indore"
print(d)

d={1:["ajay", 23, "bhopal"] ,2:["danish", 23, "ujjain"]}
print(d)
print(d[1])
print(d[1][2])

#d.update ({2: ["ajay",23, "indore"]})
#d[2][2]="indore"
#print(d)'''


'''d1={101: {"name": "ajay", "age":23, "city": "bhopal"},102: {"name": "danish", "age":23, "city":" indore"}}
d1[102]["city"]="ujjain"
print(d1)
d1[102].update({"city": "ujjain"})
print(d1)'''

'''d={1: "mon",-2:"tue", 3: "wed"}
# key()
keys=sorted(d.keys()) # keys only keys deti hai----------ghatahe oder mein 
print(keys)
# values()
values=d.values() # value only value deta hai-----
print(type(values))

#items
items=d.items()
print(items)  #items key and value dono deta hai------typeof se data type operation use karte hai



sorted_keys=sorted(d.keys()) #
print(keys,type(keys))'''


#method of dict
#zip() function--------------------------------------------------
'''Name=["ajay", "danish", "raj","sonam", "naman"]
age=[23,23,45,24,26]

result=dict(zip(Name,age))#disnerey
print(result)
result=tuple(zip(Name,age)) #tuple
print(result)
result=list(zip(Name,age))# list
print(result)'''

#get() function ----------------------------------------------->
data={'ajay':23, 'vikas':23, 'Arun':45}
a=data["Arun"]
print(a)

a=data.get('Arun')
print(a)

# setdefault()------------------------------->disnaray function
#key abalable---> return exting value
# key not avaliable----> key--value pair add, 
# retuen added value 

'''data={'1':2390, '2':2387, '3':4522}

value= data.setdefault('1', 6666)
print(value)

value= data.setdefault('11', 6666)
print(data)
print(value)'''

#pop() , popitem(), ---->return
#clear

'''data={'1':2390, '2':2387, '3':4522}
print(data)
value=data.pop('2') # pop clean karta hai---
print(data)
print(value)

value=data.popitem()
print(data)
print(value)'''



'''data={'1':2390, '2': 2387, '3': 4533, '4': {'11': 3523, '22': 6534, '44': 4575}}
nested_dict=data['4']
print(nested_dict)          #nasted dictnery mein pahle ham list banayege and then using pop function---->
nested_dict.pop('44')
print(data)'''

'''data={'1':2390, '2': 2387, '3': 4533, '4': {'11': 3523, '22': 6534, '44': 4575}}
print(type(data['1']))

print(type(data))
print(type(data['4']))
data['4'].popitem()
print(data)
data.popitem()'''

#set data type() function--------------->collection of data
#duplication are not allow
#set is a unoder data type odre are not import

''''   
set is a conrainer in which we catain multiple data, but duplication is not allow and
unorderd data type 

where our main concern is data, but not any order related to it , then we use set

'''

'''s1={1,2,3,3,4,9,11}
s2={4,5,17,89}
s3={"a","b", 1,2,3,88}

#print(s1)
#print(type(s1))

#r=s1.union (s2,s3)
#print(r)
r=s1|s2|s3
print(r)
#r=s1.union(s2)
#print(r)

#res1.intersection
#r=s1&s2
#print(r)
#intersection common------

#r=s1.intersection(s2,s3)
#print(r)



#set difference
#r=s1.difference(s1,s3)    
#print(r)'''               

'''#intersection common---
#r=s1.intersection(s2,s3)
#print(r)

##set difference
r=s2.difference(s1)
print(r)'''

'''s1={'a', 'a', 'b', 'f', 'y', 't'}
s2={'b', 'y', '1', '6', '7'}
r=s1.difference(s2)
print(r)

#update
s1={1,2,3,4,3,9,11,17}# new element add karta hai
s2={34,55}
s1.update(s2)
print(s1)'''

'''s1.update(s2)  #list tuple sabhi add ho sakte hai----
print(s1)

s1.union(s2) #union return karta hai value ko isko new varivale mein istore karna hotaa hai---
print(s1)'''

'''s1={1,2,3,4,3,9,11,17}
s1.update((2,90,99)) #tuple
print(s1)'''

'''s1={1,2,3,4,3,9,11,17}
s1.add((2,90,9))
print(s1)'''

































