# Basic print statement
print("hello World")
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
#l1=[22,23,2,3,2,3,3]
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
a=22
b=21
c=15


d = input("Enter your name:") # if you enter any(string,number,float) input in the user it will be stored as string
d = int(d)
"""
 #typecasting convertd a data type into another data type
d = float(d)
d = str(d)
"""

print(type(d)) 

if(d>a):
    print("d Enter the number)

else:
    print("d is not greater than a ")

