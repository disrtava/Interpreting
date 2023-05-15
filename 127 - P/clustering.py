from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns 
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

radius = df.iloc[:, 0].values
mass = df.iloc[:, 1].values

X = np.array(list(radius, mass))

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


plt.figure(figsize = (10,5))
sns.lineplot(x = range(1,11),y = wcss,marker = 'o',color = 'red')
plt.title('The Elbow Method')
plt.xlabel('No of clusters')
plt.ylabel('WCSS')
plt.show()