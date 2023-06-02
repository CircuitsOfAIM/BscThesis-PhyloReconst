from ete3 import Tree
predictedtree = Tree('./data/rosab_data/predictedvaeztree.newick',format=1,quoted_node_names=True)
referencetree = Tree('./data/rosab_data/orginal_prunebased.newick',format=1,quoted_node_names=True)
rf, max_rf, common_leaves, parts_t1, parts_t2, discard_t1, discart_t2  = referencetree.robinson_foulds(predictedtree,unrooted_trees=True)


# Open the file in write mode
with open("evaluation.txt", "w") as file:
    # Write the string data to the file
    file.write('rf: '+str(rf))
    file.write('\n')
    file.write('max_rf: '+str(max_rf))