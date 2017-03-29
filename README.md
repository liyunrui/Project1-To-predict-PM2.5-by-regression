Tutorial Project : Regression 
====

**Outline:**

**-Introduction**
**-Problem Description**
**-Dataset**
**-Example**
**-Toolkit**
**-Reference**

Introduction
===
**這是一個練習專案, 專案中會學習到在用Machine Learning來處理生活周邊資料時, 有需要需要注意哪些部分, 能使得機器學習的結果能更好。**

分成三個面向來討論:
1. Data Preprocessing
2. Feature Processing
3. Model & Model Selection

Problem Description
===
**利用從中央氣象局爬下來為期一年的氣象資料, 希望找出資料間的Insight能更準確地預測未來PM2.5得值, 以來幫助氣象局做出更好的污染決策制定。**

Dataset
===
**本次資料使用豐原站的觀測記錄，分成train set跟test set，train set是豐原站每個月的前20天所有資料。test set則是從豐原站剩下的資料中取樣出來。**
- train.csv: 每個月前20天的完整資料

|日期| 觀測值 | 描述 |
|--- |------ | ----------- |
|2014/1/1 | AMB_TEMP   | 包含24小時的觀測值 |
|2014/1/1| CH4 | 包含24小時的觀測值 |
|2014/1/1| CO    |包含24小時的觀測值 |
|2014/1/1| NMHC    | 包含24小時的觀測值 |
|2014/1/1| NO   | 包含24小時的觀測值 |
|2014/1/1| NO2    | 包含24小時的觀測值 |
|2014/1/1| NOx    | 包含24小時的觀測值 |
|2014/1/1| O3   | 包含24小時的觀測值|
|2014/1/1| PM10 | 包含24小時的觀測值 |
|2014/1/1| PM2.5| 包含24小時的觀測值 |
|2014/1/1| RAINFALL | 包含24小時的觀測值 |
|2014/1/1| RH | 包含24小時的觀測值 |
|2014/1/1| SO2 | 包含24小時的觀測值 |
|2014/1/1| THC | 包含24小時的觀測值 |
|2014/1/1| WD_HR | 包含24小時的觀測值|
|2014/1/1| WIND_DIREC | 包含24小時的觀測值|
|2014/1/1| WIND_SPEED | 包含24小時的觀測值|
|2014/1/1| WS_HR | 包含24小時的觀測值|
- test_X.csv: 從每個用剩下10天的資料當中取樣出連續的10小時為一筆，前九小時的所有觀測數據當作feature，第十小時的PM2.5當作answer。一共取出240筆==不重複==的test data，請根據feauure預測這240筆的PM2.5

|id| 觀測值 | 描述 |
|--- |------ | ----------- |
|id0 | AMB_TEMP   | 包含連續9小時的觀測值 |
|id0| CH4 | 包含連續9小時的觀測值 |
|id0| CO    |包含連續9小時的觀測值 |
|id0| NMHC    | 包含連續9小時的觀測值 |
|id0| NO   | 包含連續9小時的觀測值 |
|id0| NO2    | 包含連續9小時的觀測值 |
|id0| NOx    | 包含連續9小時的觀測值 |
|id0| O3   | 包含連續9小時的觀測值|
|id0| PM10 | 包含連續9小時的觀測值 |
|id0| PM2.5| 包含連續9小時的觀測值 |
|id0| RAINFALL | 包含連續9小時的觀測值 |
|id0| RH | 包含連續9小時的觀測值 |
|id0| SO2 | 包含連續9小時的觀測值 |
|id0| THC | 包含連續9小時的觀測值 |
|id0| WD_HR | 包含連續9小時的觀測值|
|id0| WIND_DIREC | 包含連續9小時的觀測值|
|id0| WIND_SPEED | 包含連續9小時的觀測值|
|id0| WS_HR | 包含連續9小時的觀測值|

- submit.csv:預測結果

資料來源：https://inclass.kaggle.com/c/ml2017-hw1-pm2-5

Example
===
- Data_preprocessing.py
- model.py

Toolkit
===
**python 2.7.6**
**scikit learnn 0.18.1**

Reference
===



