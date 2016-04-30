# Author: CodePothunter
# Date  : 2016-04-30

from keras.models import Sequential
from keras.layers import LSTM, Activation, Dense, Reshape
import activations


class lstm(object):
    """Implement a lstm box for input and output"""
    def __init__(self, args):
        self.layers = args['layers']
        self.input_dim = args['input_dim']
        self.scale = args['scale']
        self.hidden_size = args['hidden_size']
        self.model = Sequential()

    def build_net(self):
        self.model.add(Dense(output_dim=self.hidden_size, input_dim=self.input_dim))
        self.model.add(Reshape((1,self.hidden_size), input_shape=(self.input_dim, )))
        self.model.add(LSTM(output_dim = 1))
        linear = activations.Linear(self.scale).linear
        self.model.add(Activation(linear))
        self.model.compile(loss='mean_squared_error', optimizer='sgd')




if __name__ == '__main__':
    args = {
        'layers':1,
        'input_dim':10,
        'hidden_size': 10,
        'scale':1000
    }
    a = lstm(args)
    a.build_net()
