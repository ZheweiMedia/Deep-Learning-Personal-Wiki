# Paper

* **Title**: Multi-scale context aggregation by dilated convolutions
* **Authors**: Fisher Yu, Vladlen Koltun
* **Link**: https://arxiv.org/abs/1511.07122
* **Tags**: Neural Network,
* **Year**: 2015
* **Cited by**: 196
* **Conference**: ICLR2016

# Summary

* What
    * Convolutional network performs well in classification. But for dense prediction
    like semantic segmentation, we don't know which property of vanilla CNN is needed.
    * Semantic segmentation needs pixel-level accuracy, and at the same time
    needs multi-scale contextual information. Recently people use two methods to achieve
    the original resolution and catch the multi-scale information. The first one is
    repeated up-convolutions, which rises a quesation that does pooling is needed. The other one
    is set multi-scaled images as inputs, which is not known if necessary.
    * This paper presents a convolutional network module which use dilated convolutions
    to systematically aggregate multiscale contextual information
    without losing resolution.

* How
    * Dilated convolution.
    * ![dilate](/images/dilation.gif)
    * By setting stride = 1 and corresponding padding, we can achieve the same size output of convolutional layers without
    using pooling.
    * Multi-scale context aggregation. Basically it means set different dilation
    factors to different layers.
    * ![multiscale](/images/multiscaledilatedcnn.png)
    * Random initialization if not effective for context module. In the paper
    the authors use identity initialization, which means set the corresponding weight as 1 for the
    same index of input feature map and output map. It's like pass the input directly
    to the output. But backpropagation still can update the weights.
    
  
* Experiments
    * ![results](/images/resultsofdilatedCNN.png)
    * ![improveothers](/images/improveothers.png)
    * We can see dilated convolution as a convolutional module can
    integrated to other models and improve these models.
