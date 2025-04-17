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

# Original params (for reference)
# params = [
#     (710, 4.0, 1.2, 0.28, 28, 110, 20, 100, 1),
#     (715, 3.9, 1.5, 0.35, 30, 120, 25, 120, 2),
#     (705, 4.3, 1.1, 0.39, 27, 105, 30, 150, 3),
# ]

# New params with varied social network structures (corrected order)
params = [
    # Dense Social Network (Facebook-like: high connectivity, strong communities)
    (1000, 2.2, 1.2, 0.15, 20, 50, 20, 100, 1),
    
    # Sparse Professional Network (LinkedIn-like: fewer connections, clear hierarchy)
    (1000, 2.8, 1.8, 0.25, 8, 30, 10, 50, 2),
    
    # Scale-Free Social Network (Twitter-like: many weak ties, few strong hubs)
    (1000, 1.8, 1.5, 0.3, 12, 100, 5, 200, 3),
    
    # Tight-Knit Community Network (Family/Friend groups: strong local connections)
    (1000, 2.5, 1.3, 0.1, 15, 40, 30, 150, 4),
    
    # Mixed-Scale Network (Real-world social: combination of different scales)
    (1000, 2.0, 1.6, 0.2, 10, 80, 15, 120, 5)
]

# Generate and save each graph
for i, p in enumerate(params, start=1):
    G = generate_directed_lfr(*p)
    filename = f"lfr_directed_iter2_{i}.txt"
    with open(filename, "w") as f:
        for u, v in G.edges():
            f.write(f"{u} {v} 1\n")
    print(f"Saved {filename} with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")