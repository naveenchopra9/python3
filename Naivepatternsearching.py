def search(txt,pat):
	M=len(txt)
	N=len(pat)
	for i in range(M-N+1):
		for j in range(N):
			if txt[j+i]!=pat[j]:
				break;
		if j==N-1:
			print ("position pattren" +str(i))

txt=str(input("input txt string: "))
pat=str(input("input pat string: "))
search(txt,pat)
