f= open('MCM.csv','rb')
csv.reader(f)
head=csv.reader(f).next()
col={}

for h in head:
	col[h]=[]

for row in reader:
	for h,v in zip(head,row):
		 col[h].append(v)
