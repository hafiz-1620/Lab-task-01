print("Hello,World!")

#Condition
if 5>2:
    print("Five is geater than two")  #This is indentation.
"""
Indentation is a proccess to indentify
any block.
"""
age=22
if (age>18):
      print("You can Vote")
else:
      print("You can't Vote")

#Variable
x=5
x="Mehedi Hasan"
y="HIRA"    
print(x)
print(y)

#Casting
x="3"
x=int(x)
y=5
print(x+y)

#Get Type
x="3"
y=5
print(type(x))
print(type(y))

#Camel Case
myVariablename="Hira"
print(myVariablename)
#Pascal Case
MyVariableName="Mehedi"
print(MyVariableName)

#Snake Case
my_variable_name=55
print(my_variable_name)

#multiple variables
x, y, z = "Orange", "Banana", 5
print(x)
print(y)
print(z)

#unpack
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python"
y = "is "
z = "awesome"
print(x + y + z)

#For Loop
for i in range(0, 10, 2): 
    print(i) 

#While loop
count = 0
while (count < 3): 
    count = count + 1
    print("Hello World!")

#Global
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#function
def add(x,y):
    sum=x+y
    print(sum)
add(5,6)
