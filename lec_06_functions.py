# def sumof2nums (m=0, n=0):
#     return m+n
# # a=int(input("enter num1 = "))
# # b=int(input("enter num2 = "))
# # c=sumof2nums(a,b)
# # print(c)

# for i in range(1000):
#     a =int(input("enter the first number = "))
#     b =int(input("enter the second number = "))
#     c=sumof2nums(a,b)
#     print(c)


# def sumof2nums():
#     a=int(input("enter the first number = "))
#     b=int(input("enter the second number = "))
#     c=a+b
#     print(c)


# for i in range(1000):
#     sumof2nums()

######### LAMBDA FUNCTION ##########
# x=lambda i:i*i
# print(x(5))

# x=lambda i,j :i**j
# print(x(5,4))

# x = lambda i,j=3: i**j
# print(x(2))


# def billamount(unit):
#     amount=0
#     if(unit>=0 and unit<=199):
#         amount = unit*1.20
#     elif unit>=200 and unit<400:
#         amount = unit*1.50
#     elif unit>=400 and unit<600:
#         amount = unit*1.80
#     elif unit>=600:
#         amount = unit*2.00

#     total_bill=0
#     print("Bill amount = ", amount)
#     if amount<=100:
#         total_bill = 100
#         return total_bill
#     elif amount>=400:
#         total_bill = amount + amount*0.15
#         return total_bill

# for i in range (10):
#     a=input("customer ID=")
#     b=input("customer name=")
#     c=int(input("unit consumed="))
#     overall_bill = billamount(c)
#     print("Total Bill = ", overall_bill)


