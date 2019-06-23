# Small object detection

## Augmentation for small object detection

**Problems**

1. There are relatively fewer images that contain small objects in the MS COCO dataset.(sample imbalance)
2. The area covered by small object is mush smaller,implying the lack of diversity in the locations of small object.(We conjecture this makes it difficult for the object detection model to generalize to small objects in the test time when they appear in less explored portions of an image.)
3. Small objects contribute much less to computing the region proposal loss,which biases the entire network to favor large and medium objects.

**Solutions**

1. oversampling those images contain small objects.
2. copy-pasting small objects multiple times.

## LOCO

**Problems**

 The small target may only occupy a very small fraction(30x15 pixels in a 1280x720 pixels image).It have fewer features can be extracted.

**Solutions**

1. The traffic light or sign is usually on the top of a vertical pole or suspended on a horizontal pole. Therefore, the poles become local context information of the traffic signs. 
2. We can extract features from both horizontal and vertical areas surrounding small objects.So we design a local context layer to extract more discriminative native features from the areas around target.

**Pipeline**

- local context layer : vertically and horizontally expands the original ROIs generated from RPNS.So we sent **Rv Rh Ro** to ROI Pooling.Thus we get **Fv Fh Fo**.
- detail : We get 3 x C channel features ,then a C dimension and 1 x 1 size convolution layer to compress the channel size to original size.Finally, we sent the C channels feature to full connection layer for classifying.

- **Conclusion**
  Different from big objects such as humans, vehicle, animal and buildings, the traffic signs only contain a few pixels in the images. Therefore, it is very hard to detect them because of few discriminative features. To solve it, in the proposed framework, a local context layer is designed to automatically extract more discriminative information from the regions around the traffic signs, which can take advan- tage of the local context information to accurately detect the small objects. 

## Small Object Detection in Optical Remote Sensing Images via Modified Faster R-CNN
**Solutions**

1. modify anchors in RPN based on the statistics of training set to generate small object proposals.
2. feature fusion
3. context information
4. a sampling strategy called **random rotation** to solve class imbalance during training.

## Feature selective anchor-free Module

**Motivation**

Let each instance select the best level of feature freely to optimize the network