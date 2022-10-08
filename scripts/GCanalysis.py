import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

GC_all = pd.read_csv('../reSLUTS/NuclCont/GContent.csv')
GC_trans = pd.read_csv('../reSLUTS/NuclCont/GC_Transposon_mean.csv')

IDs = []
GCs = []
TransGCs = []
for i in range(len(GC_all)):
    ID = GC_all.loc[i, 'ID']
    for j in range(len(GC_trans)):
        TransID = GC_trans.loc[j, 'ID']
        if TransID == ID:
            TransGC = GC_trans.loc[j, 'GC%']
            GC = GC_all.loc[i, 'GC']
            IDs.append(TransID)
            GCs.append(GC)
            TransGCs.append(TransGC)


GCanalysis = pd.DataFrame()
GCanalysis['ID'] = IDs
GCanalysis['GC'] = GCs
GCanalysis['Transposon GC'] = TransGCs
#GCanalysis.to_csv('../reSLUTS/NuclCont/GCanalysis.csv', sep=',')
#GCanalysis.set_index('ID', inplace=True)

GCanalysis.plot.barh(x='ID', color=['red', 'pink'], width = 0.8)
#plt.show()
#plt.savefig('../reSLUTS/PDF/GCanalysis.pdf', format='PDF')

a = GCanalysis['GC'].to_numpy()
b = GCanalysis['Transposon GC'].to_numpy()

print(stats.ttest_ind(a=a, b=b, equal_var=False))
#Ttest_indResult(statistic=-5.156627569601541, pvalue=2.2937580795757305e-06)

