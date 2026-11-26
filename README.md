# A one-step nullhomotopy for Čech complexes of hypercube graphs

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

For a graph G and an integer r >= 0 let N(G,r) be the nerve of the closed balls of radius r/2 about the vertices of G in its geometric realization. Adams, Shukla and Singh (Čech complexes of hypercube graphs, Homology Homotopy Appl. 27 (2025) 83-105, doi:10.4310/HHA.2025.v27.n1.a6, arXiv:2212.05871) proved that the inclusion of N(Q_n,r) into N(Q_n,r+2) is null-homotopic for the hypercube graph Q_n, and asked (Question 7.5) whether the inclusion into N(Q_n,r+1) is null-homotopic as well. We show that it is, for every n >= 1 and r >= 0. Consequently every bar in the reduced Čech persistence barcode of Q_n over integer scales lives at a single scale. The proof rests on a lemma for graph maps into a bipartite graph that agree up to one edge at every vertex, and it applies equally to Cartesian products of trees.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/check_one_step.py`: tests both contiguities of the proof of Theorem 1.1 for the coordinate clamps of Q_n, computing the maximal simplices of N(Q_n,r) from points of the geometric realization rather than from the lemma used in the proof. At odd r it also counts failures of the direct contiguity, which the intermediate map avoids. Run `python3 check_one_step.py 5` for n <= 5 and every r <= 2n; standard library only, a few minutes.
- `SHA256SUMS`: sha256 of each file above.
