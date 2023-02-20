# Sequence Type: sequence is the ordered collection of similar or different data types. Sequences allows to store multiple values in an organized and efficient fashion. 
# String
# List
# Tuple
# they are sequence data type in python

#String: 
String1 = 'Welcome to python world'
# multiline string, and explore triple quote
String2 = '''"python" is not snake. 
Don't scare'''
# string are arrange such a way that you access them using indexing concept. 
# left to right 0 --> n
# right to left -1 --> -n
print(String1) 
print(String2) 
print(String2[0]) # here we get the first ch
print(String2[-1]) # here we get last ch 

# List: 
numbers = [1, 2, 3, 4, 5] # creating and putting values to string in python

print(numbers) # print the whole list

print(numbers[0]) #accessing first index
print(numbers[-1]) #accessing last index
numbers[-1]=7 # changing index value
print(numbers) # print the whole list

#  Tuple
#  tuple is also an ordered collection of Python objects. The only difference between tuple and list is that tuples are immutable i.e. tuples cannot be modified after it is created.
name=("Hello world")
print(name) #print the tuple object

# Creating a Tuple  
# with nested tuples 
tuple1 = (0, 1, 2, 3) 
tuple2 = ('python', 'geek') 
tuple3 = (tuple1, tuple2) 
print("\nTuple with nested tuples: ") 
print(tuple3) 
# Accessing element using indexing
print("First element of tuple")
print(tuple1[0])
# Accessing element from last
# negative indexing
print("\nLast element of tuple")
print(tuple1[-1])
  
print("\nThird last element of tuple")
print(tuple1[-3])
