import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Build Nodes
nodes = ["Andre", "Beverly", "Carol", "Diane", "Ed", "Fernando", "Garth", "Heather", "Ike", "Jane"]
G.add_nodes_from(nodes)

#Build Edges
edges = [   ("Andre", "Carol"), 
            ("Andre", "Diane"), 
            ("Andre", "Fernando"),

            ("Beverly", "Diane"), 
            ("Beverly", "Garth"), 
            ("Beverly", "Ed"),

            ("Carol", "Fernando"), 
            ("Carol", "Diane"),

            ("Diane", "Fernando"), 
            ("Diane", "Garth"), 
            ("Diane", "Ed"), 

            ("Ed", "Garth"), 

            ("Fernando", "Heather"),
            ("Garth", "Heather"),
             
            ("Heather", "Ike"), 

            ("Ike", "Jane")]

G.add_edges_from(edges)

pos = nx.spring_layout(G)

nx.draw(G, pos, 
        with_labels=True, node_color="green", 
        node_size=2000, edge_color="purple", 
        font_size=15, font_color="black", 
        font_weight="bold")

plt.title("Krackhardt Kite Graph")

plt.show()