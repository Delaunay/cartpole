import torch.nn as nn

class Model(nn.Module):
    """Very basic multiple layer neural network"""

    def __init__(self, input_size, outputs):
        super(Model, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(input_size, input_size * 2, bias=True),
            nn.ReLU(),
            nn.Linear(input_size * 2, outputs, bias=True),
            nn.Softmax(dim=1)
        )

    def forward(self, x):
        return self.model(x)
