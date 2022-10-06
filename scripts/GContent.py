from Bio import SeqIO
from Bio.SeqUtils import GC
import pandas as pd

fin = "../raw/Mammalia.fa"

IDs=[]
GCs=[]
for entry in SeqIO.parse(fin, 'fasta'):
    id = entry.id
    seq = entry.seq
    gc = round(GC(seq), 1)

    IDs.append(id)
    GCs.append(gc)

df = pd.DataFrame()
df['ID'] = IDs
df['GC'] = GCs

df.to_csv('../reSLUTS/GContent.csv', sep=",")