import csv
import pandas as pd
ID_t=[]
Per_GC=[]
list_ID=[]
list_GC=[]
s=0
with open('/home/ekaterina/Documents/Haha/GCtransposon.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ID_t.append(row['ID'])
        Per_GC.append(row['GC_transposon'])
for i in ID_t:
    if ID_t.count(i)!=1:
        c = ID_t.count(i)
        index_1 = ID_t.index(i)
        index_2=index_1+c
        dlya_srednee = Per_GC[index_1:index_2]
        list_ID.append(i)
        for k in dlya_srednee:
            s=s+float(k)
        srednee = s/c
        del ID_t[index_1:index_2]
        del Per_GC[index_1:index_2]
        list_GC.append(round(srednee,1))
        s=0
    else:
        list_ID.append(i)
        list_GC.append(Per_GC[ID_t.index(i)])


df = pd.DataFrame()
df['Transposon'] = list_ID
df['GC%'] = list_GC

df.to_csv('/home/ekaterina/Documents/GC_Transposon_srednee.csv', sep=",")