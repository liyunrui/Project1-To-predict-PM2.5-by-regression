import os
import sys
basepath = os.path.join(os.getcwd(),'..')
print basepath
dataset_filepath = os.path.join(basepath, "dataset")
train = os.path.join(dataset_filepath,'train.csv')
test = os.path.join(dataset_filepath,'test_X.csv')
print train
print test