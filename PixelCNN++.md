# Paper

* **Title**: PixelCNN++: A PixelCNN Implementation with Discretized Logistic Mixture Likelihood and Other Modifications
* **Authors**: Tim Salimans and Andrej Karpathy and Xi Chen and Diederik P. Kingma and Yaroslav Bulatov
* **Link**: https://openreview.net/pdf?id=BJrFC6ceg
* **Tags**: Neural Network,
* **Year**: 2017
* **Cited by**: 4

# Summary

* What
    * OpenAI implenment pixelCNN with some modifications.
    * 1) Use dicretized logistic mixture likelihood on the pixel rather than a 256-way softmax
    * 2) Condition on whole pixels, rather than R/G/B sub-pixels
    * 3) Use downsampling for multiple resolution
    * 4) Short-cut connections to speed up optimization
    * 5) Dropout for regularization
    
* How
    * 256-way softmax is independent with each other, so the model doesn't know 128 is close to 127 and 129; And also it need
    a lot of memory. So at here they assume there is a continuous distribution for the color intensity, which can be 
    thought as mixture likelihood of logistic. The pixel distribution of CIFAR-10 is like this:
    ![continuous](images/continuous.png)  
    And we factorize the distribution like this:
    <img src="images/distribution.png" width="636" height="125" />

    The authors claims that only small number of mixture components, like 5, is needed for the model.
