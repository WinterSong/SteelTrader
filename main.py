#!/usr/bin/python
# Author: CodePothunter
# Date:   2016-04-30


from utils import reader
from utils import lstm

file1 = "data\TK_IH1609[s20160401_00093000_e20160428 00153000]20160429_1032.csv"



conf = {
    'filename':file1,
    'maxlen':20,
    'sample_size':100,
    'context_size':5,
    'input_dim':27*11,
    'hidden_size': 100,
    'scale':1000,
    'bais':2000,
    'learning_rate':0.001
}

print "Begin to load data"
reader = reader(conf)
reader.get_data()
reader.padding()
features = reader.features
targets = reader.targets
print "Load data complete"

print "Begin to build Networks"
network = lstm(conf)
network.build_net()
print "Build Networks complete"
print network.fit(features, targets)