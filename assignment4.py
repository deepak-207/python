#Q11

t=(2,4,6,8,1)
print(t)

print(len(t))


#Q2
t=(2,4,6,8,1)
print(max(t))
print(min(t))



#program to find the product of all element of tuple
def  pro(t):
 r=1
 for i in t:
  r=r*i
 return r
tu=(1,2,3)
p=pro(tu)
print(p)

 #sets
#Q1


a=set([4,5,6,7,8])
b=set([1,2,3,4,5])

print(a-b)

  #INTERSECTION
a=set([4,5,6,7,8])
b=set([1,2,3,4,5])
print(a & b)

#create a dictionary to store name and marks of 10 students
d={}
for n in range (10):
    name=input("enter your name;")
    marks=int(input("enter your marks:"))
    d[name]=marks
print(d)


#sorting of dictionary
d={'a':20,'b':30,'c':40}
print(d)
values=list(d.values())
print(values)
values.sort()
print(values)

 #count the no. of occurence of each letter in word "MISSISSIPPI"
l = list("MISSISSIPPI")
print(l)
d={}
d['M']=l.count('M')
d['I']=l.count('I')
d['S']=l.count('S')
d['S']=l.count('S')
d['I']=l.count('I')
d['S']=l.count('S')
d['S']=l.count('I')
d['I']=l.count('I')
d['P']=l.count('P')
d['P']=l.count('P')
d['I']=l.count('I')
print(d)











      
