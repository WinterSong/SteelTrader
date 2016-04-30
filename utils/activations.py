# Author: CodePothunter
# Date  : 2016-04-30

class Linear(object):
    def __init__(self, scale=1, bais=0):
        self.scale = scale
        self.bais = bais
    def linear(self, x):
        return x*self.scale+self.bais