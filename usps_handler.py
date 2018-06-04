# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:38:22 2015

@author: hiyu
"""

from __future__ import division
import gzip, cPickle
import sys
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#np.set_printoptions(threshold=sys.maxint)

mat_data = scipy.io.loadmat('usps_resampled.mat')

train_patterns = mat_data.get('train_patterns')
train_label = mat_data.get('train_labels')

test_patterns = mat_data.get('test_patterns')
test_label = mat_data.get('test_labels')

train_data = np.transpose((np.array(train_patterns)+1)/2)
train_dump = np.array(train_label)
train_labels = np.argmax(train_dump, axis=0)

test_data = np.transpose((np.array(test_patterns)+1)/2)
test_dump = np.array(test_label)
test_labels = np.argmax(test_dump, axis=0)

train_set = train_data, train_labels
test_set = test_data, test_labels

dataset = [train_set, test_set]
cupf = gzip.open('usps.pkl','wb')
cPickle.dump(dataset, f)
f.close()