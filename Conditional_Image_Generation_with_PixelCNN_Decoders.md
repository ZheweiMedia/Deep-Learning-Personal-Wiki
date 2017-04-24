# Paper

* **Title**: Conditional Image Generation with PixelCNN Decoders
* **Authors**: Aaron van den Oord, Nal Kalchbrenner, Oriol Vinyals, Lasse Espeholt, Alex Graves, Koray Kavukcuoglu
* **Link**: http://papers.nips.cc/paper/6527-conditional-image-generation-with-pixelcnn-decoders
* **Tags**: Neural Network,
* **Year**: 2016
* **Cited by**: 49

# Summary

* What
    * This paper expores image generation with PixelCNN. This model can be conditioned on any vector.
    If it conditioned on previous pixels, then it can predict current pixel. If conditioned on class labels, then it can generate images like GAN. But as the
    authors claimed, Conditional PixelCNN has the advantage that it can return a explicit probability densities, which cannot be done by GAN. The author also 
    show that PixelCNN can be used as a decoder if we set the condition as the output of encoder.
    
* How
    * In previous papers, PixelRNN performs better than PixelCNN. Two possible reasons. The first one is PixelRNN can use all previous pixels, but the dependent
    region for PixelCNN is bounded. The authors claim that it can be alleviated by using suffiently layers. The second reason is PixelRNN use gates, so 
    it can model more complex interactions. So the authors also add gate to PixelCNN with the **gated activation unit**:
    * Blind spot. Previous version PixelCNN cannot use all previous pixels. Now they use horizontal and vertical convolutional networks to fix thsi problem.
    * Conditional PixelCNN with a latent vector **h**. If **h** is one-hot encoding and we add **h** to every layer, then it is equivalent to adding
    class dependent bias to every layer. Then we can generate images from class labels. We even can set the position for the generation by replace **h** with
    **s**=m(**h**), which has the same size with the image.
    * PixelCNN Auto-Encoder. Because Conditional PixelCNN can generate images from images representation, so it we set the image representation as the
    output of encoder. Conditional PixelCNN has the good ability to handle pixel statistics by predicting pixel with previous pixels. So for encoder, 
    it doesn't have to encoder the pixel relationship.
  
* Results
![Algorithm](images/Improved_dropout.png)
