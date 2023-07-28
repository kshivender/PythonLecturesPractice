# print(range(10))
# for a in range(10):
#     print(a)

# for a in range(10):
#     print(a,end=" - ")
    

# for i in range(20,30,2):
#     print(i)


# for i in range(100,1,-1):
#     print(i)

# for i in range(500,1000,78):
#     print(i)

# i=0
# while i<10:
#     print(i)
#     i=i+3

# i=20
# while i<100:
#     print(i)
#     i=i+4 

# for i in range (1,100):
#     if i%2==0:
#         print(i)

# i=0
# while i<100:
#     if i%5==0:
#         print(i)
#     i=i+1

# i=70
# while i<700:
#     if i%65==0:
#         print(i)
#     i=i+1

# for i in range (70,700):
#     if i%65==0:
#         print(i)

# for i in range (50,1000,5):
#     if  i%10==0:
#         print(i)


# i=1
# while i>0:
#     a=int(input("Enter a number = "))
#     for i in range(1,11):
#         print(a*i)
    
#     i=int(input("Do you want to continue ?\npress any number to continue \n Press 0 to exit\nEnter your choice = "))

# i=1
# while i>0:
#     a=int(input("enter the first value="))
#     b=int(input("enter the second value="))
#     q=int(input("calulation method\n 1-additiom\n 2-subtraction\n 3-multiply\n 4-division\nenter the number of method="))
#     if q==1:
#         d=a+b
#         print("sum of these numbers",d)
#     elif q==2:
#         e=a-b
#         print("subtration of these numbers",e)
#     elif q==3:
#         f=a*b
#         print("multiply of these numbres",f)
#     elif q==4:
#         g=a/b
#         print("division of these numbers",g)
#     else:
#         print('Invalid option try again')
#     i=int(input("Do you want to continue ?\npress any number to continue \n Press 0 to exit\nEnter your choice = "))






# i=1
# while i>0:
#     a=int(input("Enter a number = "))
#     for i in range(1,11):
#         print(a*i)
#         if (a*i)%5 == 0:
#             break
    
#     # i=int(input("Do you want to continue ?\npress any number to continue \n Press 0 to exit\nEnter your choice = "))
#     break





# i=1
# while i>0:
#     a=int(input("Enter a number = "))
#     for i in range(1,11):
#         print(a*i)
#         if (a*i)%5 == 0:
#             break
    
#     # i=int(input("Do you want to continue ?\npress any number to continue \n Press 0 to exit\nEnter your choice = "))
#     continue




# while True:
#     a=int(input("enter the first value="))
#     b=int(input("enter the second value="))
    
#     q=int(input("calulation method\n 1-additiom\n 2-subtraction\n 3-multiply\n 4-division\nenter the number of method="))

    # if q==1:
    #     d=a+b
    #     print("sum of these numbers",d)
    # elif q==2:
    #     e=a-b
    #     print("subtration of these numbers",e)
    # elif q==3:
    #     f=a*b
    #     print("multiply of these numbres",f)
    # elif q==4:
    #     g=a/b
    #     print("division of these numbers",g)
    # else:
    #     print('Invalid option try again')

    # i=input("Do you want to continue ?\npress any key to continue \n Press 0 to exit\nEnter your choice = ")
    
    # if i=='0':
    #     break

# a=int(input("enter the intial range="))
# b=int(input("enter the final range"))
# for i in range (a,b):
#     print(i)



# a=input("enter the intial range=")
# b= a.split()
# print(b)
# for i in range(int(b[0]), int(b[1]), -2):
#     print(i)

# # write a python program to display the first 10 natural numbers.
# a=int(input("enter the number="))
# for i in range (1,11):
#     print(i,end=" ")

##write a python program to display the sum of first ten natural numbers.

# a=int(input("enter the intial range="))
# b=int(input("enter the final range="))
# s=0
# for i in range (1,11):
#     s=s+i
# print("sum of range",s)

# ## write a python program to display the sum of n terms of natural numbers.
# a=int(input("enter the number="))
# s=0
# for i in range (1,a):
#     s=s+i
#     print(i,end=" ")

# print("\n total sum=",s)
#write a python program to find out the sum and average of the 10 number enter by the keyboard.

# x=int(input("How many numbers do you want to enter ? = "))
# s=0
# for i in range(x):
#     a= int(input(f"Enter number {i+1} = "))
#     s=s+a

