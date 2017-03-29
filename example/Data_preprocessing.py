# -*- coding:utf8
import pandas as pd
import numpy as np
import cPickle as pickle
import itertools
from collections import OrderedDict
from datetime import datetime
import os
import sys
basepath = os.path.join(os.getcwd(),'..')
dataset_filepath = os.path.join(basepath, "dataset")
train = os.path.join(dataset_filepath,'train.csv')
training = os.path.join(dataset_filepath, 'training.xlsx')
output = os.path.join(dataset_filepath, 'data.p')
File_name = train
data = pd.read_csv(File_name,header=None)
attributes = data.axes[1].tolist()
observations = data[attributes[2]].tolist()[1:19]
def create_xlsx(observation):
	info = [data.ix[row].tolist() for row in xrange(data.shape[0])]
	obs = [row for row in info if row[2] == observation]
	obs = [[i[0]]+i[2:] for i in obs]
	dict_ = {}
	for i in range(len(obs)):
		dict_[datetime.strptime(obs[i][0],'%Y/%m/%d').strftime('%Y/%m/%d')] = obs[i][2:]
		#dict_[obs[i][0]] = obs[i][2:]
	#print OrderedDict(sorted(dict_.items(), key=lambda t: t[0]))
	DataFrame = pd.DataFrame(OrderedDict(sorted(dict_.items(), key=lambda t: t[0]))) # dict to DataFrame
	return DataFrame

def systematic_sampling(data,num): #num = sampling interval# without replacem
	k =len(data)/num
	ini = 0
	result = []
	for i in range(k):
		sample = data[ini:ini+num]
		result.append(sample) 
		#print 'ini',ini
		ini = ini + num
	return result

def sampling(data,interval):
	######################################
	# Data hinting: to get more data
	######################################
	interval = interval
	result = []
	for i,j in enumerate(data):
		#print ls[i:i+2]
		if len(data[i:i+interval])>=interval:
			#print ls[i:i+interval]
			result.append(data[i:i+interval])
	return result

def data_preprocess(obs):
	File_name = training
	Sheet1 = obs
	with pd.ExcelFile(File_name) as xls:
		data = pd.read_excel(xls,Sheet1)
	attributes = data.axes[1]
	N = len(attributes)
	temp = [data[attributes[i]].tolist() for i in range(N)]
	data =[]
	for i in temp:
		data += i
	for i in xrange(12): 
		if i == 0:
			temp = data[i:480]
			result = sampling(temp,8)
		else:
			temp = data[i*480:(i+1)*480]
			result = result + sampling(temp,8)
	return result
def data_preprocess2(raw_data):
	features = []
	y_hat = []
	N = len(raw_data[0])
	for i in xrange(N):
		temp = []
		for obs in observations:
			#print obs
			if obs == 'PM2.5':
				y_hat.append(raw_data[observations.index(obs)][i][-1])		
			if obs != 'RAINFALL':
				#print obs,[x for j,x in enumerate(raw_data[observations.index(obs)][i][:-1]) if j>0 ]
				temp.append([x for j,x in enumerate(raw_data[observations.index(obs)][i][:-1]) ])
				#temp.append(raw_data[observations.index(obs)][i][:-1])
			if obs == 'RAINFALL':
				#print obs,[0.0 if x == 'NR' else float(str(x)) for j,x in enumerate(raw_data[observations.index(obs)][i][:-1]) if j > 0]
				temp.append([0.0 if x == 'NR' else float(str(x)) for j,x in enumerate(raw_data[observations.index(obs)][i][:-1]) ])
				#temp.append([0.0 if x == 'NR' else float(str(x)) for x in raw_data[observations.index(obs)][i][:-1]])
		features.append(list(itertools.chain.from_iterable(temp))) ##pseudo_code : features.append(flatten(temp))
	return features , y_hat
if __name__ == '__main__': 
	####################################
	# Prepocessing data
	####################################
	print observations
	####################################
	#Step1: Create training.xlsx for visualizing data
	####################################
	File_name = training
	writer = pd.ExcelWriter(File_name, engine = 'xlsxwriter')
	for obs in observations:
		Sheet = obs
		create_xlsx(obs).to_excel(writer, sheet_name = Sheet)

	####################################
	#Step2: Establishing a data.p for analyzing data
	####################################
	data = [data_preprocess(obs) for obs in observations]
	f = open(output,'w')
	pickle.dump(data,f)
	f.close()
