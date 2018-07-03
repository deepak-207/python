#1.
import re
emails = "deepak207@facebook.com page45@google.com ffej42@amazon.com"
p=re.compile(r"(.*)@(.*).(...) (.*)@(.*).(...) (.*)@(.*).(...)")
result=p.match(emails)
a=(result.group(1))
b=(result.group(2))
c=(result.group(3))
d=(result.group(4))
e=(result.group(5))
f=(result.group(6))
g=(result.group(7))
h=(result.group(8))
i=(result.group(9))
A=[a,b,c]
B=[d,e,f]
C=[g,h,i]
l=[tuple(A),tuple(B),tuple(C)]
print(l)




#2.
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter,To make the bitter butter better."
p=re.compile(r"B",re.I)
result=p.finditer(text)
for r in result:
	print(r)
	
	
 
#3.
 import re
sentence = "A, very very; irregular_sentence"
m=re.sub(r"[^\w]"," ",sentence)
p=re.sub("_"," ",m)
print(p)