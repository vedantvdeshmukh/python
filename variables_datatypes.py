myvar1 = 19                         # integer
print(myvar1, type(myvar1))         # prints value and type of myvar1
myvar2 = 5.31                       # float
print(myvar2,type(myvar2))          # prints value and type of myvar2
myvar3 = 3 + 8j                     # complex number      
print(myvar3,type(myvar3))          # prints value and type of myvar3
myvar4 = "Hello, World!"            # string    
print(myvar4,type(myvar4))          # prints value and type of myvar4
myvar5 = '''this is also a string
that spans multiple lines'''        # multi-line string
print(myvar5,type(myvar5))          # prints value and type of myvar5
myvar6 = [10, 20, 30, 40, "apple", 3.14]          # list
print(myvar3,type(myvar3))          # prints value and type of myvar3
myvar7 = (100, 200, 300, "banana", 2.71)        # tuple
print(myvar7,type(myvar7))          # prints value and type of myvar7

myvar = int(input("Enter a value: "))  # input from user
print("You entered:", myvar,type(myvar))      # prints the entered value