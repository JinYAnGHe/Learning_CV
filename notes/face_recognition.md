##Face Recognition
###ArcFace
- Motivation
**Embedding Target**
Intra-class Compactness + Inter-class Discrepancy
**Triplet-Loss**
"Margin" is useful
Image2image 转换到 Image2class comparsion
问题是online class feature embedding is not efficient
**Softmax-Loss**
Image2class
问题是不存在Margin，类别多时W矩阵很大
- Method
1.X and W Normalization
2.Additive Angular Margin
###RetinaFace
- Singe-stage on feature pyramid
- Context Moudle:刚性和非刚性建模
- Multitask loss：
  extra-supervision(facial landmark regression)
  self-supervision