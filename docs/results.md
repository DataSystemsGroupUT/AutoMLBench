
# Results
* [Tables and Results Summaries](#tables-and-results-summaries)
  * [Summary of Frameworks](#summary-of-frameworks)
  * [Vanilla Version Vs Meta-learning](#vanilla-version-vs-meta-learning)
  * [Wilcoxon Test Summary](#wilcoxon-test-summary)
    * [10  Minutes](#10-minutes)
    * [30  Minutes](#30-minutes)
    * [60  Minutes](#60-minutes)
    * [240  Minutes](#240-minutes)
* [Tools Performance Summary](#tools-performance-summary)
* [Impact of Meta-learning](#impact-of-meta-learning)
* [Impact of Ensembling](#impact-of-ensembling)
* [Impact of Combined Meta-Learning and Ensembling](#impact-of-combined-meta-learning-and-ensembling)
* [Impact of Time Budget](#impact-of-time-budget)
* [Impact of Search Space](#impact-of-search-space)



## Tables and Results Summaries

### Summary of Frameworks

| Time Budget | Framework | N | Mean | SD |
|---|---|---|---|---|
| 10 Min | ATM <br> AutoWeka <br> Recipe <br> AutoSKLearn-e <br> AutoSKLearn-m <br> AutoSKLearn-v <br> AutoSKLearn <br> SmartML <br> TPOT | 75 <br> 86 <br>33 <br>99 <br>99<br> 99 <br>99<br> 89<br> 43 | 0.888 <br>0.848<br> 0.84 <br>0.873 <br>0.87<br> 0.868 <br> 0.873<br> 0.799 <br>0.894 | 0.123 <br>0.161<br> 0.176 <br>0.139<br> 0.144 <br>0.145<br> 0.143 <br>0.212 <br>0.117 |
| 30 Min | ATM <br> AutoWeka <br> Recipe <br> AutoSKLearn-e <br> AutoSKLearn-m <br> AutoSKLearn-v <br> AutoSKLearn <br> SmartML <br> TPOT | 74 <br>90<br> 69<br> 99<br> 99 <br>99 <br>99 <br>90<br> 59 | 0.903<br> 0.845<br> 0.855 <br>0.88 <br>0.873<br> 0.873 <br>0.876 <br>0.808<br> 0.885 | 0.116<br> 0.161<br> 0.144<br> 0.136 <br>0.143 <br>0.142 <br>0.139 <br>0.199 <br>0.136 |
| 60 Min | ATM <br> AutoWeka <br> Recipe <br> AutoSKLearn-e <br> AutoSKLearn-m <br> AutoSKLearn-v <br> AutoSKLearn <br> SmartML <br> TPOT | 79 <br>91 <br>76 <br>99<br> 99<br> 99<br> 99<br> 89<br> 70 | 0.89<br> 0.844 <br>0.864 <br>0.884<br> 0.873<br> 0.874 <br>0.882 <br>0.816 <br>0.89 | 0.126 <br>0.157 <br>0.139 <br>0.132<br> 0.141 <br>0.137 <br>0.133 <br>0.194 <br>0.131 |
| 240 Min | ATM <br> AutoWeka <br> Recipe <br> AutoSKLearn-e <br> AutoSKLearn-m <br> AutoSKLearn-v <br> AutoSKLearn <br> SmartML <br> TPOT | 86<br> 96<br> 85<br> 99 <br>99 <br>99<br> 99 <br>89 <br>89 | 0.895<br> 0.845<br> 0.859<br> 0.886<br> 0.877<br> 0.875<br> 0.887 <br>0.826<br> 0.893 | 0.123 <br>0.159<br> 0.155 <br>0.13 <br>0.136<br> 0.141<br> 0.13 <br>0.169 <br>0.126 |

### Vanilla Version Vs Meta-learning

| Time Budget | Framework  | N  | Mean | SD |
|---|---|---|---|---|
| 10 Min | AutoSKLearn-m  <br>AutoSKLearn-v | 99<br>99 | 0.87 <br>0.868 | 0.144 <br>0.145 |
| 30 Min | AutoSKLearn-m  <br>AutoSKLearn-v | 99<br>99 | 0.873 <br>0.873 | 0.143<br>0.142 |
| 60 Min | AutoSKLearn-m  <br>AutoSKLearn-v | 99<br>99 | 0.873<br>0.874 | 0.141<br>0.137 |
| 240 Min | AutoSKLearn-m  <br>AutoSKLearn-v | 99<br>99 | 0.877 <br>0.872 | 0.136<br>0.149 |

### Wilcoxon Test Summary

#### 10 Minutes

|ATM | AutoWeka | Recipe | Auto SKLearn-e | Auto SKLearn-m | Auto SKLearn-v | Auto SKLearn | SmartML | TPOT|
|---|---|---|---|---|---|---|---|---|
|ATM | 0.002 | 0.313 | 0.965 | 0.557 | 0.527 | 0.446 | 0.044 | 0.597|
|AutoWeka | 0.002 | 0.050 | 0.000 | 0.000 | 0.000 | 0.000 | 0.143 | 0.053|
|Recipe | 0.313 | 0.050 | 0.023 | 0.072 | 0.399 | 0.004 | 0.214 | 0.386|
|AutoSKLearn-e | 0.965 | 0.000 | 0.023 | 0.941 | 0.016 | 0.006 | 0.001 | 0.737|
|AutoSKLearn-m | 0.557 | 0.000 | 0.072 | 0.941 | 0.007 | 0.008 | 0.000 | 0.288|
|AutoSKLearn-v | 0.527 | 0.000 | 0.399 | 0.016 | 0.007 | 0.000 | 0.004 | 0.017|
|AutoSKLearn | 0.446 | 0.0 | 0.004 | 0.006 | 0.008 | 0.0 | 0.0 | 0.491|
|SmartML | 0.044 | 0.143 | 0.214 | 0.001 | 0.0 | 0.004 | 0.0 | 0.002|
|TPOT | 0.597 | 0.053 | 0.386 | 0.737 | 0.288 | 0.017 | 0.491 | 0.002|

#### 30 Minutes

|ATM | AutoWeka | Recipe | Auto SKLearn-e | Auto SKLearn-m | Auto SKLearn-v | Auto SKLearn | SmartML | TPOT|
|---|---|---|---|---|---|---|---|---|
|ATM | 0.002 | 0.26 | 0.981 | 0.283 | 0.136 | 0.883 | 0.002 | 0.87|
|AutoWeka | 0.002 | 0.322 | 0.0 | 0.0 | 0.0 | 0.0 | 0.565 | 0.001|
|Recipe | 0.26 | 0.322 | 0.0 | 0.002 | 0.048 | 0.0 | 0.021 | 0.0|
|AutoSKLearn-e | 0.981 | 0.0 | 0.0 | 0.001 | 0.0 | 0.209 | 0.0 | 0.917|
|AutoSKLearn-m | 0.283 | 0.0 | 0.002 | 0.001 | 0.093 | 0.137 | 0.0 | 0.124|
|AutoSKLearn-v | 0.136 | 0.0 | 0.048 | 0.0 | 0.093 | 0.002 | 0.007 | 0.002|
|AutoSKLearn | 0.883 | 0.0 | 0.0 | 0.209 | 0.137 | 0.002 | 0.0 | 0.137|
|SmartML | 0.002 | 0.565 | 0.021 | 0.0 | 0.0 | 0.007 | 0.0 | 0.0|
|TPOT | 0.87 | 0.001 | 0.0 | 0.917 | 0.124 | 0.002 | 0.137 | 0.0|

#### 60 Minutes

|ATM | AutoWeka | Recipe | Auto SKLearn-e | Auto SKLearn-m | Auto SKLearn-v | Auto SKLearn | SmartML | TPOT|
|---|---|---|---|---|---|---|---|---|
|ATM | 0.001 | 0.176 | 0.083 | 0.482 | 0.585 | 0.14 | 0.001 | 0.093|
|AutoWeka | 0.001 | 0.081 | 0.0 | 0.0 | 0.0 | 0.0 | 0.345 | 0.0|
|Recipe | 0.176 | 0.081 | 0.0 | 0.025 | 0.01 | 0.0 | 0.014 | 0.0|
|AutoSKLearn-e | 0.083 | 0.0 | 0.0 | 0.007 | 0.001 | 0.326 | 0.0 | 0.32|
|AutoSKLearn-m | 0.482 | 0.0 | 0.025 | 0.007 | 0.544 | 0.0 | 0.001 | 0.027|
|AutoSKLearn-v | 00.585 | 0.0 | 0.01 | 0.001 | 0.544 | 0.0 | 0.003 | 0.006|
|AutoSKLearn | 0.14 | 0.0 | 0.0 | 0.326 | 0.0 | 0.0 | 0.0 | 0.686|
|SmartML | 0.001 | 0.345 | 0.014 | 0.0 | 0.001 | 0.003 | 0.0 | 0.0|
|TPOT | 0.093 | 0.0 | 0.0 | 0.32 | 0.027 | 0.006 | 0.686 | 0.0|

#### 240 Minutes

|ATM | AutoWeka | Recipe | Auto SKLearn-e | Auto SKLearn-m | Auto SKLearn-v | Auto SKLearn | SmartML | TPOT|
|---|---|---|---|---|---|---|---|---|
|ATM | 0.045 | 0.101 | 0.535 | 0.877 | 0.788 | 0.561 | 0.001 | 0.092|
|AutoWeka | 0.045 | 0.487 | 0.0 | 0.0 | 0.001 | 0.0 | 0.58 | 0.0|
|Recipe | 0.101 | 0.487 | 0.0 | 0.002 | 0.0 | 0.0 | 0.052 | 0.0|
|AutoSKLearn-e | 0.535 | 0.0 | 0.0 | 0.006 | 0.016 | 0.477 | 0.0 | 0.139|
|AutoSKLearn-m | 0.877 | 0.0 | 0.002 | 0.006 | 0.957 | 0.0 | 0.0 | 0.001|
|AutoSKLearn-v | 0.788 | 0.001 | 0.0 | 0.016 | 0.957 | 0.0 | 0.0 | 0.0|
|AutoSKLearn | 0.561 | 0.0 | 0.0 | 0.477 | 0.0 | 0.0 | 0.0 | 0.156|
|SmartML | 0.001 | 0.58 | 0.052 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0|
|TPOT | 0.092 | 0.0 | 0.0 | 0.139 | 0.001 | 0.0 | 0.156 | 0.0|

## Tools Performance Summary

![all1](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/all/001SuccessRateAll.png?token=ABVXF3UEUELS3V2WHMHMCNC6PSP5K)
![all2](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/all/002BestPerformanceAll.png?token=ABVXF3UWZPF5WZFEZY3XKU26PSQOM)
![all3](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/all/003WorstPerformanceAll.png?token=ABVXF3WSYE3I67I2ZZRELTC6PSQSI)
![all4](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/all/004BestTimeBudgetsAll.png?token=ABVXF3QRTGWNGPSMCMF2G5S6PSQV2)


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

