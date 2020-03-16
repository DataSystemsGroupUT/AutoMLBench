
# Results
* [Tables and Results Summaries](#tables-and-results-summaries)
  * [Summary of Frameworks](#summary-of-frameworks)
* [Impact of Meta-learning](#impact-of-meta-learning)
* [Impact of Ensembling](#impact-of-ensembling)
* [Impact of Combined Meta-Learning and Ensembling](#impact-of-combined-meta-learning-and-ensembling)
* [Impact of Time Budget](#impact-of-time-budget)
* [Impact of Search Space](#impact-of-search-space)



## Tables and Results Summaries

### Summary of Frameworks

| Time Budget | Framework | N | Mean | SD |
|-------|---------------------------------------|--------------------|----------------------|------------------------------------|
| 10 Min | ATM <br> AutoWeka <br> Recipe <br> AutoSKLearn-e <br> AutoSKLearn-m <br> AutoSKLearn-v <br> AutoSKLearn <br> SmartML <br> TPOT | 75 <br> 86 <br>33 <br>99 <br>99<br> 99 <br>99<br> 89<br> 43 | 0.888 <br>0.848<br> 0.84 <br>0.873 <br>0.87<br> 0.868 <br> 0.873<br> 0.799 <br>0.894 | 0.123 <br>0.161<br> 0.176 <br>0.139<br> 0.144 <br>0.145<br> 0.143 <br>0.212 <br>0.117 |
| 30 Min | ATM <br> AutoWeka <br> Recipe <br> AutoSKLearn-e <br> AutoSKLearn-m <br> AutoSKLearn-v <br> AutoSKLearn <br> SmartML <br> TPOT | 74 <br>90<br> 69<br> 99<br> 99 <br>99 <br>99 <br>90<br> 59 | 0.903<br> 0.845<br> 0.855 <br>0.88 <br>0.873<br> 0.873 <br>0.876 <br>0.808<br> 0.885 | 0.116<br> 0.161<br> 0.144<br> 0.136 <br>0.143 <br>0.142 <br>0.139 <br>0.199 <br>0.136 |
| 60 Min | ATM <br> AutoWeka <br> Recipe <br> AutoSKLearn-e <br> AutoSKLearn-m <br> AutoSKLearn-v <br> AutoSKLearn <br> SmartML <br> TPOT | 79 <br>91 <br>76 <br>99<br> 99<br> 99<br> 99<br> 89<br> 70 | 0.89<br> 0.844 <br>0.864 <br>0.884<br> 0.873<br> 0.874 <br>0.882 <br>0.816 <br>0.89 | 0.126 <br>0.157 <br>0.139 <br>0.132<br> 0.141 <br>0.137 <br>0.133 <br>0.194 <br>0.131 |
| 4 Hours | ATM <br> AutoWeka <br> Recipe <br> AutoSKLearn-e <br> AutoSKLearn-m <br> AutoSKLearn-v <br> AutoSKLearn <br> SmartML <br> TPOT | 86<br> 96<br> 85<br> 99 <br>99 <br>99<br> 99 <br>89 <br>89 | 0.895<br> 0.845<br> 0.859<br> 0.886<br> 0.877<br> 0.875<br> 0.887 <br>0.826<br> 0.893 | 0.123 <br>0.159<br> 0.155 <br>0.13 <br>0.136<br> 0.141<br> 0.13 <br>0.169 <br>0.126 |

### Impact of Meta-learning
![meta1](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/006MetaLearningEffectAll10min.png)
![meta2](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/007MetaLearningEffectAll30min.png)
![meta3](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/008MetaLearningEffectAll60min.png)
![meta4](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/009MetaLearningEffectAll4hours.png)


### Impact of Ensembling
![ensem1](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/011EnsemblingEffectAll10min.png)
![ensem2](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/012EnsemblingEffectAll30min.png)
![ensem3](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/013EnsemblingEffectAll60min.png)
![ensem4](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_Ensembling_(4_Hours).png)

### Impact of Combined Meta-Learning and Ensembling
![comb1](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_Combined_Meta-Learning_and_Ensembling._(10_Min).png)
![comb2](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_Combined_Meta-Learning_and_Ensembling._(30_Min).png)
![comb3](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_Combined_Meta-Learning_and_Ensembling._(60_Min).png)
![comb4](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_Combined_Meta-Learning_and_Ensembling._(4_Hourse).png)
### Impact of Time Budget
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn_(30_Min-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn_(60_Min-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn_(4_Hours-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn_(60_Min-30_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn_(4_Hours-30_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn_(4_Hours-60_Min).png)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-m_(30_Min-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-m_(60_Min-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-m_(4_Hours-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-m_(60_Min-30_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-m_(4_Hours-30_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-m_(4_Hours-60_Min).png)


![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-e_(30_Min-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-e_(60_Min-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-e_(4_Hours-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-e_(60_Min-30_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-e_(4_Hours-30_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-e_(4_Hours-60_Min).png)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-v_(30_Min-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-v_(60_Min-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-v_(4_Hours-10_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-v_(60_Min-30_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-v_(4_Hours-30_Min).png)
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/bench_figs/Effect_of_time_budget_Increasing_for_AutoSKLearn-v_(4_Hours-60_Min).png)
### Impact of Search Space
![size](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/Accuracyfcand3cfor30minutes.png)

