#Open a file
# f=open("main.txt","w") #w  means write mode and r means readable mode and wb means binary mode

# print("the name of the file is ", f.name) #printing the name of the file
# print("the close status of this file is ", f.closed) #closed or not
# print("the  mode of this file is ", f.mode)#show which mode it is open

# string = f.read() # press alt to press multiple cursor
# print(string)

# string= f.write("this is my line 1-written by MainFile.py")n #This is how you overwite a fil
# string=f.write("https://youtu.be/Z1RJmh_OqeA")
# string=f.write("https://www.fullstackpython.com/flask.html")
# string=f.write("https://youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH")
# string=f.write("https://youtu.be/3mwFC4SHY-Y")
# string=f.write("https://flask.palletsprojects.com/en/1.1.x/")
# string=f.write("https://towardsdatascience.com/the-right-way-to-build-an-api-with-python-cd08ab285f8f")
# string=f.write("https://realpython.com/api-integration-in-python/")
# string=f.write("https://www.codementor.io/@sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq")
# string=f.write("https://rapidapi.com/blog/how-to-use-an-api-with-python/")
# string=f.write("https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask")
# string=f.write("https://youtube.com/playlist?list=PLzMcBGfZo4-n4vJJybUVV3Un_NFS5EOgX")
# f.close()

class Employee: #constructor is a function that is use to initialize the object

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def printName(self):
        print("the name of the employee is ", self.name)

    def printSalary(self):
        print("the salary of the employee is ", self.salary)

    harry = Employee("Harry", 5666)
    harry.printName()
    harry.printSalary()



    