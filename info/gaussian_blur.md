# Gaussian Blur Filter

The Gaussian Blur filter is a widely used image smoothing technique that reduces noise and detail in an image.

## How it Works
The filter works by applying a Gaussian function to create a kernel that is used to blur the image. Each pixel's new value is a weighted average of its neighboring pixels, with weights determined by the Gaussian distribution.

## Parameters
- **Kernel Size**: Controls the size of the blur effect (must be odd number)
- **Sigma**: Controls the spread of the Gaussian distribution

## Use Cases
- Noise reduction
- Pre-processing for edge detection
- Creating soft focus effects
- Reducing image detail

### Example Image
![Gaussian Blur Example](https://via.placeholder.com/150)
