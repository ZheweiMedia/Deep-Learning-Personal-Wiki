# Paper

* **Title**: Parallel Multi-Dimensional LSTM, With Application to Fast Biomedical Volumetric Image Segmentation
* **Authors**: Marijn F. Stollenga, Wonmin Byeon, Marcus Liwicki, Juergen Schmidhuber
* **Link**: https://arxiv.org/pdf/1506.07452.pdf
* **Tags**: Neural Network,
* **Year**: 2017
* **Cited by**: 40

# Summary

* What
    * Previous M(ulti)D(imensinal)-LSTM is hard to parallelize on GPU. The authors propose a method that
    change the traditional cuboid order to pyramidal order. And this PyraMiD-LSTM is easy to parallelize,
    especially for 3D data.

* How
  
* Experiments
    * Sub-volumes and Augmentation. Because of lack of memory, the authors train and test on sub-volumes.
    In test, the sub-volumes are stitches together by Gaussian kernel.
    * Pre-processing. In this paper the authors use EM dataset and MR Brain dataset. So both them are about greyscale
    medical images. The first step is normalize each input slice as N(0,1). Then enhance the local contrast by subtruct Gaussian smoothed
    images then Contrast-Limited Adaptive Histogram Equalization (CLAHE).
    **Image**
    * Bootstrapping to speed up training. Doesn't like CNN, LSTM is difficult to parallelize. It ralate to the length of the
    squences. When apply LSTM on image, the sequence is very long. At here the authors use some trick to speed up training.
    So at begining they run LSTM on the block of 64\*64\*8, then 128\*128\*15, then 256\*256*20. It means in these three step, the
    inital value of parameters of next step is from the last step. So it doesn't shorten the time for each epoch. It reduce the epoch
    needed for the original image segmentation.
    * In experiments they use three PyraMiD-LSTM layers. And use fully-connected layer to connect them. I think at here it is not
    necessary to be fully-connected.
    **Image**
