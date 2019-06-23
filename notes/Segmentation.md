### FCN

- 将端到端的全卷积网络推广到语义分割中
- 重新将预训练好的Imagenet网络用于分割问题中
- 使用反卷积层进行上采样，第一层：padding=100
- 提出了跳跃连接来改善上采样的粗糙程度:   FCN-32s FCN-16s FCN-8s

### UNet

- Encoder-Decoder 结构
- Skip-connection:得到更好的分割结果
- 不同的backbone的改进

### PANet

- **bottom-up augmentation** : 通过融合FPN高低层特征提升目标检测的效果 
- **adaptive feature poolng** : RPN在不同预测特征层上得到的多个ROI经过ROIAlign与全连接层后，对输出的所有的特征进行融合后再进行分类和回归
- **fully-connected fusion **: 在Mask支路上增加一条包含2个3x3卷积的分支以及一个全连接层，后reshape得到与上面支路相同的前背景mask，维度为**28 x 28 x K**（类别数），即增加的支路生成关于每个像素的前背景分类，最后将两部分特征融合进行预测，得到了更加精确分割结果

### DeepLabV1

- 使用了空洞卷积
- 提出了atrous spatial pyramid pooling(ASPP)
- 使用了 Fully connected CRF

### DeepLabV2

- 采用ASPP，在多尺度下获得更好的分割效果
- 采用ResNet结构

### DeepLabV3

- 改进了ASPP模块，纵式结构中加入了1x1conv(dilation rate value is close to the feature map)和global avg pool(image-level feature)，加入BN
- 参考了HDC的思想，block中(1, 2, 4)，ASPP中(6,12,18)，避免gridding效应

### DeepLabV3+

- 设计基于v3的decode module
- 以modifiy xception做backbone，一是Middle flow由8次变为重复16次(more layers)，二是将池化层替换为步长为2的分组卷积，三是加入了BN+ReLU
