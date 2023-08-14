def addition(m,n):
    return m+n

def subtraction(m,n):
    return m-n

def multiplication(m,n):
    return m*n

def division(m,n):
    return m/n

def billamount(unit):
    amount=0
    if(unit>=0 and unit<=199):
        amount = unit*1.20
    elif unit>=200 and unit<400:
        amount = unit*1.50
    elif unit>=400 and unit<600:
        amount = unit*1.80
    elif unit>=600:
        amount = unit*2.00

    total_bill=0
    # print("Bill amount = ", amount)
    if amount<=100:
        total_bill = 100
        return total_bill
    elif amount>=400:
        total_bill = amount + amount*0.15
        return total_bill
    else:
        total_bill = amount
        return total_bill