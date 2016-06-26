# Author: CodePothunter
# Date  : 2016-04-30

from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense, Reshape,TimeDistributed
from keras.optimizers import SGD
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
        self.model.add(LSTM(output_dim = 100,init='uniform', 
                            input_shape=(self.maxlen, self.input_dim),
                            return_sequences=True))
        print self.model.output_shape
        self.model.add(TimeDistributed(Dense(output_dim=2)))
        print self.model.output_shape
        self.model.add(Activation('softmax'))
        print self.model.output_shape
        self.model.compile(loss='binary_crossentropy', 
            optimizer = 'adam',
            metrics=['accuracy'])

    def draw(self,save_pic):
        plot(self.model, to_file=save_pic)


    def fit(self, x, y):
        cnt = 0
        x_ = []
        y_ = []
        for i in xrange(0, len(x), self.maxlen):
            x_.append(x[i:i+self.maxlen])
            y_.append(y[i:i+self.maxlen])
        if len(x_[-1]) != len(x_[0]):
            x_ = x_[:-1]
            y_ = y_[:-1]
        print np.array(x_).shape
        # # self.model.fit(x_,y_, nb_epoch=self.nb_epoch)
        # print np.array(x).shape, np.array(y).shape
        # assert(self.maxlen <= len(x))
        while cnt < self.nb_epoch:
            hit = 0
            score_ = self.model.fit(x_, y_, nb_epoch=5)
            pred_ = self.model.predict(x_)
                # print score_, pred_
            for i in xrange(len(pred_)):
                for j in xrange(len(pred_[i])):
                    print pred_[i][j], np.argmax(y_[i][j])
                    if y_[i][j][np.argmax(pred_[i][j])]  == 1:
                        hit += 1.0
            print "Epoch {0}, accuracy is {1}".format(cnt, hit / self.sample_size )
            break
            cnt += 1
        return 0

    def test(self, x, y):
        # To Be Continue
        pass




if __name__ == '__main__':
    args = {
        'layers':1,
        'input_dim':10,
        'hidden_size': 10,
        'scale':1000
    }
    a = lstm(args)
    a.build_net()
