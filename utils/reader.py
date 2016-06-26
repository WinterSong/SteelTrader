# Author: CodePothunter
# Date  : 2016-04-30


import pandas
import sys
import numpy as np

class reader(object):
    """
    Read data from data set file.
    """
    def __init__(self, conf):
        self.file = conf['filename']
        self.maxlen = conf['maxlen']
        self.sample_size = conf['sample_size']
        self.cntxwnd = conf['context_size']
        self.scale = conf['scale']
        self.features = []
        self.targets = []
        self.testset = []
        self.testtar = []

    def get_data(self):
        read_in = pandas.read_csv(self.file)
        for item in read_in['Mode'][34:self.sample_size+34]:
            if item==0:
                self.targets.append([1,0,0,0])
            elif item ==1:
                self.targets.append([0,1,0,0])
            elif item ==2:
                self.targets.append([0,0,1,0])
            else:
                self.targets.append([0,0,0,1])
        for item in read_in['Mode'][self.sample_size+34:self.sample_size+1034]:
            if item==0:
                self.testtar.append([1,0,0,0])
            elif item ==1:
                self.testtar.append([0,1,0,0])
            elif item ==2:
                self.testtar.append([0,0,1,0])
            else:
                self.testtar.append([0,0,0,1])
        #self.targets = list(read_in['Mode'])[34:]
        # for i in xrange(len(read_in)):
        for i in xrange(34, self.sample_size+34): 
            feature = []
            for ind in [5,7]+range(9,30)+range(33,36):
                key = read_in.columns.values[ind]
                feature.append(float(read_in[key][i]))
            target = [0,0]
            target[int(float(read_in['LastPrice'][i+1]) > float(read_in['LastPrice'][i]))]=1
            self.features.append(feature)
        for i in xrange(self.sample_size+34,self.sample_size+1034): 
            feature = []
            for ind in [5,7]+range(9,30)+range(33,36):
                key = read_in.columns.values[ind]
                feature.append(float(read_in[key][i]))
            target = [0,0]
            target[int(float(read_in['LastPrice'][i+1]) > float(read_in['LastPrice'][i]))]=1
            self.testset.append(feature)
        # print np.array(self.features).shape

    def padding(self):
        # print len(self.features), len(self.targets)
        features = []
        empty = [0]*32
        self.features = [empty] * self.cntxwnd + self.features + [empty] * self.cntxwnd
        print len(self.features[0])
        # print len(self.features), len(self.targets)
        for i in xrange(self.cntxwnd, self.cntxwnd + self.sample_size):
            feature = []
            for j in xrange(self.cntxwnd, 0, -1):
                feature += self.features[i - j]
            for j in xrange(0, self.cntxwnd + 1, 1):
                try:
                    feature += self.features[i + j]
                except:
                    print i+j
            features.append(feature)

        # print len(features), len(targets)
        # self.features = features
        self.features = []
        targets = self.targets[:]
        self.targets = []
        for i in xrange(0, self.sample_size, self.maxlen):
            self.features.append(features[i:i+self.maxlen])
            self.targets.append(targets[i:i+self.maxlen])
            # print self.features
        print len(self.features)



        
        
