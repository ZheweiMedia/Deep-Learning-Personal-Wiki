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
    * First method FlowNetSimple is directly use CNN to generate optical flow because CNN can learn
    any function. However, we cannot be sure that we can achieve this result by gradient descent.
    * The modified version add a correlation layer. This correlation operation can be done by convolution. After this
    correlation layer the correlation value is generated. Then the correlation value is used for producing
    optical flow.(emmm, why correlation value can produce optical flow?)
    * Refinement. The original optical flow is generated at the lowest level, then the flow is upsampled and
    concatenate with featrue maps (two parts, like U-net) and produce the refined flow. (emm, also a little weired.)
    
  
* Experiments
    * FlowNetSimple even better than FlowNetC. The authors said that "Since the average endpoint
error often favors over-smoothed solutions."


# Paper

* **Title**: FlowNet 2.0: Evolution of Optical Flow Estimation with Deep Networks
* **Authors**: Eddy Ilg, Nikolaus Mayer, Tonmoy Saikia, Margret Keuper, Alexey Dosovitskiy, Thomas Brox
* **Link**: https://arxiv.org/abs/1612.01925
* **Tags**: Neural Network, flownet
* **Year**: Dec, 2016
* **Conference**:
* **Cited by**: 65

# Summary

* What
    * CNN for optical flow
    * Flownet2.0 based on flownet

* How
    * bootstrap network. The mind of residuel network.
    * First network generate raw optical flow, then applied on the second image, then set the first image and the 
    translated second images as the input for the second network.
    * Translate image with flow by a warping layer.
    * A network for small displacement, which designed with small stride.
    * A network merge all flows together.   
  
* Experiments
    * The author said FlowNetC performs better than FlowNetSimple, which is contrast with the original paper.
    * multiple dataset improves the results.
    
