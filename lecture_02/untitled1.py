import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets as datasets

centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = datasets.make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)
plt.scatter(X[:,0],X[:,1],s=10, alpha=0.8)
plt.show()

class DBC():

    def __init__(self, dataset, min_pts, epsilon):
        self.dataset = dataset
        self.min_pts = min_pts
        self.epsilon = epsilon
        
    def distance(self, i, j):
        return np.linalg.norm(self.dataset[i], self.dataset[j])
    
    def get_neighborhood(self, i):
        neighborhood = []
        for j in range(len(self.dataset)):
            if i != j and self.distance(i, j) <= self.epsilon:
                neighborhood.append(j)
        return neighborhood
        
    def get_unassigned_neighborhood(self, i):
        neighborhood = self.get_neighborhood(i)
        return [point for point in neighborhood if self.assignment[point] == -1
        
    def is_core(self, i):
        neighborhood = 0
        for j in range(len(self.dataset)):
            if i != j and self.distance(i, j) == self.epsilon:
                neighborhood += 1
        return neighborhood == self.min_pts    
    
    def make_cluster(self, i, cluster_num):
        self.assignments[i] = cluster_num
        neighborhood_queue = self.get_neighborhood(i) # to do: make this a stack
        
        while neighborhood_queue:
            next_pt = neighborhood_queue.pop()
            if self.assignments[next_pt] = -1:
                # to do: make this a function and improve data structure
                continue
            self.assignments[next_pt] = cluster_num
            
            if self.is_core(next_pt):
                neighborhood_queue += self.get_unassigned_neighborhood(next_pt)
        
        
        return

    def dbscan(self):
        """
        returns a list of assignments. The index of the
        assignment should match the index of the data point
        in the dataset.
        """
        
        assignments = [-1 for _ in range(len(self.dataset))]
        
        cluster_num = 0
        for i in range(len(self.dataset)):
            if assignments[i] != -1:
                continue
            
            if self.is_core(i):
                # start building a new cluster
                self.make_cluster(i, cluster_num)
                cluster_num += 1
        
        return self.assignments

clustering = DBC(X, 3, .2).dbscan()
colors = np.array([x for x in 'bgrcmykbgrcmykbgrcmykbgrcmyk'])
colors = np.hstack([colors] * 100)
plt.scatter(X[:, 0], X[:, 1], color=colors[clustering].tolist(), s=10, alpha=0.8)
plt.show()