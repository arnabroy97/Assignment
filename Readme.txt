#####################   Readme     #################
The outputs are obtained after performing PCA by the PCA package created from scratch in Python.
Fig1 gives a bar plot of percentage of variance obtained for PC1 to PC30(30 principal components).
Fig2 gives the main PC1 vs PC2 plot in which all the samples or features S1 to S30 are obtained in cluster form at certain places.
Fig3 gives the plot of Time(in Hours) of sample collection with the distinct samples/features.

Conclusion:

PCA has provided us the uncorrelated features in clustered form together.So,we can infer that among those 30 distinct features(S1-S30) all are not useful as there are many redundant features.To remove this redundancy,PCA does a unique job of feature selection of any one among each cluster.To elaborate this we can say,as in our result we have obtained 10 clusters each with 3 features,so all 30 features are not necessary to take,rather we can take any one feature among each cluster and then proceed to train and test our model to do further tasks.Thus in reduction of features and removing redundancy PCA is playing a pivotal role.

The comparison of Fig2 and Fig3 tells us that the same indexed features which are collected at a particular time(in Hours) are also seen to form clusters at one place in the PC1 vs PC2 plot.So,taking one cluster (say S1,S2,S3)at a time we can infer that since at same point of time those 3 features were collected,so only those 3 indexed fetures are clustered at one place in Fig2.
This observation means that the given complete dataset is full of time dependent redundancy that can be removed by PCA very effectively.