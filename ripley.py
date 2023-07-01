import numpy as np
from scipy.spatial import distance
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

def Kclust(pts, xlim, ylim, rseq, thseq, score=False, rlabel=False, report=True):
    N = pts.shape[0]
    D = distance.cdist(pts,pts)
    D = D[:N, :N]
    for r in rseq:
        K = np.sum(D <= r, axis=1) - 1
        L = np.sqrt((np.diff(xlim) * np.diff(ylim)) * K / (np.pi * (N - 1)))
        plt.plot(L)
        plt.show()
        for th in thseq:
            print(r,th)
            idx = np.argwhere(L < th)
            idxx = np.argwhere(L >= th)
            if len(idx) > 0:
                A = D < 2*r
                A = np.delete(A,idx,axis=0)
                A = np.delete(A,idx,axis=1)
                np.fill_diagonal(A,0)
                csr = csr_matrix(A)
                components, labels = connected_components(csr,directed=False)
                plt.scatter(pts[idxx, 0], pts[idxx, 1], c=labels, cmap='rainbow', s=1,marker='x')
                plt.scatter(pts[idx, 0], pts[idx, 1], color='black', s=1,marker='x')
                plt.show()

                
spots = pd.read_csv('data.txt')
rseq = np.arange(1.0,2.0,0.1)
thseq = np.linspace(0.1,4.0,10)
xlim = (spots['x'].min(),spots['x'].max())
ylim = (spots['y'].min(),spots['y'].max())
Kclust(spots[['x','y']].values,xlim,ylim,rseq,thseq)
