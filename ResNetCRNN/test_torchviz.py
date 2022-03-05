import torch
from torchviz import make_dot

class MLP(torch.nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.linearl = torch.nn.Linear(3, 5)
        self.relu = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(5, 2)

    def forward(self, x):
        x = self.linearl(x)
        x = self.relu(x)
        x = self.linear2(x)

        return x

model = MLP()
x = torch.randn(8, 3)
y = model(x)
vise=make_dot(y, params=dict(model.named_parameters()))
vise.view()