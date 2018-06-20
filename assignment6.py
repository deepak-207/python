#Q1 

#  using for loop

for  i in range (0,10):
	 n=int(input("enter integer value"))
	 print(n)
	
	
#Q2



i=1
while i!=-1:
	print("hello")
	i=i+1
	
	
	
#Q3


l=[]
s=[]
a=int(input("enter the range of list"))
for x in range(a):
	l.append(int(input("enter a number:")))
for x in l:
	s.append(x**2)
print(l)
print(s)	


#Q4

l = []
for x in range(0, 3):
    x = int(input("enter numbers"))
    l.append(x)
for x in range(3, 6):
    x = input("enter strings")
    l.append(x)
for x in range(6, 9):
    x = float(input("enter floats"))
    l.append(x)
print(l)
l1 = []
l2 = []
l3 = []
for x in l:
    if type(x) == int:
        l1.append(x)
    elif type(x) == str:
        l2.append(x)
    elif type(x) == float:
        l3.append(x)
print(l1)
print(l2)
print(l3)


#Q5

e=[]
o=[]


for i in range  (1,101) :
	if i%2==0:
		e.append(i)
	else:
		o.append(i)
		i=i+1
print("odd list:")
print(o)
print("even list:")
print(e)		


#Q6

n=int(input("enter the numbers of row"))
for i in range (0,n):
	for j in range (0,i+1):
		print("*",end="")
	print()
	
	
#Q7


d = {}
for x in range(5):
    keys = int(input("enter the keys"))
    values = input("enter value items")
    d[keys] = values
print(d)


#Q8


flag = 0
for x in range(5):
    x = int(input("enter the numbers"))
    l.append(x)
print(l)
y = int(input("select any number you want to search"))
for x in l:
    if x == y:
        l.remove(x)
        flag = 1
print(l)
if flag == 0:
    print("the number you entered is not in the list")
