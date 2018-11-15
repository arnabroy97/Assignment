import pandas as pd
import sys,os
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt


df = pd.read_csv('pcadata/Assignment-gene_data.csv',sep=",",low_memory=False)
meta_df = pd.read_csv('pcadata/Assignment-Meta_data_sheet.csv',sep=",")
meta_df = meta_df.drop("Unit",axis=1)
meta_df = meta_df.drop("sIdx",axis=1)

#sys.exit()
data = df.drop("Index", axis=1)
data = data.drop("Symbol", axis=1)
data = data.drop([12076], axis=0)


scaled_data = preprocessing.scale(data.T) 
#print scaled_data
pca = PCA() # create a PCA object
pca.fit(scaled_data) # do the math
pca_data = pca.transform(scaled_data) # get PCA coordinates for scaled_data


per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
labels = ['PC' + str(x) for x in range(1, len(per_var)+1)]
x=range(1,len(per_var)+1)

plt.bar(x, per_var, tick_label=labels , align='center', alpha=0.5)
plt.ylabel('Percentage of Explained Variance')
plt.xlabel('Principal Component')
plt.title('Scree Plot')
plt.show()

#print pca_data


arnab = ['S' + str(i) for i in range(1,31)]
arnab1 = [str(i) for i in range(1,len(data)+1)]
#print ko
pca_df = pd.DataFrame(pca_data, index=arnab[0:], columns=labels)

plt.scatter(pca_df.PC1, pca_df.PC2)
plt.title('My PCA Graph')
plt.xlabel('PC1 - {0}%'.format(per_var[0]))
plt.ylabel('PC2 - {0}%'.format(per_var[1]))
 
for sample in pca_df.index:
    plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))
 
plt.show()

fig, ax = plt.subplots()
plt.scatter(x,meta_df.values)
plt.xlabel("Features")
plt.ylabel("Time (Hours)")

for i, txt in enumerate(arnab):
    ax.annotate(txt, (x[i], meta_df.values[i]+0.5))
plt.show()
