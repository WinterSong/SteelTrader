# Author: CodePothunter
# Date  : 2016-04-30

class Linear(object):
    def __init__(self, scale):
        self.scale = scale
    def linear(self, x):
        return x*self.scale