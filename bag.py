def s(s):
	for i in s:
		if (ord(i)<123 and ord(i)>96)or (ord(i)<58 and ord(i)>47) or i=='_':
			s=s
		else:
			s=s.replace(i," ")
	return s			
def freq(n):
	d={}
	for i in n:
		if i in d:
			d[i]+=1
		else:
			d[i]=1
	return d

def mathy(d):
	x=0
	for i in d:
		x+=((d[i])**2)
	return x
import glob
i='C:/Users/hp/Desktop/project/bag/*.txt'
l=glob.glob(i)
le=len(l)
r=[]
for i in range(le):
	r.append([])
	for j in range(le):
		if i==j:
			r[i].append(0)
		else:
			f1=open(l[i])
			f2=open(l[j])
			a,b=f1.read().lower(),f2.read().lower()
			s1,s2=s(a).split(),s(b).split()
			d1,d2=freq(s1),freq(s2)
			sum=0
			for k in d1:
				if k in d2:
					e=d1[k]*d2[k]
					sum+=e
			ah=(mathy(d1)*mathy(d2))**(1/2)
			c=round((sum/ah)*100,2)
			r[i].append(c)
print(r)





	