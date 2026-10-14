# def addition(a,b):
#     print("Welcome!! ")
#     print("Addition is",a+b)
# addition(10,20)




# for printing the number for 100 times ---------------------------->>>>>>>>>>>>>>



# def addition(a,b):
#     print("Welcome!! ")
#     print("Addition is",a+b)
# for i in range(101):
#     a=int(input("Enter the first number:"))
#     b=int (input("Enter the second number "))
#     addition(a,b)




# Built-in Function---------------------->>>>>>>>>>>>>>



# str1="Saksham Singh"
# print(len(str1))


# user-defined function-------------------------------->>>>>>>>>>>


# this line is uses to define the code using the def 
# and then the variable is used for the function 
# after that we pass parameter is passed means it is used to take input 

# def display(message):
#     print("WELCOME !!")
#     print(message)
# display("Hello World")
# print("="*50)
# display("Hello Saksham")


# Non-parameterized function ----------->>>>


# def display():
#     print("Welcome!!")
#     message=input("Enter message : ")
#     print(message)
# display()
# print('='*60)
# display()
 


# Question ----------------->>>>> Calculate the simple interset




# def simple_interest(p,n,r):
#     print("Principle amount is : ",p)
#     print("Number of years : ",n)
#     print("Rate of interest : ",r)
#     si = (p*n*r)/100
#     print("Simple interest is : ",si)

# simple_interest(10000,5,6.5520)  
# print("=-="*50)
# simple_interest(5000,5,65.3)





# Local Identifiers------------->>>>>>>>>>>>>
# The object defines under the function is called local identifier ...
# and the variable inside the the function is called local scope.....





# def display(name):
#     age = 22     # local variables
#     print(f"{name} has age {age}")
# display("Saksham")

# .... Note ---->>> Parameters are consider as a local variable...




# locals()------->>>




# def display(name):
#     age = 22     # local variables
#     print(f"{name} has age {age}")
#     print(locals())

# display("Saksham")




# how to calculate the length of the variable ------------->>>>>>>>>>>




# def display(name):
#     age = 22     # local variables
#     print(f"{name} has age {age}")
#     print(len(locals()))
#     print(age)
    
# display("Saksham")





# Suppose you have write more than 500 lines of code and after that you want to access any variable from above code then you can easily find it using your function --->>> 
# Let's consider it with an example---->>>




# def display(name):
#     age = 22     # local variables
#     x = 20
#     print(f"{name} has age {age}")
#     # 500 lines of code 
#     variables = locals()
#     print(variables)
#     print(variables['x'])
#     print(age)


# display("Saksham")




# Global Variable ----------------->>>>>>>>>>>

# Consider with an example------>>>>>>


# country = 'India'
# def display():
#     name ="Saksham" # local scope
#     print(name)  
#     print(country) 

# display()



# What if we have same local and global variable----------->>>>>>>>>>


# num = 10
# def display():
#     num = 20 
#     print("Inside : ", num)

# display()
# print("Outside:",num)



# globals()------->>>>>

# name = 'Saksham' #global variable
# def display ():
#     age = 23

# display()
# print(globals())



# UnboundlocalError----------->>>>>  overcome 



# num = 10
# def display():
#     global num 
#     num = num + 5
#     print("Inside:",num)

# display()
# print("Outside :",num)



# Return Statement ------------->>>>>>>>>>>

# Need of return statement-------->>>>>>>>>

# def simple_interest(p,n,r):
#     si = (p*n*r) / 100
#     print("Simple interest is:",si)
#     return si
    

# P = 10000
# N=9
# R = 9.25
# si = simple_interest(P,N,R)
# total = P + si
# print("Total payable amount :",total)



# You can return any type of python object--------->>>>>>>


# def display():
#     return "SAKSHAM"
# print(display())



# You can return multiple values ---------------->>>>>>>>>>>



# def calci(a,b):
#     add = a+b
#     sub = a-b
#     return add,sub
# n1,n2=calci(30,20)
# print("Addition is : ",n1)
# print("Substracton is :",n2)




# def calci(a,b):
#     add = a+b
#     sub = a-b
#     return add,20
# n1,n2=calci(30,20)
# print("Addition is : ",n1)
# print("Substracton is :",n2)





# Default return type is None


# def display():
#     print("Hello World")
# print(display())



# function is an object---------------->>>>>>>>>>>


# def display():
#     print("Hello world")
# print(type(10))



# def display():
#     print("Hello world")
# print(type(display()))



# Creating aliases for function------------->>>>>>>>>
# We can assign different vaiable and call the function..............



# def display():
#     print("Hello world")

# var = display
# var1 = display
# var1()
# display()



# Nested Function --------->>>>>>>>
# A nested function is simply a function defined inside another function ... 



# def outer():
#     print("Hello World!!")
#     def inner ():
#         print("Welcome!!")
#     inner()

