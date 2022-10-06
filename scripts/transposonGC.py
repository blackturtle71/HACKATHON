from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd

fasta = "../raw/Mammalia.fa"
hasLTR = "../reSLUTS/repeatmasker_res/transposon_stuff/hasLTR.species"



df = pd.read_csv(hasLTR, header=None)
df.rename(columns={0:'ID', 1:'begin', 2:'end'}, inplace=True)
#df.set_index('ID', inplace=True)


IDs=[]
GCs=[]

for entry in SeqIO.parse(fasta, 'fasta'):
    eid = entry.id
    seq = entry.seq
    for i in range(len(df)):
        LTRid = df.loc[i, 'ID']
        begin = df.loc[i, 'begin']
        end = df.loc[i, 'end']
        if eid == LTRid.strip():
            transposon = seq[begin-1:end]
            gc = round(GC(transposon), 1)
            IDs.append(eid)
            GCs.append(gc)

gc_df = pd.DataFrame()
gc_df['ID'] = IDs
gc_df['GC_transposon'] = GCs

gc_df.to_csv('../reSLUTS/GCtransposon.csv')






