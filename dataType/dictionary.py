# Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element 
# Dictionary holds key:value pair. Key-value is provided in the dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon :, whereas each key is separated by a ‘comma’
# Creating an empty Dictionary 
Dict0 = {} 
print("Empty Dictionary: ") 
print(Dict0) 
# Creating a Dictionary  
# with Mixed keys 
Dict1 = {'Name': 'Geeks', 1: [1, 2, 3, 4]} 
print("\nDictionary with the use of Mixed Keys: ") 
print(Dict1) 
    
# Creating a Dictionary 
# with dict() method 
Dict2 = dict({1: 'Geeks', 2: 'For', 3:'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict2) 
    
# Creating a Dictionary 
# with each item as a Pair 
Dict3 = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict3) 

# accessing a element from a Dictionary  
    
# Creating a Dictionary  
Dict4 = {1: 'Geeks', 'name': 'For', 3: 'Geeks'} 
    
# accessing a element using key 
print("Accessing a element using key:") 
print(Dict4[1]) 
  
# accessing a element using get() 
# method 
print("Accessing a element using get method:") 
print(Dict4.get('name')) 