import torch
import torch.nn as nn
x = torch.randn([1, 1024])
print(x.shape)
bn1 = nn.BatchNorm2d(1024)
x = bn1(x)
print(x.shape)