# print("Total Sum = ",s )
# print("Average = ", s/x)

# ##write a python program to find out the cube of number upto an integer.
# a=int(input("enter the number="))
# for i in range (1, a+1):
#     print(f"number is:{i} and cube of {i} is {i**3}")

# #write a python  program to display the multiplication table of the given integer.
# a=int(input("enter the number="))
# for i in range (1,11):
#     print(a*i,end=" ")

# ## write a python program to display the multipilcation table of the given integer in this format 10*1=10.
# a=int(input("enter the number="))
# for i in range (1,11):
#     print(f"{a}*{i} = {a*i}")


##write a python program to display the multiplication table vertically from 1 to n.
# a=int(input("enter the number="))
# for i in range (1,a+1):
#     for j in range (1,11):
#         print(f"{i}*{j} = {j*i}")
#     print("")

# a=int(input("enter the number="))
# for i in range (1,a*2):
#     if i%2==1:
#         print(i)
# ###########################
# *  
# * *  
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# for i in range (1,10):
#     for j in range(1, i+1):
#         print("*",end=" ")
#     print(" ")


# ###########################
# 1  
# 1 2  
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

# for i in range (1,10):
#     for j in range(1, i+1):
#         print(j,end=" ")
#     print(" ")

# ###########################
# 1  
# 2 2  
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9
# for i in range (1,10):
#     for j in range(1, i+1):
#         print(i,end=" ")
#     print(" ")
# #############################
# 1  
# 2 3  
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31 32 33 34 35 36
# 37 38 39 40 41 42 43 44 45
# c=1
# for i in range (1,10):
#     for j in range(1, i+1):
#         print(c,end=" ")
#         c=c+1
#     print(" ")

#  Write a python program to calculate the factorial of a given number.
# a=int(input("enter the number="))
# s=1
# for i in range (1,a+1):
#     s=s*i
#     print(i,end=" ")

# print("factorial of a: =",s)

# Write a python program to display the sum of n terms of even natural numbers.

# a=int(input("enter the number="))
# s=0
# for i in range (1,(a*2)+1):
#     if i%2==0:
#         print(i, end=" ")
#         s=s+i

# print("\ntotal = {s}",format(s))


# # Write a program in python to display the n terms of a harmonic series and their sum.
# 1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms

# a=int(input("Enter the number of terms= "))
# s=0
# for i in range(1,a+1):
#     s=s+(1/i)
# print("The sum of series is", s)


# #  Write a program in python to display the sum of the series [ 9 + 99 + 999 + 9999 ...].
# a=int(input("Enter the range of number="))
# s=0
# p=9
# s=s+p
# for i in range(1,a):
#     p=(p*10)+9
#     s=s+p
# print("The sum of the series = ",s)

# Write a C program that displays the n terms of square natural numbers and their sum.
# 1 4 9 16 ... n Terms

# a=int(input("enter the number="))
# s=1
# for i in range (1,1+a):
#     print(i**2)
#     s=s+(i**2)
# print('sum of numbers=',s)

# # Write a program in python to find the sum of the series 1 +11 + 111 + 1111 + .. n terms
# a=int(input("enter the value="))
# s=1
# print(s)
# m=1
# for i in range (1,a+1):
#     s=((10**i)+s)
#     print(s)
#     m = m+s
# print("sum=",m)

# # Write a python program to check whether a given number is a 'Perfect' number or not.
# a=int(input("enter any number="))
# s=0
# for i in range(1,a):
#     if (a%i==0):
#         s=s+i
#         print(i)
# if (s==a):
#     print("the number is perfect")
# else:
#     print("the number is not perfect")


# # # # Write a python program to print all perfect numbers in a range 
# a=int(input("enter the intial number="))
# b=int(input("enter the final number="))
# for j in range (a, b+1):
#     s=0
#     for i in range(1,j):
#         if (j%i==0):
#             s=s+i

#     if (s==j):
#         print(f"the number {j} is perfect")

# Python Program to print all numbers in a range divisible by a given number.
# a=int(input("enter the intial number="))
# b=int(input("enter the final number="))
# c=int(input("enter the number to be divided by="))
# for i in range (a, b+1):
#     if (i%c==0):
#         print(i)

# #write a python program to check whether a given number is an Armstrong number or not
# x=input("enter the number=")
# s=0
# for i in x:   
#     s= s+ (int(i)**3)
#     print(i,s)

