
# Set
#  Set is an unordered collection of data type that is iterable, mutable and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.
# Python program to demonstrate  
# Creation of Set in Python 
    
# Creating a Set 
set1 = set() 
print("Initial blank Set: ") 
print(set1)    
# Creating a Set   
set1 = set("GeeksForGeeks") 
print("\nSet with the use of String: ") 
print(set1) 
  
# Creating a Set 
 
set2 = set(["Geeks", "For", "Geeks"]) 
#N.B:can't print the duplicate value
print("Set with the use of List: ") 
print(set2) 
# Creating a Set with  
# a mixed type of values 
set3 = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks']) 
print("Set with the use of Mixed Values") 
print(set3) 
# we can access set element by using loop