# -*- coding:utf8
import pandas as pd
import numpy as np
import cPickle as pickle
import itertools
from Data_preprocessing import systematic_sampling
from Data_preprocessing import data_preprocess2
from sklearn.linear_model import Ridge
from sklearn import linear_model
from sklearn import preprocessing
import random
import os
import sys
basepath = os.path.join(os.getcwd(),'..')
dataset_filepath = os.path.join(basepath, "dataset")
test = os.path.join(dataset_filepath,'test_X.csv')
submit = os.path.join(dataset_filepath,'submit.csv')
input_ = os.path.join(dataset_filepath, 'data.p')
####################################
#Prepare some data
####################################
f = open(input_,'r')
data = pickle.load(f)
f.close()
N = len(data[0])
AvgErr= []
overfitting = []
V_vold = 10
####################################
#V-vold validation 
####################################
for z in xrange(V_vold):
	feature , label = data_preprocess2(data)
	feature = preprocessing.scale(feature)
	temp = list(zip(feature,label))
	random.shuffle(temp) #### randomtest set則是從豐原站剩下的資料中取樣出來。
	feature , label = zip(*temp)
	feature = list(feature)
	label = list(label)
	X_train = feature[: int(N*0.9)]
	X_val = feature[int(N*0.9):]
	Y_train = label[: int(N*0.9)]
	Y_val = label[int(N*0.9):]
	reg = linear_model.RidgeCV(alphas=[10**i for i in xrange(-10,10)])
	reg.fit(X_train,Y_train)
	clf = Ridge(alpha = reg.alpha_,solver='cholesky') #1000 # why we can't use close form
	clf.fit(X_train,Y_train)
	predict = [i for i in clf.predict(X_train)]
	train_error = 1.0 * sum([(i-j)**2 for i,j in zip(Y_train,predict)])/ len(predict)
	predict = [i for i in clf.predict(X_val)]
	val_error = 1.0 * sum([(i-j)**2 for i,j in zip(Y_val,predict)])/ len(predict)
	AvgErr.append(val_error)
print 'AvgErr', sum(AvgErr)/len(AvgErr)
# f = open('record.txt','w')
# f.write(str(sum(AvgErr)/len(AvgErr)))
# f.close()
####################################
#Training 
####################################
feature , label = data_preprocess2(data)
scaler = preprocessing.StandardScaler().fit(feature)
feature = scaler.transform(feature)
######################################
# Testing
######################################
####################################
#Part1: Testing Data
#################################### 
File_name = test
data = pd.read_csv(File_name,header=None)
attributes = data.axes[1].tolist()
test = [data.ix[row].tolist() for row in xrange(data.shape[0])]
test = [[float(value) for value in row[4:]] if row[1] != 'RAINFALL' else [0.0 if value == 'NR' else float(str(value)) for value in row[4:]] for row in test]
#print test
#test = [[float(value) for value in row[2:]] for row in test if row[1] != 'RAINFALL']
####################################
#Part2: feature scaling Testing Data
#################################### 
X_test = [list(itertools.chain.from_iterable(i)) for i in systematic_sampling(test,18)]
X_test = scaler.transform(X_test)
predict = [i for i in clf.predict(X_test)]
######################################
# Submission
######################################
Submission = pd.DataFrame({'value':predict,
							'id': ['id_%i'%i for i in xrange(len(predict))]				}
							)
Submission.to_csv(submit,index = False)