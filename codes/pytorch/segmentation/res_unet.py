import torchvision
import torch.nn as nn

resnet = torchvision.models.resnet50(pretrained=True)


class ConvBlock(nn.Module):
    """
    Conv -> BN -> ReLU

    """
    def __init__(self, in_planes, out_planes, kernel_size=3, stride=1, padding=1, with_nonlinearity=True):
        super(ConvBlock, self).__init__()
        self.conv = nn.Conv2d(in_planes, out_planes, kernel_size=kernel_size, stride=stride, padding=padding)
        self.bn = nn.BatchNorm2d(out_planes)
        self.relu = nn.ReLU()
        self.with_nonlinearity = with_nonlinearity

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        if self.with_nonlinearity:
            x = self.relu(x)
        return x

class UpBlock
    nn.ModuleList