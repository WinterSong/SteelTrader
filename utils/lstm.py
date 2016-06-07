# Author: CodePothunter
# Date  : 2016-04-30

import time
from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense, Reshape, Merge
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
        self.interval = args['interval']

        self.batch_size = args.get('batch_size', 10)
        self.nb_epoch = args.get('nb_epoch', 1000)
        self.layers = args.get('layers', 1)
        self.hidden_size = args.get('hidden_size', 10)
        self.learning_rate = args.get('learning_rate', 0.05)
        self.scale = args.get("scale", 10000)
    def build_net(self):
        self.model = Sequential()
        merge_list = []
        for i in xrange(self.interval):
            tmp_model = Sequential()
            tmp_model.add(Reshape((1, self.input_dim), input_shape=(self.input_dim,)))
            tmp_model.add(LSTM(output_dim = 100,init='uniform'))
            tmp_model.add(Dense(10))
            tmp_model.add(Activation('relu'))
            merge_list.append(tmp_model)
        self.model.add(Merge(merge_list, mode='concat'))
        self.model.add(Dense(100, activation="tanh"))
        self.model.add(Dense(1, init='uniform'))
        self.model.add(Activation('tanh'))
        self.model.compile(loss='mse', optimizer = SGD(lr=self.learning_rate, decay=1e-6, momentum=0.9, nesterov=True))

    def draw(self,save_pic):
        plot(self.model, to_file=save_pic)


    def fit(self, x, y):
        cnt = 0
        assert(self.maxlen <= len(x))
        loss = 0
        while cnt < self.nb_epoch:
            score = 0
            t_beg = time.time()
            cntt = 0
            for i in xrange(len(x)):
                x_ = [np.array(sb) for sb in x[i]]
                y_ = np.array(y[i])
                score_ = self.model.train_on_batch(x_, y_)
                loss_ = 0
                pred_ = self.model.predict_on_batch(x_)
                # print pred_, y_

                for j in xrange(len(pred_)):
                    # print pred_[j], y_[j]
                    loss_ += math.fabs(pred_[j]-y_[j])*self.scale
                score += score_
                loss += loss_
                cntt += 1
            score /= cntt
            loss /= cntt
            t_end = time.time()
            print "Epoch {0}, score is {1},loss is {2}, elapse {3:.4f} seconds".format(cnt, score, loss, t_end- t_beg )
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
