def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res=0
    for i in range(len(x)):
        res+=abs(x[i]-y[i])
    return res

def jaccard_dist(x, y):
    intersection=len(list(set(x).intersection(y)))
    unions=len(list(x))+len(list(y))-intersection
    if unions==0:
        return 1
    sim=float(intersection)/unions
    return 1-sim

def cosine_sim(x, y):
    dot=0
    xs=0
    ys=0
    for i in range(len(x)):
        dot+=x[i]*y[i]
        xs+=x[i]**2
        ys+=y[i]**2
    sca=xs**0.5*(ys**0.5)
    if sca==0:
        return 0.5
    sim=dot/sca
    return sim

# Feel free to add more
