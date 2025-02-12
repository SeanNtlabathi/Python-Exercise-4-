    # Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"
def greeting(greet) :
    print(greet)

# TODO: Call the 'greet' function
greeting("hello world")

#------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
name=input("please enter your name :")

def personalized_greeting(greeting) :
    print(f"hello {greeting}")

# TODO: Call the 'personalized_greeting' function with your name
personalized_greeting(name)
#Hello Bukho

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number as a parameter and returns its square
# number=int(input("insert a number :"))

def square(number) :
     answer=number*number
     return answer
# TODO: Call the 'square' function with the number 5 and print the result
print(f"the square of 5 is: {square(5)}")
#25

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
def rectangle_area(length, width) :
    answer=length*width
    return answer
# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result
print(f"the area of a rectangle is: {rectangle_area(4,5)}")

#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument

# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(function,number): 
    return function(number) 
# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double(number):
    return number*2
# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
double= apply_operation(double,7)
print(double)
# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
def square(number):
    return number*number
square= apply_operation(square,3) 
print (square)
   
