import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph

# Function to assign colors to vertices of graph
def greedy_coloring(g):

	# stores color assigned to each vertex
	result = {}

	# assign color to vertex one by one
	for u in g.nodes():
		# set to store color of adjacent vertices of u
		# check colors of adjacent vertices of u and store in set
		assigned = set([result.get(i) for i in list(G.neighbors(u)) if i in result])

		# check for first free color
		color = 0
		for c in assigned:
			if color != c:
				break
			color = color + 1

		# assigns vertex u the first available color
		result[u] = color

	return result


# Greedy coloring of graph
if __name__ == '__main__':

	# Colors to pint vertex
	colors = ["green", "red", "yellow", "orange", "pink", "blue", "white", "maroon", "grey", "teal", "coral",
			"navy", "aqua", "lime", "purple", "brown", "black"]

	# GEneration of random graph, n=number of nodes with p probability of have an edge
	G = nx.gnp_random_graph(n=20, p=0.5, seed=4)

	result = greedy_coloring(G)
	colours_used = [colors[i] for i in list(result.values())]

	pos = nx.spring_layout(G)
	nx.draw(G, pos, nodelist=sorted(G.nodes()), node_color=colours_used, with_labels=True,
			node_size=150, font_size=8, font_weight='bold')

	plt.savefig("colored_graph.png", format="PNG", dpi=190)

	print("################# RESULTS #################")
	print(f"Nodes: {G.nodes()}")
	print(f"Adjacent vertices: {G.edges()}")
	# print(f"Number of colours used: {len(set(colours_used))}")
	print(f"Number of colors should use: {max(list(result.values()))+1}")