# if int(x)==s:
#     print(s, " is a armstrong number")
# else:
#     print(s, 'is not an armstrong number')

# ##Write a C program to find the Armstrong number for a given range of number
# x=int(input("enter the starting number="))
# y=int(input("enter the final number="))
# for i in range (x,y+1):
#     s=0
#     for j in str(i):
#         s= s+(int(j)**3)

#     if (s==i):
#         print(f"the number {i} is armstrong")

##### Write a python program to determine whether a given number is prime or not.
# a=int(input("enter the number="))
# s=0
# for i in range (2,a+1):
#     if (a%i==0):
#         break
    
# if a==i:
#     print(a," is a prime number ")
# else:
#     print(a, "is not a prime number")

### Write a program in python to find the prime numbers within a range of numbers

# a=int(input("enter the intial range="))
# b=int(input("enter the final range="))
# for i in range(a,b+1):
#     s=0
#     m=0
#     for j in range(2,i+1):
#         m=j
#         if (i%j==0):
#             break

#     if i==m:
#         print(f"the number {i} is prime")

###  Write a program in C to display the first n terms of the Fibonacci series.Fibonacci series 0 1 1 2 3 5 8 13 ....

# x=int(input("enter the range upto="))
# a=0
# b=1
# c=a+b
# print(a,b,c,end=" ")
# for i in range(7):
#     a=b
#     b=c
#     c=a+b
#     print(c,end=" ")

#### write a python program to check the number is palindrome or not

# y=int(input("enter any number="))
# rev = int(str(y)[::-1])

# if y == rev:
#     print('Palindrome')
# else:
#     print("Not Palindrome")

# x=input(("enter any value:"))
# if(x==x[::-1]):
#     print("is a palindrome")
# else:
#     print("Not a palindrome")


### write a python program to find out the number and sum of the all intergers in between 100 and 200 which is divisible by 9.

# x=int(input("enter the intial range="))
# y=int(input("enter the final range="))
# s=0
# for i in range (x,y+1):
#     if i%9==0:
#         print( f"the number {i} are integers divible by 9")
#         s=s+i
# print("total of numbers=",s)

##### write a python program to check the number is strong number or not.
# x=input("enter the any number=")
# m=0
# for j in x:
#     s=1
#     for i in range (1,int(j)+1):
#         s=s*i
#         # print(i,end=" ")

#     m=m+s

# if int(x) == m:
#     print(x, "is a strong number ")
# else:
#     print(x, "is not a strong number ")


##### Write a python program to find Strong Numbers within a range of numbers.
# x=int(input("enter intial range="))
# y=int(input("enter final range="))
# for n in range(x,y+1):
#     m=0
#     for j in str(n):
#         s=1
#         for i in range (1,int(j)+1):
#             s=s*i

#         m=m+s

#     if int(n) == m:
#         print(n, "is a strong number ")

##### Write a python program to find the sum of an A.P. series.
# x=int(input("enter the starting number of the A.P series="))
# y=int(input("enter the number of items of the A.P series="))
# d=int(input("enter the common diffrence of the A.P series="))
# s=0
# i=0
# while i<y:
#     print(x)
#     x=x+d
#     s = s+ x
#     i=i+1

# print("Sum of AP series = ",s)
# ##############
# s=0
# for i in range(y):
#     print(x)
#     x=x+d
#     s = s+ x

# print("Sum of AP series = ",s)

#####   Write a python program to find the sum of the G.P. series
# x=int(input("enter the starting number of the G.P series="))
# y=int(input("enter the number of items of the G.P series="))
# d=int(input("enter the common ratio of the G.P series="))
# s=0
# for i in range(y):
#     print(x)
#     x=x*d
#     s=s+x

# print("Sum of GP series = ",s)

#### Write a python program to print a string in reverse order.
# y=(input("enter any string="))
# rev = (str(y)[::-1])
# print('reverse of string is =',rev)


###### write a python program to find the length of a string without using the library function.

# a=input("Enter string:")
# s=0
# for i in a:
#     s=s+1
# print("Length of the string is:",s)


###### write a program to check the Armstrong number of n digits.

# n=int(input("enter the number of digit you want to enter="))
# x=input("enter the number=")
# s=0
# for i in x:
#     s= s+ (int(i)**n)
#     print(i,s)

# if int(x)==s:
#     print(s, " is a armstrong number")
# else:
#     print(s, 'is not an armstrong number')
