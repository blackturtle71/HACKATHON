from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt

fin = "../raw/Mammalia.fa"

ids = []
As = []
Ts = []
Gs = []
Cs = []

Ap = []
Tp = []
Gp = []
Cp = []


for entry in SeqIO.parse(fin, 'fasta'):
    id = entry.id
    seq = entry.seq

    A = seq.count('A')
    T = seq.count('T')
    G = seq.count('G')
    C = seq.count('C')

    perA = round((A / (T+G+C)) * 100, 1)
    perT = round((T / (A+G+C)) * 100, 1)
    perG = round((G / (T+A+C)) * 100, 1)
    perC = round((C / (T+G+A)) * 100, 1)

    ids.append(id)
    As.append(A)
    Ts.append(T)
    Gs.append(G)
    Cs.append(C)

    Ap.append(perA)
    Tp.append(perT)
    Gp.append(perG)
    Cp.append(perC)

df = pd.DataFrame()
df['ID'] = ids

df['A'] = As
df['T'] = Ts
df['G'] = Gs
df['C'] = Cs

df['A%'] = Ap
df['T%'] = Tp
df['G%'] = Gp
df['C%'] = Cp


df.to_csv('../reSLUTS/ATGContent.csv', sep=",")


########################################


df['A%'].plot(kind='hist', bins=20, color="green")
plt.xlabel('A%')
plt.savefig('../reSLUTS/A_distro.PDF', format='PDF')
plt.clf()

df['C%'].plot(kind='hist', bins=20, color="blue")
plt.xlabel('C%')
plt.savefig('../reSLUTS/C_distro.PDF', format='PDF')
plt.clf()

df['G%'].plot(kind='hist', bins=20, color="black")
plt.xlabel('G%')
plt.savefig('../reSLUTS/G_distro.PDF', format='PDF')
plt.clf()

df['T%'].plot(kind='hist', bins=20, color="red")
plt.xlabel('T%')
plt.savefig('../reSLUTS/T_distro.PDF', format='PDF')
plt.clf()

##########################

a_extremities = df.query('`A%` >= 52 or `A%` <= 46')
c_extremities = df.query('`C%` >= 40 or `C%` <= 33')
g_extremities = df.query('`G%` >= 16 or `G%` <= 14')
t_extremities = df.query('`T%` >= 43 or `T%` <= 33')

