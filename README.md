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

## 🔧 Installation

Clone the repository and set up the necessary dependencies.

```bash
git clone https://github.com/administer03/ColorClusters-PaintByNumber.git
cd ColorClusters-PaintByNumber
pip install -r requirements.txt
```
## 🚀 Usage

After installation, run the following command to start clustering an image:

```bash
python color_clusters.py --input <path_to_image> --clusters <number_of_clusters> --output <output_path>
```

### Example

```bash
python color_clusters.py --input my_image.jpg --clusters 8 --output clustered_image.png
```

### Parameters

- `--input`: Path to the input image
- `--clusters`: Number of color clusters (K) for the algorithm
- `--output`: Path for saving the output image

## 🎨 Examples

| Original Image | K = 4 Clusters | K = 8 Clusters |
|---------------|----------------|----------------|
| [Placeholder] | [Placeholder]  | [Placeholder]  |

## 🤝 Contributions

Contributions, ideas, and feedback are welcome! Feel free to open issues or pull requests.

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

## 🌟 Acknowledgments

Special thanks to the open-source libraries and community that make projects like this possible. Inspired by the intersection of art and data science!
