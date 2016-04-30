#!/usr/bin/python
# Author: CodePothunter
# Date:   2016-04-30


from utils import reader

file1 = "data\TK_IH1609[s20160401_00093000_e20160428 00153000]20160429_1032.csv"

reader = reader(file1)
reader.get_data()
features = raeder.features
targets = reader.targets
conf = {
    'input_dim':10,
    'hidden_size': 10,
    'scale':1000
}