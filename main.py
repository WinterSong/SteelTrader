#!/usr/bin/python
# Author: CodePothunter
# Date:   2016-04-30


from utils import reader
from utils import lstm
import numpy as np

file1 = "data/new_gz/TK_IH1609[s20160401 00093000_e20160428 00153000]20160429_1032.csv"
file2 = "data/new_gz/TK_IC1604[s20160401 00093000_e20160428 00153000]20160429_1033.csv"



conf = {
    'filename':file2,
    'nb_epoch':10000,
    'batch_size':5,
    'maxlen': 1,
    'sample_size':10000,
    'context_size':0,
    'input_dim':32,
    'hidden_size': 100,
    'learning_rate':0.05,
    'scale': 1
}

print "Begin to load data"
reader = reader(conf)
reader.get_data()
# reader.padding()
features = reader.features
targets = reader.targets
print "Load data complete"

print "Begin to build Networks"
network = lstm(conf)
network.build_net()
print "Build Networks complete"
print  network.fit(features, targets)
# network.draw("model.png")



# #####TEST#####

# a = np.ones((20,27))
# b = np.arange(0,20).reshape(20,)
# c = []
# for i in xrange(20):c.append(a[i]*b[i])
# c = np.array(c)

# from keras.models import Sequential
# from keras.layers import LSTM, Activation, Dense, Reshape
# from keras.optimizers import SGD
# # import activations

# model = Sequential()
# model.add(Dense(64, input_dim=784, init='uniform'))
# model.add(Activation('tanh'))
# model.add(Dense(64, init='uniform'))
# model.add(Activation('tanh'))
# model.add(Dense(1, init='uniform'))
# model.add(Activation('tanh'))
# model.compile(optimizer='sgd',
#               loss='mse')

# # generate dummy data
# import numpy as np
# data_1 = -np.random.random((500, 784))
# data_2 = np.random.random((500, 784))
# labels_1 = np.zeros((500,1))
# labels_2 = np.ones((500,1))
# data = np.concatenate((data_1,data_2),axis=0)
# labels = np.concatenate((labels_1,labels_2))



# # train the model, iterating on the data in batches
# # of 32 samples
# model.fit(data, labels, nb_epoch=100, batch_size=32)
# print model.predict_on_batch(np.array([data[0]]))
# print model.predict_on_batch(np.array([data[501]]))
