## Facial landmark detection and Facial alignment

## Facial landmark
1. Holistic Method
	Active Appearance Model(AAM)
    Leverage the holistic facial appearance information as well as the global facial shape patterns.
    During detection,it identifies the landmark locations by fitting the learned appearance and shape models to the testing images.
2. Constrained Local Method
	Based on the global facial shape patterns as well as the independent local appearance information around landmark.
	Local appearance model for likelihood(classificaion-based or regression-based)
    Facial shape pattern constraint applied to the shape model coefficient,as penalty term or probalilistic prior distributions.
    The whole objective function is usually non-convex.
3. Regression-based Method
	Learn the mapping from image appearance to the landmark locations.
	Direct regression methods(local or global)
    Cascaded regression methods(optimizing problem,initial landmark locations)
    Deep learning based methods
## Stacked Dense U-Nets with Dual Transformers for Robust Face Alignment
- Scale Aggregation Topology
	**热图回归的网络拓扑结构需要获取不同尺度的全局和局部信息以及保留分辨率信息**
	U-Net 
    Hourglass
    DLA
    SAT(propose)
- Transformer
  **由于固定的几何结构，U-Net网络结构缺乏变换的建模能力**
  STN
  deformable conv
  data augmentaion by random affine transformation
## Wing loss
- wing loss
  **提高神经网络对小中范围误差的训练效果**
  ![wingloss](https://github.com/JinYAnGHe/Learning_CV/tree/master/images/wingloss.png)
