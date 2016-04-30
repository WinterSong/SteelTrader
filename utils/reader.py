# Author: CodePothunter
# Date  : 2016-04-30


import pandas
import sys

class reader(object):
    """
    Read data from data set file.
    """
    def __init__(self, filename):
        self.file = filename
        self.features = []
        self.targets = []

    def get_data(self):
        read_in = pandas.read_csv(self.file)
        for i in xrange(len(read_in)):
        	feature = []
        	target = 0
        	for key in read_in.columns.values:
        		feature.append(reader[key][i])
    		target = feature[-1]
    		feature = feature[:-1]
    		self.features.append(feature)
    		self.targets.append(target)

    def get_buffer(self):
        pass
        