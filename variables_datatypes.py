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

len(myvar4)                           # length of string
print("Length of myvar4:", len(myvar4))  # prints length of myvar4

myvar4[0:5]                             # string slicing
print("Sliced myvar4:", myvar4[0:6:5])    # prints sliced string
print("Sliced myvar4:", myvar4[0:5:13])    # prints sliced string
print("Sliced myvar4:", myvar4[7:12])    # prints sliced string
print("sliced var4:",myvar4[0:4])            # prints sliced string
print("Sliced myvar4:", myvar4[::12])
print("Sliced and concatenated myvar4:",myvar4[0:5] + myvar4[7:12])  # prints sliced and concatenated string
myvar4.upper()                        # convert string to uppercase
print("Uppercase:",myvar4.upper())     # prints uppercase string
print("Lowercase:",myvar4.lower())    # prints lowercase string

print(myvar4 + "," + " We are learning python.")  # string concatenation

num1 = 10
print(num1, type(num1))                          # check type of num1
num2 = 3.5                     # float
print(num2, type(num2))                           # check type of num2
int(num2)                             # convert float to integer
print("Converted num2 to integer:",int(num2))    # prints converted integer
float(num1)                           # convert integer to float
print("Converted num1 to float:",float(num1))      # prints converted float
num3 = complex(2, 5)               # create complex number
print(num3, type(num3))                        # prints value and type of num3
num4 = complex(num1, num2)         # create complex number from int and float
print(num4, type(num4))                        # prints value and type of num4
print("Real part of num4:", num4.real)      # prints real part of complex number
print("Imaginary part of num4:", num4.imag)  # prints imaginary part of complex number
num5 = float("12.34")              # convert string to float
print(num5, type(num5))                        # prints value and type of num5
myvar8 = "python"
print(myvar8 + str(3.15))  # concatenation of string and float converted to string
bool(0.0)                          # convert float to boolean
print("Boolean value of 0.0:", bool(0.0))      # prints boolean value
bool(5)                            # convert integer to boolean
print("Boolean value of 5:", bool(5))          # prints boolean value
bool("")                           # convert empty string to boolean    
print("Boolean value of empty string:", bool(""))  # prints boolean value
bool("Hello")                     # convert non-empty string to boolean 
print("Boolean value of 'Hello':", bool("Hello"))  # prints boolean value
bool([])                             # convert empty list to boolean
print("Boolean value of empty list:", bool([]))      # prints boolean value
bool([1, 2, 3])                   # convert non-empty list to boolean
print("Boolean value of non-empty list:", bool([1, 2, 3]))  # prints boolean value
bool(())                           # convert empty tuple to boolean
print("Boolean value of empty tuple:", bool(()))      # prints boolean value
bool((0,))                           # convert tuple with zero to boolean
print("Boolean value of tuple with zero:", bool((0,)))  # prints boolean value