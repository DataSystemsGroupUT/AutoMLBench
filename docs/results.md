
# Results
* [Tables and Results Summaries](#tables-and-results-summaries)

* [Tools Performance Summary](#tools-performance-summary)
* [Impact of Time Budget](#impact-of-time-budget)
    * [Impact of Time Budget AutoSKLearn](#impact-of-time-budget-autosklearn)
    * [Impact of Time Budget TPOT](#impact-of-time-budget-tpot)
    * [Impact of Time Budget ATM](#impact-of-time-budget-atm)
* [Impact of Meta-learning](#impact-of-meta-learning)
* [Impact of Ensembling](#impact-of-ensembling)
* [Impact of Combined Meta-Learning and Ensembling](#impact-of-combined-meta-learning-and-ensembling)
* [Impact of Search Space](#impact-of-search-space)



## Tables and Results Summaries

### Comparison table of functionality of the AutoML frameworks

<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/d79bc51f0e4dafc00528b34e13890d1d89c95cc4/docs/data/tables/T1.png" alt="Comparison table of functionality of the AutoML frameworks considered in this study as of 24/12/2021" style="width:750px;"/>

</figure>

### Wilcoxon pairwise test p-values for AutoML frameworks over different time budgets.

<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/d79bc51f0e4dafc00528b34e13890d1d89c95cc4/docs/data/tables/T2.png" alt="Wilcoxon pairwise test p-values for AutoML frameworks over different time budgets." style="width:750px;"/>

</figure>

### Mean_Succ, Mean and standard deviation of the predictive performance of AutoML frameworks

<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/d79bc51f0e4dafc00528b34e13890d1d89c95cc4/docs/data/tables/T3.png" alt="Mean_Succ, Mean and standard deviation of the predictive performance of AutoML frameworks." style="width:750px;"/>

</figure>

### Summary of the impact of increasing the time budget.

<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/d79bc51f0e4dafc00528b34e13890d1d89c95cc4/docs/data/tables/T4.png" alt="Summary of the impact of increasing the time budget." style="width:750px;"/>

</figure>

### Wilcoxon test p-values for all the AutoML frameworks 
<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/d79bc51f0e4dafc00528b34e13890d1d89c95cc4/docs/data/tables/T5.png" alt="Wilcoxon test p-values for all the AutoML frameworks." style="width:750px;"/>

</figure>

### The performance of AutoSklearn-v and AutoSklearn-m and the gain in performance

<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/d79bc51f0e4dafc00528b34e13890d1d89c95cc4/docs/data/tables/T6.png" alt="The performance of AutoSklearn-v and AutoSklearn-m and the gain in performance." style="width:750px;"/>

</figure>

### Performance comparison between vanilla/base version vs ensembling version of AutoSKlearn and SmartML

<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/d79bc51f0e4dafc00528b34e13890d1d89c95cc4/docs/data/tables/T7.png" alt="Performance comparison between vanilla/base version vs ensembling version of AutoSKlearn and SmartML" style="width:750px;"/>

</figure>

## General performance trends of the benchmark AutoML frameworks

<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/67991ef92774380b30d7ccdd8ad68eec2c6a44a0/docs/data/pdf2png/No_of_times_the_tool_has_succeeded_to_return_a_model-1.png" alt="Number of successful runs" style="width:750px;"/>
<figcaption> Number of successful runs</figcaption>
</figure>

<figure>
<img src="https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBench/67991ef92774380b30d7ccdd8ad68eec2c6a44a0/docs/data/pdf2png/box_plot_240%20Min-1.png" alt="Performance of the final pipeline per AutoML framework for 240 minutes" style="width:750px;"/>
<figcaption>Performance of the final pipeline per AutoML framework for 240 minutes</figcaption>
</figure>

## Tools Performance Summary

![all1](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/all/001SuccessRateAll.png?token=ABVXF3UEUELS3V2WHMHMCNC6PSP5K)
![all2](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/all/002BestPerformanceAll.png?token=ABVXF3UWZPF5WZFEZY3XKU26PSQOM)
![all3](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/all/003WorstPerformanceAll.png?token=ABVXF3WSYE3I67I2ZZRELTC6PSQSI)
![all4](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/all/004BestTimeBudgetsAll.png?token=ABVXF3QRTGWNGPSMCMF2G5S6PSQV2)


### Impact of Time Budget
#### Impact of Time Budget AutoSKLearn
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

#### Impact of Time Budget TPOT
![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_TPOT_(30_Min-10_Min)%20-%20Copy-1.png?token=ABVXF3UEV3S5FO4PIVV7AAC6QPHRM)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_TPOT_(60_Min-10_Min)%20-%20Copy-1.png?token=ABVXF3WHE3LOGICBU5CJGF26QPHWM)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_TPOT_(4_Hours-10_Min)%20-%20Copy-1.png?token=ABVXF3SFIIQPECR4B73FAF26QPHXM)


![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_TPOT_(4_Hours-30_Min)%20-%20Copy-1.png?token=ABVXF3XRUHOTWWXSNJ4XHCC6QPHZY)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_TPOT_(4_Hours-60_Min)%20-%20Copy-1.png?token=ABVXF3UGZM4SMATME3Z4VRS6QPH2O)
#### Impact of Time Budget ATM

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_ATM_(30_Min-10_Min)-1.png?token=ABVXF3VOA74AOB4GCLXCVH26QPJNM)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_ATM_(60_Min-10_Min)-1.png?token=ABVXF3VAMZAMXYJVA7YYPVK6QPJPA)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_ATM_(4_Hours-10_Min)-1.png?token=ABVXF3UUGYA3U4GVF5KH7MK6QPJR6)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_ATM_(60_Min-30_Min)-1.png?token=ABVXF3UAI2FWAX6TMVNMQDS6QPJQK)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_ATM_(4_Hours-30_Min)-1.png?token=ABVXF3VNNIOEAYBXHTMSHIC6QPJT6)

![time](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLBenchmarking/master/docs/data/pdf2png/Effect_of_time_budget_Increasing_for_ATM_(4_Hours-60_Min)-1.png?token=ABVXF3S3NA3LLD6YUHBF2PK6QPJV6)

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

### Impact of Search Space
![size](https://raw.githubusercontent.com/DataSystemsGroupUT/AutoMLMicroAnalysis/master/docs/data/Accuracyfcand3cfor30minutes.png)

