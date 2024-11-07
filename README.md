# ColorClusters-PaintByNumber

Welcome to ColorClusters-PaintByNumber! This project combines the classic "paint-by-number" approach with the power of the K-Means clustering algorithm to create simplified, color-clustered versions of images. Perfect for generating custom paint-by-number templates, pixel art, or exploring clustering in visual contexts.

## 📌 Project Overview

ColorClusters-PaintByNumber takes an input image and processes it through K-Means clustering to reduce the color palette, grouping similar colors into clusters. The result? A stylized, segmented version of the image with distinct color blocks, perfect for generating DIY paint-by-number kits or low-polygon art.

### Key Features

- **Color Reduction**: Uses K-Means clustering to reduce colors in an image while retaining its main details
- **Customizable Clusters**: Adjust the number of color clusters to get the level of detail you want
- **Paint-by-Number Format**: Outputs images with unique colors per cluster, ready to be used for paint-by-number projects
- **Save & Share**: Export the clustered image in common formats (e.g., PNG, JPEG)

## ⚙️ How It Works

1. **Input an Image**: Provide any standard image format
2. **Set Number of Clusters (K)**: Define how many clusters (colors) you want to create. Lower numbers simplify the image; higher numbers retain more detail
3. **Run K-Means Clustering**: The algorithm groups pixels into clusters, assigning a representative color to each
4. **Generate Output**: The output image is a simplified version, ready to use for painting or artistic applications
