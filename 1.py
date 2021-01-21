# Basic print statement
print("hello World")
print("Welcome to python tutorial")
# comments  in Python
"""
I am a multiline comment
"""

# python variable(use to store data)
x=34 #x is an integer
y=3.5 # float variable
string= "ako si pogi"
# print (x,string,y) 

"""
Rules for creatinf variable in python
1. It must start with a letter or an underscore
2. It cannot start with a number
3. It can only contain alphanumeric characters or an _
"""
string2="142"
# print(type(string2)) # type command so you know what data type is being display

a=34
b=3
#this is how you do operators in ptyhon
"""
print("the value of a+ b is",a+b)
print("the value of a-b is",a-b)
print("the value of a* b is",a*b)
print("the value of a/b is",a/b)
print("the value of a // b is",a//b)
3. It can only contain alphanumeric characters or an _
"""
#Python Collection (Arrays)
'''
There are 4 types of collection in pyhton:
1.list
2.tuple
3.set
4. dictionary
'''
# l1=[22,23,2,3,2,3,3]
# print("My first list is here: ",l1)
# print("My first value list is here: ",l1[0])

# l1.append(34) #add at the end
# l1.pop(2)
# l1.remove(25)
# l1.clear()

#tuples
# t1=(1,2,13,3,)
# values cannot be changed

# sets in python
# myset={1,2,23,3,33,13,123}
# print(myset)


myDictionary= {  #the same as object in java key-value pair
    "harry" : "Good boy",
    "mac"   : "Bad boy",
    "sam"   : "only boy",
    "marks" : 1255
}

#syntax for getting value
# print(myDictionary["sam"])
# print(myDictionary.get("marks"))

# myDictionary["marks"]=15 # change value of a certain key


# If else condition in python 



# d = input("Enter your name:") # if you enter any(string,number,float) input in the user it will be stored as string
# d = int(d)
"""
 #typecasting convertd a data type into another data type
d = float(d)
d = str(d)
"""

# print(type(d)) 

'''
equals ==
greater >
less than <
less than or equal to <=
greater than or equal to >=
'''
"""
a=22
b=21
c=15
d=39

if(d>a):
    print("d is greater")

elif (d==a):
    print("d is equal")

else: 
    print("d is not greater ")

"""

#Loops in python
'''
i=0

while(i<20): #loop until the condition is met
    print('hello')
    i=i+1
'''
# for i in range(0,12): #range from 0 to 11

fruits =["Grapes","Guava","apple","Oranges"]

# for item in fruits:
#     print("Hello " + item) # can only concat string to string
#     if item =="Oranges":
#         print("Oranges found")
#         break #break can be used to if you want to get out of the loop in this case if the word is found get out of the loop
#         continue #if you use continue in this case the last item will not be printed and it will just continue the condition

#function are something that performs an action 


# def printList(List1,greet): #indent always so it will recognize
#     print (greet)  #what ever you right
#     for item in List1:
#         print("The value of the item is: ", item)


# printList(fruits,"Welcome I print you this items")

    