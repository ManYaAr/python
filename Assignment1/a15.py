import csv 
with open("c1.csv",'w') as f:
    r=csv.writer(f)
    r.writerow(["EmpID","Employee","Salary"])
with open("c1.csv",'r') as f:
    p=csv.reader(f)
    for l in f:
        print(l)