import networkx as nx
import random

def generate_directed_lfr(
    n, tau1, tau2, mu, avg_deg, max_deg, min_comm, max_comm, seed
):
    # Generate undirected LFR graph
    G = nx.LFR_benchmark_graph(
        n=n,
        tau1=tau1,
        tau2=tau2,
        mu=mu,
        average_degree=avg_deg,
        max_degree=max_deg,
        min_community=min_comm,
        max_community=max_comm,
        seed=seed
    )

    # Convert to directed by assigning random directions to each edge
    DG = nx.DiGraph()
    for u, v in G.edges():
        if random.random() < 0.5:
            DG.add_edge(u, v)
        else:
            DG.add_edge(v, u)

    return DG

# Parameter sets
params = [
    (710, 4.0, 1.2, 0.28, 28, 110, 20, 100, 1),
    (715, 3.9, 1.5, 0.35, 30, 120, 25, 120, 2),
    (705, 4.3, 1.1, 0.39, 27, 105, 30, 150, 3),
]

# Generate and save each graph
for i, p in enumerate(params, start=1):
    G = generate_directed_lfr(*p)
    filename = f"lfr_directed_{i}.txt"
    with open(filename, "w") as f:
        for u, v in G.edges():
            f.write(f"{u} {v} 1\n")
    print(f"Saved {filename} with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")