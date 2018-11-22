
def improveLabels(val):

    for u in S:
        lu[u] -= val
    for v in V:
        if v in T:
            lv[v] += val
        else:
            minSlack[v][0] -= val


def improveMatching(v):

    u = T[v]
    if u in Mu:
        improveMatching(Mu[u])
    Mu[u] = v
    Mv[v] = u


def slack(u, v): return lu[u] + lv[v] - w[u][v]


def solve():

    while True:
        ((val, u), v) = min([(minSlack[v], v) for v in V if v not in T])

        if val > 0:
            improveLabels(val)

        T[v] = u  # add (u,v) to the tree
        if v in Mv:
            u1 = Mv[v]  # matched edge,

            S[u1] = True  # ... add endpoint to tree
            for v in V:  # maintain minSlack
                if not v in T and minSlack[v][0] > slack(u1, v):
                    minSlack[v] = [slack(u1, v), u1]
        else:
            improveMatching(v)
            return


def result(weights):

    global U, V, S, T, Mu, Mv, lu, lv, minSlack, w
    w = weights
    n = len(w)

    U = V = range(n)
    lu = [max([w[u][v] for v in V]) for u in U]
    lv = [0 for v in V]

    Mu = {}
    Mv = {}

    while len(Mu) < n:
        free = [u for u in V if u not in Mu]
        u0 = free[0]
        S = {u0: True}
        T = {}
        minSlack = [[slack(u0, v), u0] for v in V]
        solve()


    val = sum(lu) + sum(lv)
    return val


n = 3
w = [[0 for v in range(n)] for u in range(n)]
w=[[15.9, 4, 5],
   [5, 7, 6],
   [5, 8, 8]]

print(result(w))