# Q1 /*calculate area of circle*/

def area():
	r=int(input("enter the value of radius"))
	a=3.14*r**2
	print ("area of circle:",a)
area()	

#Q2


def perfect(n):
  sum=0
  for i in range(1,n):
    if n%i==0:
      sum=sum + i
  if sum==n:
    return True
  else:
    return False
for i in range(1,1001):
  if perfect(i):
    print( i)

	
#Q3


def rec(i,n):
	x=0
	if i>10:
		return 0
	else:
		x=n*i
		
		print("%d * %d = %d"%(n,i,x))
		rec(i=i+1,n=n)
		
rec(n=12,i=1)


#Q4


def power():
	x=int(input("enter the first number :"))
	y=int(input("enter the second number :"))
	z=x**y
	print(z)
power()


#Q5


def fact(n):
	
	if n==0 or n==1:
					return 1
	else:
	
      		return(n*fact(n-1))
			
n=int(input("enter a number"))
print("the factorial of %d:"%n,fact(n%i))

c= fact(n)
d={n:c}
print(d)


