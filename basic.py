#variable and datatypes
# variable is used to store the a value.
# datatypes represent the value that is store 
# different type of data types are shown below

a = 10 #int
b = 20 #int
c = 20.5 #float

d= "This is a sample" # string

e = true #bool

#sum of two number
#print is used to print a statement
# quotes are used in case of print statement
print(a + b) # this will give the sum of two number stored in variable a and b  above
print("this is a print statement") 


#list
a = [2,3,4,5,6]
print(a[1]) # this will print the value on 1st position in index it will print 3 as the answer
print(a[2:4]) # this will print the value from 2nd position to 4 position in index excluding 4 position
print(a[2:]) # this will print the value from 2nd position to the end of list
a.append(7)#add value to the end of list
a.pop()#remove value from list
a.remove(2)#it will remove 2 list

#tuple
#these are immutable collections that means cannot be altered or added
#there is no method for append or pop in tuple
b = ("volvo", "mercedez","bmw")
print(b[1])#this will print the value on 1st position in index it will print mercedez as the answer 


#Set
# these contains only unique record and are sorted even if given the duplpicate value output will be unique
#these are also immutable

c = {2,3,4,5,6,1,2,22}
print(c) # will only display output as 1,2,3,4,5,6,22

#Dictionary
#stores information in key-value pairs
b = dict(name="Sam", age=20)
print(b) #output will be like a json format {'name': 'Sam', 'age': 20}
