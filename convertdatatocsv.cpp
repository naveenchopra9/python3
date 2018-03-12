import csv
l=[]
write=open('/Users/naveen/Documents/kinectProject/notrealwaving.csv','w',newline='')
with open('/Users/naveen/Documents/kinectProject/notwaving.csv', newline='') as f:
	reader = csv.reader(f)
	for row in reader:
		d=row[0].split(' ')
		d = [j for j in d if len(j) > 0]
		d=d+[1]
		if len(d)==43:
			# print(d)
			l.append(d)
			# print(len(d))
print(l)

# for p in l :
# 	print(len(p))
with write:
	writer = csv.writer(write)
	writer.writerows(l)
write.close()
