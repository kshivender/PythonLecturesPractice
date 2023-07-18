# a=input("enter your age=")
# if(int(a)>17):
#     print("eligible to vote")
# else:
#     print("not eligible to vote") 
#     print('eligible to vote' if int(a)>17 else 'not eligible to vote')
# a=int(input("enter your age="))
# if a>0 and a<=12:
#     print("child")
# elif a>13 and a<=19:
#     print("teenager")
# elif a>=20 and a<=60:
#     print('adult')
# elif a>=60:
#     print("senior citizen")
# else:
#     print("Invalid input")

# a = int(input("enter the number="))
# if a%2==0:
#     print(a,"is divisible by 2")
#     if a%3==0:
#         print(a,"is divisible by number by 3")
#     else:
#         print(a,"a is not divisible by 3")
# else:
#     print(a,"is not divisible by 2")

# a = int(input("enter the number="))
# b = int(input("enter the number="))
# if a==b:
#     print(a,"is equal to ",b)
# else:
#     print(a,"is not equal to ",b)
    

# a = int(input("enter the number="))
# if a%2==2:
#     print(a,"is even number")
# else:
#     print(a,"is odd number")

# a = int(input("enter the number="))
# if a<0:
#     print(a,"is negative number")
# else:
#     print(a,"is positive number)")

# a = int(input("enter the year"))
# if a%4==0:
#     print(a,"is leap year")
# else:
#     print(a,"is not leap year")

# a = int(input("enter the age="))
# if a>=18:
#     print(a,"is elibible for vote")
# else:
#     print(a,"is not eligible for vote")

# m = int(input("enter the value="))
# if m<0:
#     print("n=-1")
# elif m==0:
#     print("n=0")
# elif m>0:
#     print("n=1")

# a = int(input("enter the value="))
# b = int(input("enter the value="))
# c = int(input("enter the value="))
# if a>b and a>c:
#     print(a,"is greater")
# elif b>a and b>c:
#     print(b,"is greater")
# elif c>a and c>b:
#     print(c,"is greater")
# elif a==b and a==c:
#     print("All numbers are equal")

# a = int(input("enter the value="))
# b = int(input("enter the value="))
# if a>=0 and b>=0:
#     print("numbers are in first quadrent")
# elif a>0 and b>0:
#     print("numbers are in second quadrent")
# elif a<0 and b<0:
#     print("numbers are in third quadrent")
# elif a>0 and b<0:
#     print("numbers are in fourth quadrent")

# a=int(input("marks in maths="))
# b=int(input("marks in physics="))
# c=int(input("marks in chemistry="))
# d=int(input("total numbers in all three="))
# e=int(input("total numbers in Maths and physics="))
# if a>=65 and b>=55 and c>=50 and d>=190 and e>=140:
#     print("this candidate is eligible")
# else:
#     print("candidate is not eligible")


# a=int(input("enter the roll number of the student="))
# b=input("enter the name of the student")
# c=int(input("enter marks of the physics="))
# d=int(input("enter the marks of the chemistry="))
# e=int(input("enter the marks of the computer science="))
# total=c+d+e
# percentage= total/3
# print("total marks=",total)
# print("percentage=",percentage,"%")
# if(percentage>=60):
#     print("division=First")
# elif (percentage>=50):
#     print("division=second")
# elif(percentage>=40):
#     print("division=third")
# else:
#     print("division=fail")

# a=int(input("enter temperature"))
# if(a<0):
#     print("freezing weather")
# elif (a>=0 and a<10):
#     print("very cold weather")
# elif (a>=10 and a<20):
#     print("cold weather")
# elif (a>=20 and a<30):
#     print("normal weather")
# elif (a>=30 and a<40):
#     print("hot weather")
# elif (a>=40):
#     print("very hot weather")

