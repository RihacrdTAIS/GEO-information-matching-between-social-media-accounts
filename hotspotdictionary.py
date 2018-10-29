import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans
import csv
with open('matching_train.csv','r') as csvfile: 
    with open('dictionary_hotspot.csv','w') as cf:
        reader = csv.reader(csvfile)
        fieldnames = ['user', 'longtitude','latitude']
        writer = csv.DictWriter(cf, fieldnames=fieldnames)
        test={}
        for line in reader:
            ins,tw,text,location1,location2 = line
            if test.has_key(tw) == False:
                test[tw] = [[location1,location2]]
            else:
                test[tw].append([location1,location2])
        for key,value in test.items():
           # print key, value
            X = np.array(value)
	    X = X.astype(np.float64) 
            clustering = DBSCAN(eps=0.0045, min_samples=4).fit(X)
            L=[]
            L=clustering.labels_
            M=[]
            for i in range(0,10):
                N=[]
                for label in range(len(L)):
                    if L[label] == i:
                    #print X[label]
                        N.append(X[label])
                if len(N) > 0:
                    kmeans = KMeans(n_clusters=1, random_state=0).fit(N)
                    kmeans.predict(N)
                    M.append(kmeans.cluster_centers_)
            for j in range(len(M)):
	#	print M[j]
                [[la,lo]] = M[j]
                writer.writerow({'user': key , 'longtitude': lo, 'latitude': la})
                
