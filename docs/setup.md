## Experimental Setup

### Benchmarking Environment

Our experiments have been conducted on Google Cloud machines; each machine is configured with 2 vCPUs, 7.5 GB RAM, and ubuntu-minimal-1804-bionic. Since each programming language manages memory differently, Some memory leakage may happen. So, We have rebooted the machine after each run to ensure that each experiment has the same memory size.


### Evaluation Metrics

We used the F1 Score to evaluate the predictive performance. The F1 Score is the weighted average of Recall and Precision, making it an expressive performance metric, especially for unbalanced datasets.
