#Time complexity of KMP algorithm is O(n) in worst case
def kmp(txt,pat):
	l1=len(txt)
	l2=len(pat)
	lps=[0]*l2
	j=0
	lps1(pat,lps,l2)
	i=0
	while i<l1:
		if pat[j]==txt[i]:
			i+=1
			j+=1
		if j==l2 :
			print ("INDEX FOUND AT :"+str(i-j))
			j=lps[j-1]
		elif i < l1 and pat[j] != txt[i]:
			if j!=0:
				j=lps[j-1]
			else:
				i+=1

def lps1(txt,lps,m):
	len1=0
	lps[0]=0
	i=1
	while i<m:
		if pat[i]==pat[len1]:
			len1+=1
			lps[i]=len1
			i+=1
		else:
			if len1!=0:
				len1=lps[len1-1]
			else:
				lps[i]=0
				i+=1




txt=input("TEXT: ")
pat=input("Pattern :")

kmp(txt,pat)
