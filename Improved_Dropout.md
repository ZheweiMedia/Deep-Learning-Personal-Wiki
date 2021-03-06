# Paper

* **Title**: Improved Dropout for Shallow and Deep Learning
* **Authors**: Li, Zhe, Boqing Gong, and Tianbao Yang
* **Link**: http://papers.nips.cc/paper/6556-improved-dropout-for-shallow-and-deep-learning.pdf
* **Tags**: Neural Network,
* **Year**: 2016
* **Cited by**: 2

# Summary

* What
    * Dropout is equavlent to a data-dependent regularizer. The most simple method is 
multiply hidden units with i.i.d. Bernoulli noise or other types of noise like Gaussian noise.
For the standard dropout different features will have euqal probability to be dropped out. But in 
practice some feature should be more informative than the others. So we should give different features different
sampling probability.

* How
    * The authors proposed a data-dependent dropout which depend on the second order statistics of the data distribution.
In practice, the data distribution means data of a batch.
    * They also proposed a evolutional droput which consider about the distribution
of the layer's outputs.
  
* Results
![Algorithm](images/Improved_dropout.png)