# a=int(input("enter the value of first angle"))
# b=int(input("enter the value of second angle"))
# c=int(input("enter the value of third angle"))
# total=a+b+c
# if(total==180):
#     print("triangle is valid")
# elif(a<90 and b<90 and c<90 and total==180):
#     print("acute triangle")
# elif(a<=90 and b<90 and c>90 and total==180):
#     print("right angled triangle")
# else:
#     print("triangle is not valid")

# a=int(input("enter the value of first side="))
# b=int(input("enter the value of second side="))
# c=int(input("enter the value of third layer="))
# if(a==b and b==c):
#     print("equilatral triangle")
# elif(a==b or a==c or b==c):
#     print("isoceles triangle")
# else:
#     print("scalene triangle")

# a=(input("enter the character="))
# if(a.isalpha()):
#     print("character is alphabet")
# elif(a.isnumeric()):
#     print("character is digit")
# elif(a.isascii()):
#     print("character is special character")

# a=(input("enter the alphabet="))
# b='aeiou'
# if(a in b):
#     print("is vowel")
# else:
#     print("is consonant")

# a=input("enter the digit=")
# if(a=='1'):
#     print('one')
# elif(a=='2'):
#     print('two')
# elif(a=='3'):
#     print('three')
# elif(a=='4'):
#     print('four')

# a=int(input("enter the month number="))
# if(a==1):
#     print('January')
# elif(a==2):
#     print('Feburary')
# elif(a==3):
#     print('march')
# elif(a==4):
#     print('april')
# elif(a==5):
#     print('may')
# elif(a==6):
#     print('june')
# elif((a==7)):
#     print('july')
# elif(a==8):
#     print('august')
# elif(a==9):
#     print('september')
# elif(a==10):
#     print('october')
# elif(a==11):
#     print('november')
# elif(a==12):
#     print('december')
# else:
#     print('invalid option')
    

# a=int(input("customer ID="))
# b=(input("customer name="))
# c=int(input("unit consumed="))
# amount=0
# if(c>=0 and c<=199):
#     amount = c*1.20
#     print('amount charged',amount)
# elif c>=200 and c<400:
#     amount = c*1.50
#     print('amount charged',amount)
# elif c>=400 and c<600:
#     amount = c*1.80
#     print('amount charged',amount)
# elif c>=600:
#     amount = c*2.00
#     print('amount charged',amount)
# total_bill=0
# if amount<=100:
#     total_bill = 100
# elif amount>=400:
#     total_bill = total_bill + amount*0.15
#     print("surcharge amount",total_bill)
#     overall_bill = total_bill + amount
#     print("net amount paid by the customer",overall_bill)


# a=int(input("enter the first value="))
# b=int(input("enter the second value="))
# # print("calulation method\n 1-additiom\n 2-subtraction\n 3-multiply\n 4-division")
# # q=int(input("enter the number of method="))

# q=int(input("calulation method\n 1-additiom\n 2-subtraction\n 3-multiply\n 4-division\nenter the number of method="))
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


# a=int(input("select number to find out the area of the shape\n 1.sphere\n 2.rectangle\n 3.square\n 4.cube\n  "))
# if a==1:
#     r=int(input("radius of the circle="))
#     area=3.14*r*r
#     print("area of the circle",area)
# elif a==2:
#     l=int(input("length of the rectangle="))
#     b=int(input("breath of the rectangle="))
#     area_of_rectangle=l*b
#     print("area if the rectangle",area_of_rectangle)
# elif a==3:
#     s=int(input("side of square="))
#     area_of_square=4*s
#     print("area of the square",area_of_square)
# elif a==4:
#     w=int(input("side of the cube="))
#     area_of_cube=6*w*w
#     print("area of the cube",area_of_cube)
# else:
#     print("invaid input")


# a=int(input("enter the selling price="))
# b=int(input("enter the buying price="))
# profit=a-b
# loss=b-a
# if profit>0:
#     print("total profit=",profit)
# else:
#     print("total loss=",loss)

# a=input("enter the grade=").upper()
# if a=='E':
#     print("excellent")
# elif a=='V':
#     print('Very good')


























