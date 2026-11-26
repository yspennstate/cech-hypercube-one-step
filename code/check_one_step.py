"""Check of the one-step nullhomotopy for the Cech complexes N(Q_n, r) of hypercube graphs.

Maximal simplices of N(Q_n, r) are computed from points of the geometric realization (vertices and
edge points at t = j/8), as the sets {x : d(x, p) <= r/2}. For the clamp maps p_j (the first j bits set
to 0) the script tests, for n <= N and every r <= 2n, the contiguities used in the proof: p_j ~ p_{j+1} for
even r, and p_j ~ h_j ~ p_{j+1} through the even-parity map h_j for odd r. As a control it also counts
failures of the direct step p_j ~ p_{j+1} at odd r. Usage: python check_one_step.py [N] (default 4).
"""
import itertools, sys
from fractions import Fraction as F

def cube(n):
    V = list(range(1 << n))
    E = [(a, a ^ (1 << i)) for a in V for i in range(n) if a < a ^ (1 << i)]
    return V, E

def dist(a, b):
    return bin(a ^ b).count('1')

def ball_sets(n, r):
    """maximal sets {x : d(x,p) <= r/2} over sample points p of the realization."""
    V, E = cube(n)
    R = F(r, 2)
    sets = set()
    for a, b in E:
        for j in range(9):
            t = F(j, 8)
            S = frozenset(x for x in V if min(dist(x, a) + t, dist(x, b) + 1 - t) <= R)
            sets.add(S)
    maxi = [S for S in sets if not any(S < T for T in sets)]
    return maxi

def contiguous(f, g, src, tgt):
    bad = 0
    for S in src:
        img = {f[x] for x in S} | {g[x] for x in S}
        if not any(img <= T for T in tgt):
            bad += 1
    return bad

def h_of(f, g, V):
    h = {}
    for v in V:
        a, b = f[v], g[v]
        if a != b:
            h[v] = a if dist(a, 0) % 2 == 0 else b
        elif dist(a, 0) % 2 == 0:
            h[v] = a
        else:
            h[v] = a ^ 1
    return h

N = int(sys.argv[1]) if len(sys.argv) > 1 else 4
for n in range(1, N + 1):
    V, _ = cube(n)
    clamps = [{v: v & ~((1 << j) - 1) for v in V} for j in range(n + 1)]
    for r in range(0, 2 * n + 1):
        src, tgt = ball_sets(n, r), ball_sets(n, r + 1)
        tot = 0
        for f, g in zip(clamps, clamps[1:]):
            if r % 2 == 0:
                tot += contiguous(f, g, src, tgt)
            else:
                h = h_of(f, g, V)
                tot += contiguous(f, h, src, tgt) + contiguous(h, g, src, tgt)
        direct = sum(contiguous(f, g, src, tgt) for f, g in zip(clamps, clamps[1:]))
        print(f"n={n} r={r}: chain failures {tot}; direct-step failures {direct}")
