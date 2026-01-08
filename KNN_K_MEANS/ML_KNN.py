# LIBRARY #
import math

# FUNGSI DAN PROSEDUR #

# inisialisasi centroid
def init_centroid(c1, c2):
    return [c1, c2]

#  Jarak
def euclidean(a, b):
    return math.sqrt(sum((a[i] - b[i])**2 for i in range(len(a))))

# Mengelompokkan (Clustering)
def cluster(x, centroid):
    klaster = []
    
    for i in x:
        jarak = [euclidean(i, c) for c in centroid]
        klaster.append(jarak.index(min(jarak)))
    return klaster

# Update centroid
def update_centroid(x, clusters, k):
    new_centroid = []
    
    for i in range(k):
        anggota = [x[j] for j in range(len(x)) if clusters[j] == i]
        centroid = [sum(col)/len(col) for col in zip(*anggota)]
        new_centroid.append(centroid)
    return new_centroid

# INISIALISASI #

X = [
    [2, 4],
    [4, 6],
    [4, 8],
    [6, 8],
    [6, 6],
    [8, 8],
    [8, 6],
    [8, 4]
]

c1 = [4, 6]
c2 = [8, 8]

max_iter = 10
k = 2

# MAIN PROGRAM #

centroid = init_centroid(c1, c2)
for _ in range(max_iter):
    klaster = cluster(X, centroid)
    centroid = update_centroid(X, klaster, k)
print (klaster, centroid)