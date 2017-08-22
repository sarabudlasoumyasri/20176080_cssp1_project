f1=open('file1.txt','r')
f2=open('file2.txt','r')
a,b=f1.read(),f2.read()
def s(s):
	s=s.lower()
	c='abcdefghijklmnopqrstuvwxyz_0123456789'
	for i in s:
		if i not in c:
			s=s.replace(i," ")
	return s.split(" ")
s1,s2=s(a),s(b)
def freq(n):
	d={}
	for i in n:
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	return d
d1,d2=freq(s1),freq(s2)
sum=0
for i in d1:
	if i in d2:
		e=d1[i]*d2[i]
		sum+=e
def mathy(d):
	x=0
	for i in d:
		x+=((d[i])**2)
	return x
ah=(mathy(d1)*mathy(d2))**(1/2)
c=(sum/ah)*100
print('The % is matching',c)
	





	