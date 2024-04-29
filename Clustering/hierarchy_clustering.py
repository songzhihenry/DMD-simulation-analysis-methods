#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:38:40 2022

@author: zhiyuas
"""

from scipy.cluster import hierarchy
import argparse
from matplotlib import pyplot as plt
#pair-wise matrix (n x n),the element i-j (j > i) corresponds to (2*n-1-i)*i/2+j-i-1 in condensed array
def pw_to_cd(i,j,n):
    return int((2*n-1-i)*i/2+j-i-1)
parser = argparse.ArgumentParser()
parser.add_argument('ocinput',help='oc.input file or pw_rmsd file needed',type=str)
parser.add_argument('n_clusters',help='Num. of clusters wanted',type=int)
parser.add_argument('method',help='HC algorithm, including single(min), complete(max), average(mean), centroid, median, ward', type=str)
args = parser.parse_args()
ocinput = [line.strip('\n') for line in open('{}'.format(args.ocinput))]
n_snaps = int(ocinput[0])
snap_names = ocinput[1:n_snaps+1]
ytdist = list(map(float, ocinput[n_snaps+1:]))
n_k = args.n_clusters
method = args.method
Z = hierarchy.linkage(ytdist, method=method)
dn = hierarchy.dendrogram(Z,p=n_k,truncate_mode='lastp',\
    labels=snap_names,show_leaf_counts=True)
result = hierarchy.fcluster(Z, t=n_k, criterion='maxclust')
clusters = dict([(i, []) for i in range(1,1+n_k)])
for i in range(n_snaps):
    clusters[result[i]].append(i)

for i in range(1,1+n_k):
    #find centoids
    sum_sum = []
    for w in clusters[i]:
        dist_sum = 0
        for q in clusters[i]:
            if w == q:
                continue
            if w > q:
                ww = q
                qq = w
                dist_sum = dist_sum + ytdist[pw_to_cd(ww,qq,n_snaps)]
            else:
                dist_sum = dist_sum + ytdist[pw_to_cd(w,q,n_snaps)]
        sum_sum.append(dist_sum)
    centroid_index = clusters[i][sum_sum.index(min(sum_sum))]
    print ('Cluster {}; Cluster size: {}; Centroid: {}'.format(i,len(clusters[i]),snap_names[centroid_index]))
plt.savefig('dendrogram.png')
