# Paper

* **Title**: FlowNet: Learning Optical Flow with Convolutional Networks
* **Authors**: Philipp Fischer, Alexey Dosovitskiy, Eddy Ilg, Philip Häusser, Caner Hazırbaş, Vladimir Golkov, Patrick van der Smagt, Daniel Cremers, Thomas Brox
* **Link**: https://arxiv.org/abs/1504.06852
* **Tags**: Neural Network, flownet
* **Year**: 2015
* **Conference**:ICCV2015
* **Cited by**: 283+116

# Summary

* What
    * CNN for optical flow

* How
    * First method FlownetSimple is directly use CNN to generate optical flow because CNN can learn
    any function. However, we cannot be sure that we can achieve this result by gradient descent.
    * The modified version add a correlation layer. This correlation operation can be done by convolution. After this
    correlation layer the correlation value is generated. Then the correlation value is used for producing
    optical flow.(emmm, why correlation value can produce optical flow?)
    * Refinement. The original optical flow is generated at the lowest level, then the flow is upsampled and
    concatenate with featrue maps (two parts, like U-net) and produce the refined flow. (emm, also a little weired.)
    
  
* Experiments
    
