# a=(11,12,13,14,15, 'ram', 'shyam', 'mohan')
# print(a[-3])
# print(a[:5])
# print(a[5:])

# #tuple packing

# a=(1)
# print(type(a))
# # output: <class 'int'>
# a=1,
# print(type(a))
# # output: <class 'tuple'>


# # tuple unpacking
# a=123,'Hello',45,56,'World',
# m,n,o,p,q=a
# print(q)
# print(n)
# print(m)
##output: World
##        Hello
##        123


## Transversing (accessing all element at once)
# a=123,'Hello',45,56,'World',
# for i in a:
#     print(i)
# # or
# for i in range(len(a)):
#     print(a[i])
## output is same fo both cases
## 123
## Hello
## 45
## 56
## World

# # TUPLE METHODS
# p=(11,12,13,14,15)
# a,b,c,d,e=p
# r=(11,21,24,21,11,14,11,13,11)
# q=41,42,43
# print(p[1])
# print(p[-2])
# print(p[:3])

# tuple unpacking
# print(a)
# print(d)
##output: 
## 11
## 14



## Tuple packing:
# print (q)
# #output: (41, 42, 43)


# # Methods-1
# print(len(p))
# print(min(p))
# print(max(p))
## output:
## 5
## 11
## 15

# # Method-2
# print(p.index(14))
# print(p.count(11))
# print(r.count(11))
##output: 
## 3
## 1
## 4

# # # SET
# a={9,6,1,2,3,4,5,1,2,4,7,8,2,1,3,0,}
# b={'a','b','c',12,1,2,3}
# print(max(a))
# print(min(a))
# print(a)
# print(len(a))

# Methods of SET

# a.add(25)
# print(a)
# a.pop()
# print(a)

# a.remove(5)
# print(a)

# a.discard(11)
# print(a)


# print(b.union(a))
# print(b|a)
# print(b.intersection(a))
# print(b&a)
# print(b-a)

##### 3-LIST###########################################
# a=[]
# print(a)
# b=list()
# print(b)

# a=[10,11,'Ram',13,]
# print(a)
# b=list((1,2,'a','b',))
# print(b)

## Acessing the element
# print(a[1])
# print(a[1:])
# print(a[-3])


##### Accessing each element by loop
# for i in a:
#     print(i)

# for i in  range(len(a)):
#     print(a[i])

# i=0
# while i<len(a):
#     print(a[i])
#     i = i+1


li= [11,21,2,3,232,4,23,3213123,123,2]
# print(dir(li))

##### used to replace an element 
# li[0] = 1231       
# print(li)

##### used to insert a new element at the end
# li.append('Hello World') 
# print(li)

##### to insert an element to a specific location
# li.insert(5,"Shiv") 
# print(li)


# #### used to delete last element of list
# li.pop() 
# print(li)


#### to delete any specific element of list
# li.remove(232) 
# print(li)


#### to reverse a list
# li.reverse()
# print(li)

#### to print elements in ascending order
# li.sort() 
# print(li)

# #### to print elements in descending order
# li.sort() 
# li.reverse()
# print(li)
# 
# # #### to print elements in descending order by using sort() method
# li.sort(reverse=True) 
# print(li)


# li2 = li.copy()
# print(li2)


# li3 = ['a','b','c','d','e','f']
# li4 = li3 + li
# print(li4)

# li5 = ['a','b','c','d','e','f']
# li5.extend(li)
# print(li5)


# print(li.count(2))

# print(li.clear())




#########################################################
############  DICTIONARY  ###########
#########################################################


# a={}
# print(a)

# b=dict()
# print(b)

# student={'Fname':'Ram','Lname':'kumar','Address':'Mohali', 'zipcode':'123213'}
# print(student['fname'.capitalize()])
# print(student['Address'])

# print(dir(student))


# print(student.get('Address'))

# print(student.keys())
# print(student.values())
# print(student.items())

# student.pop('zipcode')
# print(student)

# print(student)
# student.popitem()
# print(student)

# print(student)
# student.update({'zipcode':'987654'})
# print(student)


# print(student)
# student.update({'city':'Phase 9'})
# print(student)


############ collection practice questions ###########

## 1. Write a program in python to store elements in a list and print them

# x=int(input("How many elements do you want to print ? = "))
# li = []
# for i in range(x):
#     a= int(input(f"Enter element {i+1} = "))
#     li.append(a)

# print(li)
# print("Total = ",sum(li))
# print("Length of list  = ",len(li))
# print("Average  = ",sum(li)/len(li))

