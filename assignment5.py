#Q1 
n=int(input("enter year"))
if (n%4==0) :
          print ("leap year")
else :
		  print("not a leap year")
		  
		  
		  
		  
		  
		  
		  

#Q2


x=int(input("enter value of length :"))

y=int(input("enter value of breadth :"))

if	(x==y):
	  print("di8mension are of square")
	  
else :
	 print("dimensions are of rectangle")



#Q3


#take ther input ager of 3 people and determine the youngest and oldest in them
a=int(input("enter your age"))
b=int(input("enter your age"))
c=int(input("enter your age"))
if(a>b):
 if(a>c):
  print("a is older")
 else:
  print("c is older")
else:
 if(b>c):
  print("b is older")
 else:
  print("c is older")
   


#Q4

a=int(input("Enter the points:"))
f=1
if a<200:
    if 1<a<50:
        f=0
        print("No Prize")
    elif 50<a<150:
        prize="Wooden Box"
    elif 150<a<180:
        prize="Book"
    elif 180<a<200:
        prize="Chocolate"
    if f!=0:
       print("Congratulations! You won a {}".format("prize"))
 	
	
	  #Q5
n=int(input("enter the cost:"))
p=n*100
if p>1000:
   disc=p*.1
   r=p-disc
   print('total cost= ',r)
