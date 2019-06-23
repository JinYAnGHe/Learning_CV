## Model Compression and Acceleration

### ShuffleNetV1

- **Channel Shuffle** for Group convolution : Output from a certain channel are only derived from a small fraction of input channels.Channel shuffle operation allow group convolution to obtain input data from
  different groups.
- Using shuffle unit to replace the residual block.
- **Depthwise separable convolution and pointwise group convolution**

### ShuffleNetV2

**Insight**:Using FLOPS as the only metric for computation complexity is insufficient and could lead to sub-optimal design.

- **MAC**(memory access cost)

1. Equal channel width minimizes MAC
2. Excessive group convolution increase MAC
3. Network fragmentation reduces the degree of parallelism(especially for GPU)
4. Reduce element-wise operation.Element-wise operation bring consumption of time is more than it reflected on FLOPS

- **Modification **

1. Channel split at the beginning of each unit
2. In a branch, three convolutions with same input and output channels
3. 1 x 1 convolution no longer grouped-wise
4. Channel shuffle between two branches

### MobileNet

- Depthwise convolution and pointwise convolution
- Width(channel) multiplier and resolution multiplier for smaller and faster requirement
- Shrinking network by reducing width rather than the number of layers

### MobileNetV2

- **Modification **

1. Linear Bottlenecks : For the representation power of model.The features of high-dimensional space  will not loss information after ReLU function.No ReLU after pointwise convolution.
2. Inverted residuals : Dimension elevation before dimension reduction

### ThunderNet

A lightweight two-stage detector.

- **Motivation**

To eliminate the performance degradation induced by small backbones and small feature maps, we design two efficient architecture blocks CEM and SAM.

- **Insight**

1. the input resolution should match the capability of the backbone
2. A large receptive field can leverage more context information and encode long-range relationship between pixels more efficently
3. Early-stage and late-stage features.Localization is more difficult for classification for large backbones.Weak representation power restricts the accuracy.
4. New backbones SNet

- Context Enhancement Module : Aggregate multi-scale local context and global context information to generate mote discriminative features.
- Spatial Attention Module : Use the knowledge from RPN to re-weight the feature distribution of feature map.It help the training of RPN

## Overview

- **Schemes**

1. parameter pruning and sharing
2. low-rank factorization
3. transferred/compact convolutional filters
4. knowledge distillation