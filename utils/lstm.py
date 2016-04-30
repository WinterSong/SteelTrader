# Author: CodePothunter
# Date  : 2016-04-30

from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense, Reshape, Convolution1D, MaxPooling1D
from keras.optimizers import SGD
from keras.preprocessing import sequence
import activations


class lstm(object):
    """Implement a lstm box for input and output"""
    def __init__(self, args):
        self.maxlen = args['maxlen']
        self.input_dim = args['input_dim']
        self.scale = args['scale']
        self.bais = args['bais']
        
        self.batch_size = args.get('batch_size', 10)
        self.nb_epoch = args.get('nb_epoch', 100000)
        self.layers = args.get('layers', 1)
        self.hidden_size = args.get('hidden_size', 10)
        self.learning_rate = args.get('learning_rate', 0.05)

    def build_net(self):
        self.model = Sequential()
        self.model.add(LSTM(output_dim = 1, input_shape=(self.input_dim, self.maxlen)))
        linear = activations.Linear(self.scale, self.bais).linear
        self.model.add(Activation(linear))
        self.model.compile(loss='mean_squared_error', optimizer=SGD(lr=self.learning_rate, momentum=0.0, decay=0.0))

    def fit(self, x, y):
        cnt = 0
        while True:
            for i in xrange(self.batch_size,len(x), self.batch_size):
                x_ = x[i-self.batch_size:i]
                y_ = y[i-self.batch_size:i]
                score_ = self.model.train_on_batch(x_, y_)
                pred_ = self.model.predict_on_batch(x_)
                for j in xrange(len(pred_)):
                    print pred_[j], y_[j]
                print "Epoch {0}, score is {1}".format(cnt, score_)
        # self.model.fit(x,y,batch_size=self.batch_size, nb_epoch=self.nb_epoch)
        score = self.model.evaluate(x,y,batch_size=self.batch_size)
        return score




if __name__ == '__main__':
    args = {
        'layers':1,
        'input_dim':10,
        'hidden_size': 10,
        'scale':1000
    }
    a = lstm(args)
    a.build_net()
