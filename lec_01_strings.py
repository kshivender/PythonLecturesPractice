# print('Hello World')

# print('Hii Everyone')

# a = 'Ram Singh'  # defined a variable
# print(a)
# print(len(a))

# print(a[5])
# print(a[-4])

# b = 'my name is Joker'

#### m y   n a m e   i s     j  o  k  e  r
#### 0 1 2 3 4 5 6 7 8 9 10  11 12 13 14 15

# print(b)
# print(len(b))
# print(b[-5])
# print(b[7])
# print(b[8])
# print(b[2])
# print(b[-4]) 
# c = 'tom'
# d = 'jerry'
# print(c+d)
# print(c+' '+d)
# e = 'rahul'
# print(e*5)
# f = 'Self-conquest is the greatest of victories'
# print(f[9])
# print(f[-9])
# print(f[-10])
# print(f[3:13])
# print(f[5:13]+f[20:30])
# b = 'missiccippi'
# c = 'independent'
# print(b[0:5]+c[7:11]+b[8:11]+c[0:4])
# print(b[0:5]+c[7:]+b[8:]+c[0:4])
# print(b[0:5]+c[7:]+b[-3:]+c[0:4])



# ##  String Methods

# print(dir(''))

# print('-'.join('ram'))

# c = 'independent'
# print(c.index('e'))
# print(c.find('z'))
# print('-'.join('ram'))
# a = "      good morning to all of you       "
# b=a.lstrip()
# print(b.lstrip('good'))

# b=a.lstrip().lstrip('good')
# print(b)

s = 'cOntrOl yOur miNd and eMotIons'
# print(s.count('o'))
# print(s.rindex('n'))
# print(s.rindex('o'))
# print(s.index('d',11,19))
# print(s.find('r',12,19))
# print(s.find('d',18,23))
# print(s.zfill(50))

# t=' tit for tat' 
# print(t.zfill(30,))

# print(s.upper())
# print(s.swapcase())
# print(s.capitalize())
# print(s.title())
# print(s.center(50))
# a = "good morning to all if you"
# b=a.lstrip()
# print(b.lstrip('good'))
# # print(b.removeprefix('good'))
# print(a.split())
# print(len(a.split()))
# print(a.split('o'))
# b = "improve sewage treatment.\n promote sustainable fishing practices.\n control industries pollution.\n support research and innovation\n."
# print(b.splitlines())
# c = "improve sewage treatment.promote sustainable fishing practices.control industries pollution.support research and innovation\n."
# print(c.splitlines())
# a='HELLO'
# b='world'
# c='12345'
# d='23.456'
# e='abc456'
# f='abc12.5f'
# print(a.isalpha())
# print(a.isupper())
# print(a.islower())
# print(a.isalnum())
# print(e.isalnum())
# print(f.isalnum())
# print(f.isascii())
# print(c.isdigit())
# print(d.isnumeric())
# print(d.isdecimal())


# Format Method
a,b,c = 12,23,34
# print("value of a = ",a,"\n value of b = ", b, "\n value of c = ",c)
# print("value of a = {0}\n value of b = {1}\nvalue of c = {2}".format(a,b,c)) 

# print("value of a = {p}\n value of b = {q}\nvalue of c = {r}".format(p=a,q=b,r=c))

# print("value of a = {}\n value of b = {}\nvalue of c = {}".format(a,b,c)) 

# print(f"value of a = {a}\nvalue of b = {b}\nvalue of c = {c}") 