### 2. Write a program in python to read n number of values in a list and display them in reverse order.
# x=int(input("How many elements do you want to print ? = "))
# li = []
# for i in range(x):
#     a= int(input(f"Enter element {i+1} = "))
#     li.append(a)

# print(li)
# li.reverse()
# print(li)


#### 4. Write a program in python to copy the elements of one list into another list

# x=int(input("How many elements do you want to print in first list ? = "))
# li = []
# for i in range(x):
#     a= int(input(f"Enter element in first list {i+1} = "))
#     li.append(a)

# y=int(input("How many elements do you want to print in second list ? = "))
# li2 = []
# for i in range(y):
#     a= int(input(f"Enter element in second list {i+1} = "))
#     li2.append(a)

# print(li)
# print(li2)
# li.extend(li2)
# print(li)

#####  5. Write a program in python to count the total number of duplicate elements in an list.

# x=int(input("How many elements do you want to print ? = "))
# li = []
# for i in range(x):
#     a= int(input(f"Enter element {i+1} = "))
#     li.append(a)

# print(li)

# li2=[]
# for i in li:
#     if i not in li2:
#         li2.append(i)

# print(li2)

# # for i in li2:
# #     if li.count(i)>1:
# #         print(i, " = ", li.count(i))

# for i in li2:
#     # if li.count(i)>1:
#     print(i, " = ", li.count(i))

##### 6. Write a program in python to print all unique elements in a list.
# x=int(input("How many element you  want to enter = "))
# li=[]
# for i in range(x):
#     a=int(input(f"enter element {i+1} = "))
#     li.append(a)
# b=list(set(li))
# b.sort()
# print(b)

###### 7. Write a program in python to merge two lists of the same size sorted in descending order.
# x=int(input("How many element do you want to enter in the first list = "))
# li=[]
# for i in range(x):
#     a=int(input(f"enter element {i+1} = "))
#     li.append(a)

# print(li)

# p=int(input("how many element do you want to enter in the second list = "))
# li2=[]
# for j in range(p):
#     c=int(input(f"enter the element {j+1} = "))
#     li2.append(c)
# print(li2)

# li3=li+li2
# li3.sort()
# li3.reverse()
# print(li3)
    
##### 8. Write a program in python to count the frequency of each element of a list.

# x=int(input("How many elements do you want to print ? = "))
# li = []
# for i in range(x):
#     a= int(input(f"Enter element {i+1} = "))
#     li.append(a)

# print(li)

# li2=[]
# for i in li:
#     if i not in li2:
#         li2.append(i)

# print("frequency of an elements")
# for i in li2:
#     print(i, " = ", li.count(i))

##### 9. Write a program in python to find the maximum and minimum elements in list. 
# x=int(input("How many elements do you want to enter = "))
# li=[]
# for i in range(x):
#     a=int(input(f"enter element {i+1} = "))
#     li.append(a)
# print(li)
# print("maximum number of elements = ", max(li))
# print("minimum number of elements = ", min(li))

###### 10. Write a program in python to separate odd and even integers into separate lists
# x=int(input("How many elements you want to enter = "))
# li=[]
# for i in range(1, x+1):
#     a=int(input("enter the element = "))
#     li.append(a)
# print("list of all intergers = ", li)

# even=[]
# odd=[]
# for j in li:
#     if (j%2==0):
#         even.append(j)
#     else:
#         odd.append(j)
# print("the list of even integers = ", even)
# print("the list of odd integers = ", odd)

####### 11. Write a program in python to sort elements of an list in ascending order

# x=int(input("How many element you want to enter = "))
# li=[]
# for i in range(x):
#     a=int(input("Enter the numbers = "))
#     li.append(a)

# li.sort()
# li.reverse()
# print (li)

####### 12. Write a program in python to sort elements of an list in descending order

# x=int(input("How many element you want to enter = "))
# li=[]
# for i in range(x):
#     a=int(input("Enter the numbers = "))
#     li.append(a)

# li.sort()
# print (li)

###### ####### 13. Write a program in python to insert the values in the list (sorted list).

# x=int(input("How many element you want to enter = "))
# li=[]
# for i in range(x):
#     a=int(input("Enter the numbers = "))
#     li.append(a)
# print("list before inserted = ", li)
# li.sort()
# li.insert(4, int(8))
# print ("list after inserted = ", li)

###### 15. Write a program in python to delete an element at a desired position from an list.

# x=int(input("How many element you want to enter = "))
# li=[]
# for i in range(x):
#     a=int(input("Enter element = "))
#     li.append(a)
# li.sort()
# print("list before remove the element at desired position = ", li)
# y=int(input("enter the element you want to delete = "))

