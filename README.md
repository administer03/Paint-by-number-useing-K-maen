# ColorClusters-PaintByNumber

Welcome to ColorClusters-PaintByNumber! This project combines the classic "paint-by-number" approach with the power of the K-Means clustering algorithm to create simplified, color-clustered versions of images. The algorithm reduces the image to a limited color palette and overlays numerical labels, making it perfect for custom paint-by-number kits, stylized artwork, or low-poly effects.

## 📌 Project Overview

ColorClusters-PaintByNumber analyzes an image and groups its colors into clusters using K-Means. The output consists of a simplified image with numbered regions and a corresponding color palette.

### Key Features

- **Color Reduction**: Uses K-Means clustering to reduce colors in an image while retaining its main details
- **Customizable Clusters**: Adjust the number of color clusters to get the level of detail you want
- **Paint-by-Number Format**: Outputs images with unique colors per cluster, ready to be used for paint-by-number projects
- **Save & Share**: Export the clustered image in common formats (e.g., PNG, JPEG)

## ⚙️ How It Works

1. **Input an Image**: Provide an image in JPEG, PNG, or BMP format.
2. **Set Number of Colors (K)**: Choose how many clusters/colors the algorithm should generate (default is 10).
3. **Processing**: The algorithm groups pixels, assigns representative colors, detects shapes, and overlays numbers onto the corresponding regions.
4. **Output the Final Image**: Saves the paint-by-number image and its color palette.

## 🔧 Installation

Clone the repository and set up the necessary dependencies.

```bash
git clone https://github.com/administer03/ColorClusters-PaintByNumber.git
cd ColorClusters-PaintByNumber
pip install -r requirements.txt
```
## 🚀 Usage

Run the following command to process an image:

```bash
python main.py <input_image> <output_image> --colors <number_of_colors>
```

### Example

```bash
python main.py ./examples/example1.jpg ./results/output.jpg --colors 8
```

### Parameters

- `--input`: Path to the input image
- `--output`: Path to save the output image
- `--clusters`: Number of color clusters (K)

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
