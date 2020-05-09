## Experimental Setup

### Benchmarking Environment

Our experiments have been conducted on Google Cloud machines, each machine is configured with 2 vCPUs, 7.5 GB RAM and ubuntu-minimal-1804-bionic. Since each programming language manages memory differently, Some memory leakage may happen. So, We have rebooted the machine after each run to ensure that each experiment has the same available memory size.


### Evaluation Metrics

We have considered two evaluation metrics: accuracy and F1 score. Accuracy is the most intuitive metric. it is simply the ratio of the correctly classified instances to the total number of instances. F1 Score is the weighted average of Recall and Precision which makes it an expressive performance metric for unbalanced datasets.
