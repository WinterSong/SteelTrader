# 期货价格预测器

这部分内容在branch hi-LSTM中
## 使用指南

网络结构：

![如图所示](https://github.com/CodePothunter/SteelTrader/model.png)

由10(self.interval)个LSTM层拼接到一起，再输入到一个LSTM层中，其中每一个LSTM输入长度60(self.maxlen)**期货信息**序列，每个**期货信息**由32(self.input_dim)个特征组成。

网络的输出是一个值，这个值是10*60(self.interval * self.maxlen)个时刻的**期货信息**累积的结果，预测的是经过这么多个时刻，期货的价格应该是多少。

