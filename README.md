# 期货价格预测器

这部分内容在branch hi-LSTM中
## 使用指南

### 网络结构：

![如图所示](https://github.com/CodePothunter/SteelTrader/blob/hi-lstm/model.png)

由10(self.interval)个LSTM层拼接到一起，再输入到一个LSTM层中，其中每一个LSTM输入长度60(self.maxlen)**期货信息**序列，每个**期货信息**由32(self.input_dim)个特征组成。

网络的输出是一个值，这个值是10\*60(self.interval \* self.maxlen)个时刻的**期货信息**累积的结果，预测的是经过这么多个时刻，期货的价格应该是多少。

### 代码

注意main函数，第一次运行的时候务必确保根目录下有data文件夹，并且保证`get_data()`和`save_data()`处于**未注释**状态，因为它需要运行一次，从`.csv`中提取数据，保存成`.npy`格式，这样能提高以后调试的速度。以后再运行的话可以将`get_data()`和`save_data()`注释掉。
