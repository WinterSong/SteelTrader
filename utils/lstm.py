# Author: CodePothunter
# Date  : 2016-04-30

from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense, Reshape
from keras.optimizers import SGD
from keras.utils.visualize_util import plot
import activations
import numpy as np
import math

class lstm(object):
    """Implement a lstm box for input and output"""
    def __init__(self, args):
        self.maxlen = args['maxlen']
        self.input_dim = args['input_dim']

        self.batch_size = args.get('batch_size', 10)
        self.nb_epoch = args.get('nb_epoch', 1000)
        self.layers = args.get('layers', 1)
        self.hidden_size = args.get('hidden_size', 10)
        self.learning_rate = args.get('learning_rate', 0.05)
        self.scale = args.get("scale", 1000)
    def build_net(self):
        self.model = Sequential()
        self.model.add(Reshape((self.input_dim * self.maxlen,),input_shape=(self.maxlen,  self.input_dim )))
        self.model.add(Dense(self.hidden_size,init='uniform'))
        self.model.add(Dense(self.input_dim * self.maxlen,init='uniform'))
        self.model.add(Reshape((self.maxlen, self.input_dim), input_shape=(self.input_dim * self.maxlen, )))
        self.model.add(LSTM(output_dim = 10,init='uniform'))
        self.model.add(Dense(2,init='uniform'))
        self.model.add(Activation('softmax'))
        self.model.compile(loss='binary_crossentropy', optimizer = SGD(lr=self.learning_rate, decay=1e-6, momentum=0.9, nesterov=True))

    def draw(self,save_pic):
        plot(self.model, to_file=save_pic)


    def fit(self, x, y):
        cnt = 0
        assert(self.maxlen <= len(x))
        while cnt < self.nb_epoch:
            cntt = 0
            score = 0
            for i in xrange(self.maxlen, len(x), self.maxlen):
                # print 1
                cntt += 1
                x_ = []
                y_ = []
                for j in xrange(0,self.maxlen): 
                    if i+j >= len(x):
                        break 
                    x_ += [x[i+j]]
                # for j in xrange(0,self.maxlen): y_ += y[i+j]
                y_ = y[i][:len(x_)]
                # print 2
                # print np.array(x_).shape, np.array(y_).shape
                score_ = self.model.train_on_batch(x_, y_)
                pred_ = self.model.predict_on_batch(x_)
                # print score_, pred_

                # for j in xrange(len(pred_)):
                #     print pred_[j], y_[j]
                #     score_ += math.fabs(pred_[j]-y_[j])*self.scale
                # score += score_/len(pred_)
                score += score_
            score /= cntt
            print "Epoch {0}, score is {1}".format(cnt, score)
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
