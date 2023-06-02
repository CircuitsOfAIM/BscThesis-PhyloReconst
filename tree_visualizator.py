from ete3 import Tree

# Read the Newick tree file
with open('orginal_prunebased.newick', 'r') as file:
    newick_string = file.read().strip()

# Create a Tree object from the Newick string
tree = Tree(newick_string,format=1, quoted_node_names=True)

# Visualize the tree
tree.show()