# li.remove(y)
# print("list after remove the element at desired position = ", li)
##### 16. Write a program in python to find the second largest element in a list

# x=int(input("How many element you want to print = "))
# li=[]
# for i in range (x):
#     a=int(input("enter element = "))
#     li.append(a)

# li.sort()
# print("Second largest element is:",li[x-2])

###### 17. Write a program in python to find the second smallest element in a list.

# x=int(input("how many element do you want to print = "))
# li=[]
# for i in range (x):
#     a=int(input("enter element = "))
#     li.append(a)
# li.sort()
# li.reverse
# print("the second smallest element of the list = ", li[x-2])

##### 18. Write a program in python for a 2D matrix of size 3x3 and print the matrix.

# x=int(input("Enter the number of rows = "))
# y=int(input("Enter the number columns = "))
# li=[]
# for i in range(x):
#     li2=[]
#     for j in range(y):
#         a=int(input(f"Enter the element at [{i}][{j}] = "))
#         li2.append(a)
#     li.append(li2)

# print(li)
# for i in li:
#     for j in i:
#         print(j , end= " ")
#     print('')

###### 19. Write a program in python for adding two matrices of the same size.
# x=int(input("enter the number of rows of first matrix = "))
# y=int(input("enter the number of columns of first matrix = "))
# li=[]
# for i in range (x):
#     li2=[]
#     for j in range(y):
#         a=int(input(f"Enter the element at [{i}][{j}] = "))
#         li2.append(a)
#     li.append(li2)
# print(li)

# a=int(input("enter the number of rows of second matrix = "))
# b=int(input("enter the number of coloumns of second matrix = "))
# li3=[]
# for i in range (a):
#     li4=[]
#     for j in range (b):
#         c=int(input(f"enter the element at [{i}][{j}] = "))
#         li4.append(c)
#     li3.append(li4)
# print(li3)

# for i in range(len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j]+li3[i][j] , end= " ")
#     print('')

##### 20. Write a program in python for the subtraction of two matrices

# x=int(input("enter the number of rows of first matrix = "))
# y=int(input("enter the number of columns of second matrix = "))
# li=[]
# for i in range (x):
#     li2=[]
#     for j in range (y):
#         z=int(input(f"enter the element at [{i}][{j}] = "))
#         li2.append(z)
#     li.append(li2)
# print(li)

# a=int(input("enter the number of rows of second matrix = "))
# b=int(input("enter the number of colums of second matrix = "))
# li3=[]
# for i in range(a):
#     li4=[]
#     for j in range (b):
#         p=int(input(f"enter tghe elements at [{i}][{j}] = "))
#         li4.append(p)
#     li3.append(li4)
# print(li3)

# for i in range (len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j]-li3[i][j] , end= " ")
#     print('')

###### 21. Write a program in python for the multiplication of two square matrices.
# x=int(input("enter the number of rows of first matrix = "))
# y=int(input("enter the number of columns of second matrix = "))
# li=[]
# for i in range (x):
#     li2=[]
#     for j in range (y):
#         z=int(input(f"enter the element at [{i}][{j}] = "))
#         li2.append(z)
#     li.append(li2)
# print(li)

# a=int(input("enter the number of rows of second matrix = "))
# b=int(input("enter the number of colums of second matrix = "))
# li3=[]
# for i in range(a):
#     li4=[]
#     for j in range (b):
#         p=int(input(f"enter tghe elements at [{i}][{j}] = "))
#         li4.append(p)
#     li3.append(li4)
# print(li3)

# for i in range (len(li)):
#     for j in range(len(li[i])):
#         print(li[i][j]*li3[i][j] , end= " ")
#     print('')


######## 22. Write a program in python to find the transpose of a given squarematrix.
# x=int(input("enter the number of rows of first matrix = "))
# y=int(input("enter the number of columns of second matrix = "))

# li=[]
# for i in range (x):
#     li2=[]
#     for j in range (y):
#         z=int(input(f"Enter the element at [{i}][{j}] = "))
#         li2.append(z)
#     li.append(li2)

# print (li)
# for i in li:
#     for j in i:
#         print(j , end= " ")
#     print('')


# li3=[]
# for i in li:
#     li2=[]
#     for j in i:
#         li2.append(j)
#     li3.append(li2)


# for i in range(len(li)):
#     j=0
#     for j in range(len(li[i])):
#         li3[j][i]=li[i][j]

# print("transpose of the given square matirix \n ", li3)
# for i in li3:
#     for j in i:
#         print(j , end= " ")
#     print('')

 

