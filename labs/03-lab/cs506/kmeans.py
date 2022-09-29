from collections import defaultdict
from math import inf
import random
import csv


def get_centroid(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    x=0
    y=0
    length=len(points)
    for i in range(length):
        x+=points[i][0]
        y+=points[i][1]
    mean=[(x/length),(y/length)]
    return mean

def get_centroids(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the centroid for each of the assigned groups.
    Return `k` centroids in a list
    """
    mean=[]
    for i in range(len(assignments)):
        x=0
        y=0
        for j in range(len(assignments[i])):
            x+=(assignments[i])[j][0]
            y+=(assignments[i])[j][1]
        mean.append=[(x/len(assignments[i])),(y/len(assignments[i]))]
    return mean

    


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i])**2
    return res**(1/2)


def distance_squared(a, b):
    res = 0
    for i in range(len(a)):
        res += (a[i] - b[i])**2
    return res


def cost_function(clustering):
    #for points in clustering, we use n
    n=len(clustering)
    #for mean we use the previous function
    c=get_centroid(clustering)
    distance=0
    for i in range(n):
        distance+=distance_squared(clustering[i],c)
    return distance

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    a=len(dataset)
    b=[]
    for i in range(a):
        b.append(dataset[i])
    c=min(b)
    r=[]
    for i in range(k):
        d=random.randint(0,a)
        e=random.randint(0,b)
        r.append([d,e])
    return r



def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    
    raise NotImplementedError()


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = get_centroids(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
