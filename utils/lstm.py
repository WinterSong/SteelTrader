# Author: CodePothunter
# Date  : 2016-04-30

from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense, Reshape,TimeDistributed
from keras.optimizers import SGD
from keras.layers.core import Dropout
from keras.utils.visualize_util import plot
import activations
import numpy as np
import math

class lstm(object):
    """Implement a lstm box for input and output"""
    def __init__(self, args):
        self.maxlen = args['maxlen']
        self.sample_size = args['sample_size']
        self.input_dim = args['input_dim']
        self.batch_size = args.get('batch_size', 10)
        self.nb_epoch = args.get('nb_epoch', 1000)
        self.layers = args.get('layers', 1)
        self.hidden_size = args.get('hidden_size', 10)
        self.learning_rate = args.get('learning_rate', 0.05)
        self.scale = args.get("scale", 1000)
    def build_net(self):
        self.model = Sequential()
        self.model.add(LSTM(output_dim = 26,init='uniform', 
                            input_shape=(self.maxlen, self.input_dim),
                            return_sequences=True))
        #========================================================
        # self.model.add(Dropout(0.3))
        # self.model.add(LSTM(
        #     output_dim=26, activation='tanh',input_dim=26,
        #     return_sequences=True
        #     ))
        # self.model.add(Dropout(0.3))
        # self.model.add(LSTM(
        #     output_dim=26, activation='tanh',input_dim=26,
        #     return_sequences=True
        #     ))
        #========================================================
        #print self.model.output_shape
        self.model.add(TimeDistributed(Dense(output_dim=4)))
        #print self.model.output_shape
        self.model.add(Activation('softmax'))
        #print self.model.output_shape
        self.model.compile(loss='categorical_crossentropy', 
            optimizer = 'adam',)
            #metrics=['accuracy'])

    def draw(self,save_pic):
        plot(self.model, to_file=save_pic)


    def fit(self, x, y):
        cnt = 0
        x_ = []
        y_ = []

        #print np.array(x).shape
        for i in xrange(0, len(x), self.maxlen):
            x_.append(x[i:i+self.maxlen])
            y_.append(y[i:i+self.maxlen])

        # print np.array(x_).shape
        # # self.model.fit(x_,y_, nb_epoch=self.nb_epoch)
        # print np.array(x).shape, np.array(y).shape
        # assert(self.maxlen <= len(x))
        file_log = open('log.txt','w')
        while cnt < self.nb_epoch:
            hit = 0
            self.model.fit(x_, y_, batch_size=self.batch_size, nb_epoch=1,show_accuracy=False)
            pred_ = self.model.predict(x_)
                # print score_, pred_
            for i in xrange(len(pred_)):
                for j in xrange(len(pred_[i])):
                    # print pred_[i][j], np.argmax(y_[i][j]), np.argmax(pred_[i][j])
                    if y_[i][j][np.argmax(pred_[i][j])]  == 1:
                        hit += 1.0
            file_log.write(str(hit/self.sample_size)+'\n')
            # print "Epoch {0}, accuracy is {1}".format(cnt, hit / self.sample_size )
            cnt += 1
        file_log.close()
        return 0

    def test(self, x, y, xr, yr):
        cnt = 0
        x_ = []
        y_ = []
        xr_ = []
        yr_ = []
        #print np.array(x).shape
        for i in xrange(0, len(x), self.maxlen):
            x_.append(x[i:i+self.maxlen])
            y_.append(y[i:i+self.maxlen])
        for i in xrange(0, len(xr), self.maxlen):
            xr_.append(xr[i:i+self.maxlen])
            yr_.append(yr[i:i+self.maxlen])

        total = len(xr)
        # print np.array(x_).shape
        # # self.model.fit(x_,y_, nb_epoch=self.nb_epoch)
        # print np.array(x).shape, np.array(y).shape
        # assert(self.maxlen <= len(x))
        file_log = open('log2.txt','w')
        while cnt < self.nb_epoch:
            hit = 0
            self.model.fit(x_, y_, batch_size=self.batch_size, nb_epoch=1,show_accuracy=False)
            pred_ = self.model.predict(xr_)
                # print score_, pred_
            for i in xrange(len(pred_)):
                for j in xrange(len(pred_[i])):
                    # print pred_[i][j], np.argmax(y_[i][j]), np.argmax(pred_[i][j])
                    if yr_[i][j][np.argmax(pred_[i][j])]  == 1:
                        hit += 1.0
            file_log.write(str(hit/total)+'\n')
            # print "Epoch {0}, accuracy is {1}".format(cnt, hit / self.sample_size )
            cnt += 1
        file_log.close()
        return 0




if __name__ == '__main__':
    args = {
        'layers':1,
        'input_dim':10,
        'hidden_size': 10,
        'scale':1000
    }
    a = lstm(args)
    a.build_net()

def get(file):
    df = pd.read_csv(file)
    mode = df['Mode']
    res = 0
    res0 = 0
    for item in mode:
        res += 1
        if item == 0:
            res0+=1
    return float(res0)/res