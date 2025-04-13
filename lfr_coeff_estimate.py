import networkx as nx
import powerlaw
from networkx.algorithms.community import louvain_communities

# Load directed graph
G = nx.read_edgelist("wiki_cleaned.txt", create_using=nx.DiGraph(), nodetype=int, data=(('weight', int),))

# Degree analysis
degrees = [G.in_degree(n) + G.out_degree(n) for n in G.nodes()]
avg_deg = sum(degrees) / len(degrees)
max_deg = max(degrees)

# Tau1 estimation
fit_deg = powerlaw.Fit(degrees, discrete=True)
tau1 = fit_deg.power_law.alpha

# Convert to undirected for community detection
G_undirected = G.to_undirected()
communities = list(louvain_communities(G_undirected))

# Community size power law
comm_sizes = [len(c) for c in communities]
fit_comm = powerlaw.Fit(comm_sizes, discrete=True)
tau2 = fit_comm.power_law.alpha
min_comm = min(comm_sizes)
max_comm = max(comm_sizes)

# Mixing parameter
def compute_mu_directed(G, communities):
    node_to_comm = {}
    for i, comm in enumerate(communities):
        for node in comm:
            node_to_comm[node] = i
    inter = sum(1 for u, v in G.edges() if node_to_comm.get(u) != node_to_comm.get(v))
    return inter / G.number_of_edges()

mu = compute_mu_directed(G, communities)

print("Average degree:", avg_deg)
print("Max degree:", max_deg)
print("Tau1 (deg exp):", tau1)
print("Tau2 (comm size exp):", tau2)
print("Min comm size:", min_comm)
print("Max comm size:", max_comm)
print("Mu (mixing):", mu)