d=256
def search(txt,pat,q):
    M=len(pat)
    N=len(txt)
    i =0
    j =0
    p =0
    t =0 #hash value of pattren
    h =1 #hash value for txt
    for i in range(M-1):
            h=(h*d)%q
    for i  in range(M):
        p=(d*p+ord(pat[i]))%q
        t=(d*t+ord(txt[i]))%q
    for i in range(N-M+1):
        if p==t:
            for j in range(M):
                if txt[i+j]!=pat[j]:
                    break
            j+=1
            if j==M:
                print("found at index"+str(i))
        if i<N-M:
            t=(d*(t-ord(txt[i])*h)+ord(txt[i+M]))%q
            if t< 0:
                t=t+d
txt=[]
pat=[]
txt=input("Input string:")
pat=input("Pattern string:")
search(txt,pat,101)
