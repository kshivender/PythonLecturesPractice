# a=(11,12,13,14,15, 'ram', 'shyam', 'mohan')
# print(a[-3])

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

# # SET
a={9,6,1,2,3,4,5,1,2,4,7,8,2,1,3,0,'a'}
b={'a','b','c',12,1,2,3}
# print(max(a))
# print(min(a))

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

##### 3-LIST
# a=[]
# print(a)
# b=list()
# print(b)

a=[10,11,'Ram',13,]
# print(a)
b=list((1,2,'a','b',))
# print(b)

## Acessing the element
# print(a[1])
# print(a[1:])
# print(a[-3])


##### Accessing each element by loop
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])

# i=0
# while i<len(a):
#     print(a[i])
#     i = i+1


# li= [11,21,2,3,232,4,23,3213123,123,2]
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

student={'Fname':'Ram','Lname':'kumar','Address':'Mohali', 'zipcode':'123213'}
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