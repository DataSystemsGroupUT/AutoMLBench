# AUTOML tools 

- [AutoSklearn](#autosklearn)
- [TPOT](#tpot)
- [Recipe](#recipe)
- [ATM](#atm)
- [AutoWeka](#autoweka)
- [SmartML](#smartml)

## AutoSklearn 
#### [docs](https://automl.github.io/auto-sklearn/master/)
AutoSklearn is an autoML tool that has been implemented on top of Scikit-Learn, a popular Python machine learning package. AutoSklearn introduced the idea of meta-learning in the initialization of combined algorithm selection and hyperparameter tuning. It used SMAC as a Bayesian optimization technique too. Besides, ensemble methods were used to improve the performance of output models. Both meta-learning and ensemble methods improved the performance of vanilla SMAC optimization.

## TPOT 
#### [docs](http://automl.info/tpot/)
TPOT framework represents another type of solution that has been implemented on top of Scikit-Learn. It is based on genetic programming by exploring many different possible pipelines of feature engineering and learning algorithms. 

## Recipe 
#### [source](https://github.com/laic-ufmg/Recipe)

Recipe follows the same optimization procedure as TPOT using genetic programming, which in turn exploits the advantages of a global search. However, it considers the unconstrained search problem in TPOT, where resources can be spent into generating and evaluating invalid solutions by adding a grammar that avoids the generation of invalid pipelines and can speed up the optimization process. It works with a bigger search space of different model config-urations than AutoSkLearn and TPOT.

## ATM 
#### [docs](https://hdi-project.github.io/ATM/)

Auto-Tuned Models (ATM) framework that has been introduced as a parallel framework for fast optimization of machine learning modeling pipelines. In particular, this framework depends on parallel execution along with multiple nodes/cores with a shared model hub that stores the results out of these executions and tries to enhance the selection of other pipelines that can outperform the current chosen ones. ATM is implemented based on two searching methods, a hybrid Bayesian and multi-armed bandit optimization system which are used to traverse the search space and report the target pipeline.

## AutoWeka 
#### [docs](https://www.cs.ubc.ca/labs/beta/Projects/autoweka/)

Auto-Weka is  considered  as  the  first  and  pioneer machine learning automation framework. It was implemented in  Java  on  top  of  Weka,  a  popular  machine  learning  library  that  has  a  wide  range  of  machine  learning  algorithms. Auto-Weka  applies  Bayesian  optimization  using  Sequential Model-based  Algorithm  Configuration  (SMAC)  and  tree-structured parzen estimator (TPE) for both algorithm selection and hyper-parameter optimization (Auto-Weka uses SMAC asits  default  optimization  algorithm  but  the  user  can  configure the tool to use TPE).

## SmartML 
#### [SOURCE](https://github.com/DataSystemsGroupUT/SmartML)

SmartML has been introduced as the first R package for automated model building for classification tasks. In the algorithm selection phase, SmartML uses a meta-learning approach where the meta-features of the input dataset is extracted and compared with the meta-features of the datasets that are stored in the framework’s knowledge base, populated from the results of the previous runs. The similarity search process is used to identify the similar datasets in the knowledge base, using the nearest neighbor approach, where the retrieved results are used to identify the best performing algorithms on those similar datasets to nominate the candidate algorithms for the dataset at hand. The hyperparameter tuning of SmartML is based on SMAC Bayesian Optimisation. SmartML maintains the results of the new runs to continuously enrich its knowledge base to further improve the accuracy of the similarity search and thus the performance and robustness for future runs.
