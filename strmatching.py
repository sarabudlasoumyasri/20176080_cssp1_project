def s(s):
	for i in s:
		if (ord(i)<123 and ord(i)>96)or (ord(i)<58 and ord(i)>47) or i=='_':
			s=s
		elif(i==' '):
			s=s		
		else:
			s=s.replace(i,"")

	return s
def compare(s1,s2):
	lcs=0
	for i in range (len(s1)):
		x=i
		y=x
		for j in range  (len(s2)): 
			if(x<len(s1)):
				if s1[x]==s2[j]:
					x+=1
					if(x-i)>lcs:
						lcs=x-i
						k=s1[i:x].strip()
						print(k)
				else:
					x=y
	return k

	
import glob
i='C:/Users/hp/Desktop/cssp/project/str/*.txt'
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
			c=f1.read().lower()
			d=f2.read().lower()
			s1,s2=s(c),s(d)
			print(s1,s2)
			a=len(s1)+len(s2)
			k=compare(s1,s2)
			e=len(k)
			z=round((((2*e)/a)*100),2)
			r[i].append(z)
print(r)

			