# outer()




#Positional argument ------------->>>>>>>>>
# Number of parameter and number of arguments should be same......
# and the value given in the argument is assosiated with parameter......

 

# def display(name,age):
#     print(f"Name is {name} and age is {age}")
# display('Saksham',23)
# display(23,'Saksham')




# Keyword arguments-------------------->>>>>>>>..
# No importance of position here........
# No need to mantain the order.........
# number of argument = number of parameter......



# def display(name,age):
#     print(f"Name is {name} and age is {age}")
# display(name='Saksham',age=23)
# display(age = 23 , name = 'Saksham')


# mixed both positional argument and keyword argument---------->>>>


# def display(name,age):
#     print(f"Name is {name} and age is {age}")
# display('Saksham',age = 23)

# In this case --:--
# Keyword argument  --> positional argument  ....  wrong
# Positional argumnet --> keyword argument   ....  right 




# default Argument----------------->>>>>>>>>>>


# def total_cost(items,currency='USD'):
#     total = sum(items.values())
#     print("Total cost is : ",total,currency)

# cart = {"apple":1.00,"banana":0.75,"orange":1.25}
# total_cost(cart,'INR')



#Another Example ----->>>>

# def total_cost(items={},currency='USD'):
#     print(items)
#     print(currency)
# cart = {"apple":1.00,"banana":0.75,"orange":1.25}
# total_cost(currency = 'INR')  



# How to find the details of default values ---------->>>


# def details(name="xyz",age=0):
#     print(f"Name is {name} and age is {age}")

# details()
# print(details.__defaults__)



# Default argumernts on mutable datatypes----------->>>>>>>>


# def add_item(name,employee_data=[]):
#     employee_data.append(name)
#     print("Update data is : ", employee_data)

# add_item("jay")
# print(add_item.__defaults__)
# add_item("viru")
# print(add_item.__defaults__)
# add_item("basanti")
# print(add_item.__defaults__)
# add_item("thakur")
# print(add_item.__defaults__)


# To avoid from this we can............



# def add_item(name,employee_data=None):
#     if employee_data is None:
#         employee_data=[]
#     employee_data.append(name)
#     print("Update data is : ", employee_data)

# add_item("jay")
# add_item("viru")
# add_item("basanti")
# add_item("thakur")


# Variable length positional arguments ----------------->>>>>>>>>>
# in this we get tuple when we simply not return the function..........

# def addition(*nums):
#     sum1 = 0
#     for n in nums :
#         sum1 = sum1 + n 
#     return sum1

# print(addition(10,20,30))
# print(addition(10,20))
# print(addition(10,20,30,40))




# Variable length keywords arguments ------------->>>>>
# in this we get dictionary when we simply not return the function.........

# def addition(**nums):
#    print(nums)

# print(addition(n1=10,n2=20,n3=30))
# print(addition(n1=10,n2=20))
# print(addition(n1=10,n2=20,n3=30,n4=40))




# def addition(**nums):
#    return sum(nums.values())

# print(addition(n1=10,n2=20,n3=30))
# print(addition(n1=10,n2=20))
# print(addition(n1=10,n2=20,n3=30,n4=40))



# Mixing variable length keyword and positional argument ---------------->>>>>>>>>>>>>>>


# def addition(*num,**nums):
#     return sum (nums.values())

# print(addition(100,200,300,n1=10,n2=200))



# positional arguments --->> variable length positional arguments -->> keywords argumnents -->> variable length keyword arguments -->> default arguments





# Lambda Function --------------------->>>>>>>>>>>>>>>>


# add=lambda x,y:x+y
# print(add(10,20))
# print(type(add))


# add= lambda:print("Hello World")
# add()  



# add = lambda x,y : (x+y,x-y)
# addition,subtraction = (30,10)
# print("Addition is :",addition)
# print("Subtraction is :",subtraction)



# Using Lambda with the sorted() Function---------------->>>>>>


# print(sorted([10,20,5,3,6,9,8,20]))

# print(sorted(['Shivangi','Saksham','suar','macchar']))


#On the basis of their len short the name ---------------->>>>>>>>>>


# print(sorted(['Shivangi','Saksham','suar','macchar'],key=len)) 


# lambda nm:nm.split()[1]
# data = ['Sharma Rohit', 'Kohli Virat', 'Tendulkar Sachin', 'Raina Suresh', 'Gill Shubman', 'Kishan Ishan']
# print(sorted(data,key=lambda nm:nm.split()[1]))




# Nested Lambda Function------------->>>>>>>>>>>


# def outer():
#     return lambda  num1, num2: num1+num2
# add = outer()
# print(add(3,4))


#  For outer function ----->>>>.


# outer = lambda : lambda num1,num2:num1+num2
# add = outer()
# print(add(3,4))




# Pthon Lambda FUnction with if -else------------------->>>>>>>>>>





