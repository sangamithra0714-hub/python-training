import csv
f=open("students.csv","r")
data=csv.reader(f)
s1=open("students1.csv","w")
w=csv.writer(s1)
for i in data:
    w.writerow(i)

s2=open("students2.csv","w")
f.seek(0)
w=csv.writer(s2)
for i in data:
    w.writerow(i)
s3=open("students3.csv","w")
f.seek(0)
w=csv.writer(s3)
for i in data:
    w.writerow(i)
f.close()
