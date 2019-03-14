class lcs(object):
	def s(self,s):                                         #removing of special characters
		for i in s:
			if (ord(i)<123 and ord(i)>96)or (ord(i)<58 and ord(i)>47) or i=='_':
				s=s
			elif(i==' '):
				s=s		
			else:
				s=s.replace(i,"")
		return s
	def compare(self,s1,s2):
		lcs=0
		for i in range (len(s1)):             #comparision of character by character and find largest common string length
			x=i
			y=x
			for j in range  (len(s2)): 
				if(x<len(s1)):
					if s1[x]==s2[j]:
						x+=1
						if(x-i)>lcs:
							lcs=x-i
							k=s1[i:x].strip() 
					else:
						x=y
		return k	
import glob,os 
os.chdir('match')
i='*.txt'
l=glob.glob(i)
le=len(l)                                     #access of some text files
obj=lcs()
r=[]
for i in range(le):
	r.append([])	
	for j in range(le):
		if i==j:                      #appending the 0 is comparision same files
			r[i].append(0)                        
		else:                                    
			f1=open(l[i])                     #opening the files
			f2=open(l[j])
			try:                                       
				c=f1.read().lower()                           #reading,converting to lower case
				d=f2.read().lower()
				if len(c)*len(d)==0:
					raise ZeroDivisionError      #raise zerodivison error
				else:
					s1,s2=obj.s(c),obj.s(d)                   # saving the files and creating objects to file to access class         
					a=len(s1)+len(s2)                        #finding files length
					k=obj.compare(s1,s2)       # calling function for compare characters
					e=len(k)                                               # length of lcs
					z=round((((2*e)/a)*100),2)                     # percentage of matching (z)
					r[i].append(z) 								#append the percentages in to list
			except ZeroDivisionError:
				print('One of the lists is empty')         #print list is em                      
print(r)                                                   #print r i.e; matrix 

			