**AutoColorCorrelogramFilter**
SYNOPSIS
A batch filter for calculating a color correlogram from an image. A color correlogram encodes the spatial correlation of colors in an image, and is an effective feature that is robust to changes in viewing position and camera zoom.

**BinaryPatternsPyramidFilter**
SYNOPSIS
A batch filter for extracting a pyramid of rotation-invariant local binary pattern histograms from images. Each local binary pattern represents an intensity pattern (e.g. an edge or a corner) around a point. A histogram of local binary patterns therefore encodes the larger scale patterns that occur across regions of images. Local binary patterns are useful for texture and face recognition.

**ColorLayoutFilter**
SYNOPSIS
A batch filter for extracting MPEG7 color layout features from images. This filter divides an image into 64 blocks and computes the average color for each block, and then features are calculated from the averages.

**EdgeHistogramFilter**
SYNOPSIS
A batch filter for extracting MPEG7 edge histogram features from images. Edges are the lines or discontinuities in an image.  An edge histrogram is therefore a summary of the directions that the edges are going in across an image.

**FCTHFilter**
SYNOPSIS
A batch filter for extracting FCTH color features from images. FCTH stands for 'Fuzzy Color and Texture Histogram', and as the name suggests, these features encode both color and texture information in one histogram.  One bonus of this feature is that it is very small -- limited to 72 bytes per image -- and therefore suitable for  large image datasets.

**FuzzyOpponentHistogramFilter**
SYNOPSIS
A batch filter for extracting a fuzzy 64-bin histogram, based on the Opponent color space, from images.

**GaborFilter**
SYNOPSIS
A batch filter that uses a Gabor wavelet to extract texture features from images. Gabor filters are very common in computer vision, and the features should be invariant to rotation.

**JpegCoefficientFilter**
SYNOPSIS
A batch filter for extracting JPEG coefficients from images.  Converting an image to the JPEG file format discards information that it imperceptible to humans  and in the process produces a sequences of quantized coefficients that are part of the compressed  representation of the image. These coefficients are the features computed by this filter.

**PHOGFilter**
SYNOPSIS
A batch filter for extracting PHOG features from images.PHOG stands for 'Pyramid Histogram of Oriented Gradients', and as the name suggests, it encodes information about the orientation of intensity gradients across an image.

**SimpleColorHistogramFilter**
SYNOPSIS
A batch filter for extracting color histogram feature from images.  This is the most basic color feature that can be computed; essentially, it three histograms  (one for red, one for green, one for blue) each of which has 32 bins.  Each bin contains a count of the pixels in the image that fall into that bin.

