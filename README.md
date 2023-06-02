# Pylogenetic reconstruction of Rosa x binaloudensis plant using trained random forest model

## Problem

One of the most promising methods of phylogetic tree construction is maximum likelihood method.This method uses searching algorithms by constructing different versions of a initial tree and assign a likelihood to it.One of these algorithms is SPR.In this algorithm the initial tree is pruned from certain points and regrafted again based on criteria and for each new build tree mll computation is done.

The drawback of using this method is the high cost of calculating likelihood for these trees.So The prediction approach is usually acquired.One of the state-of-art methods are machine-learning-based methods.On a research, using machine learning for predicting maximum likelihood on a spr algorithm has intruduced (see the reference).

This projects aims to apply this open-source approach for using in reconstructing a new identified species Rosa x binaloudensis and compare it with current approaches.So the trained model gets a list of SPR neighbour candidate and it returns the predicted likelihood for each version.

## Procedure

#### model prepration

In this step the original code of the mentioned paper used.but it customized to the vision of the project and datasets accordingly.
The dataset contains of multiple sequence alignment of each datapoint which was collected from PloiDB and TreeBase.Then :

-Initial starting tree is build using `phyml 3.01` linux software

-SPR neighbours for the corresponding tree acquired.

-log-likelihood for each calculated using `raxml-ng linux`

-feature selection done by using most promising features needed to construct a tree

-training the random forest model with tree-likelihood pairs

#### Tree construction

At first multiple sequence alignment of the phylogenetic data of Rosa x binaloudensis which first introduced by a research done by using `BioEdit` software.Then using the mentioned code, initial tree and neighbouring trees built up.Then passed to the model for predictoin.Evaluation made and predicted tree visualized

## Setup
  -Unzip the mode `finalized_model.zip`
  
  -Use `predictor.py` to generate log-likehood predictions.
  
  NOTE: tree extraction module has to be fixed.As the index of input data (in CSV) is same as output of model.You can find the best tree version by index of the output in input.By knowing the name of the sub_trees you can acquire tree representation in newick format.
  
  -Use `visualizer.py` to visualize the predicted tree using ete module.
  
  -Use `evaluator.py` to compare original versus predicted model using robinsoun-floud metric.
  
#### File System

-`data` : contains training_data , validation_data and data related to Rosa x binaloudensis (initial tree,spr collection,input data,out data)

-`softwares`: linux version of used phyml and raxml-ng softwared included

-`training` : all the modules related to training the model.

## Results

- The following result are correlation value for the model

- you can see the predicted tree versus the original tree obtained from other methods in the paper 2

![](predicted_tree.pdf)

- Comparision result of robinson-floud metric shows rf/maxrf is 2/36 which the normalized indicate good similarity.

## References

1- [Azouri, D., Abadi, S., Mansour, Y. et al. Harnessing machine learning to guide phylogenetic-tree search algorithms. Nat Commun 12, 1983 (2021). https://doi.org/10.1038/s41467-021-22073-8](https://www.nature.com/articles/s41467-021-22073-8)

2- [Origin of Rosa x binaloudensis (Rosaceae), a new natural hybrid species from Iran](https://www.biotaxa.org/Phytotaxa/article/view/phytotaxa.411.1.2)  
