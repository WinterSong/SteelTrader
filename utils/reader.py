# Author: CodePothunter
# Date  : 2016-04-30


import pandas
import sys


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

    def get_data(self):
        read_in = pandas.read_csv(self.file)
        # for i in xrange(len(read_in)):
        for i in xrange(34, self.sample_size+34): 
            feature = []
            for key in read_in.columns.values[4:]:
                feature.append(float(read_in[key][i]))
            target = [0,0]
            target[int(float(read_in['LastPrice'][i+1]) > float(read_in['LastPrice'][i]))]=1
            self.features.append(feature)
            self.targets.append(target)

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



        
        
