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
        self.sample_size = conf.get('sample_size', -1)
        self.cntxwnd = conf['context_size']
        self.scale = conf['scale']
        self.interval = conf['interval']
        self.features = []
        self.targets = []

    def get_data(self):
        read_in = pandas.read_csv(self.file)
        # for i in xrange(len(read_in)):
        if self.sample_size == -1:
            self.sample_size = len(read_in['LastPrice']) - 35
        for i in xrange(34, self.sample_size+34): 
            feature = []
            for key in read_in.columns.values[4:]:
                feature.append(float(read_in[key][i]))
            target = [float(read_in['LastPrice'][i+1])/self.scale]
            # target[int(float(read_in['LastPrice'][i+1]) > float(read_in['LastPrice'][i]))]=1
            self.features.append(feature)
            self.targets.append(target)
        return self.sample_size

    def save_data(self):
        print "Saving data to file"
        np.save("data/features", np.array(self.features))
        np.save("data/targets", np.array(self.targets))
        print "data saved"
    def load_data(self):
        print "Loading data from file"
        self.features = np.load("data/features.npy").tolist()
        self.targets = np.load("data/targets.npy").tolist()
        self.sample_size = len(self.features)
        print "data loaded"
    def padding(self):
        # print len(self.features), len(self.targets)
        print len(self.features), self.sample_size
        features = []
        empty = [0]*32
        self.features = [empty] * self.cntxwnd + self.features + [empty] * self.cntxwnd
        print "dimension: ", len(self.features[0])
        print len(self.features), len(self.targets)
        for i in xrange(self.cntxwnd, self.cntxwnd + self.sample_size):
            feature = []
            for j in xrange(self.cntxwnd, 0, -1):
                feature += self.features[i - j]
            for j in xrange(0, self.cntxwnd + 1, 1):
                try:
                    feature += self.features[i + j]
                except Exception as e:
                    print i + j
                    print e
                    exit()
            features.append(feature)

        self.features = []
        targets = self.targets[:]
        self.targets = []
        for i in xrange(0, self.sample_size, self.maxlen):
            self.features.append(features[i:i+self.maxlen])
            self.targets.append(targets[i:i+self.maxlen])

        self.sample_size = len(self.features)-1-(len(self.features)-1)%(self.interval * self.maxlen)
        # print len(self.features), len(self.targets)
        # print "sample_size:"self.sample_size
        features = self.features[:self.sample_size]
        targets = self.targets[:self.sample_size]
        self.features = []
        self.targets = []
        for i in xrange(0, self.sample_size, self.interval):
            self.features.append([features[i: i+self.interval]])
            self.targets.append(targets[i+self.interval-1])
        self.features = [x[0] for x in self.features]
        print "Number of batches: ", len(self.features), len(self.targets)



        
        
