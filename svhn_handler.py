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

np.set_printoptions(threshold=sys.maxint)

mat_train = scipy.io.loadmat('train_svhn.mat')
mat_test = scipy.io.loadmat('test_svhn.mat')

def convert(pixel):
    return (0.21*pixel[0] + 0.72*pixel[1] + 0.07*pixel[2]) / 255

train_dat = mat_train.get('X')
train_labels = mat_train.get('y')
test_dat = mat_test.get('X')
test_labels = mat_test.get('y')

train = np.array(train_dat)
labels_tr = np.hstack(np.array(train_labels))
test = np.array(test_dat)
labels_ts = np.hstack(np.array(test_labels))

train_n1 = np.transpose(train)
test_n1 = np.transpose(test)

train_dump = []
test_dump = []

for i in xrange(73257):
    if labels_tr[i] == 10:
        labels_tr[i] = 0
        
for i in xrange(26032):
    if labels_ts[i] == 10:
        labels_ts[i] = 0

for i in xrange(73257):
    train_n2 = []
    for j in xrange(32):
        train_n3 = []
        for k in xrange(32):
            foo = np.transpose(train_n1[i])[j][k]
            bar = convert(foo)
            train_n3.append(bar)
        train_n2.append(train_n3)
        dump = np.array(train_n2).flatten()
    train_dump.append(dump)
    
for i in xrange(26032):
    test_n2 = []
    for j in xrange(32):
        test_n3 = []
        for k in xrange(32):
            foos = np.transpose(test_n1[i])[j][k]
            bars = convert(foos)
            test_n3.append(bars)
        test_n2.append(test_n3)
        dumps = np.array(test_n2).flatten()
    test_dump.append(dumps)

data_tr = np.array(train_dump)
data_ts = np.array(test_dump)

train_set = data_tr, labels_tr
test_set = data_ts, labels_ts

#dataset = [train_set, test_set]
#f = gzip.open('svhn.pkl','wb')
#cPickle.dump(dataset, f)
#f.close()

print data_tr.shape, data_ts.shape
