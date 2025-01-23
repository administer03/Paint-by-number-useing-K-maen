import argparse
import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def plot_color(color, y_, x_):
    im = np.zeros((y_, x_, 3))
    for y in range(y_):
        for x in range(x_):
            if y == 0 or x == 0 or y == (y_-1) or x == (x_-1):
                im[y][x] == 255
            else:
                im[y][x] = color
    return im

def put_text(img_plt, text, x, y):
    cv2.putText(
        img_plt,
        str(text),
        (x,y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.4,
        (0, 0, 0, 0),
        2)

def check_bool(x, y, size_x, size_y, edges_image):
    for i in range(y, y + size_y):
        for j in range(x, x+ size_x):
            try:
                if edges_image[j][i] != 255:
                    return False
            except:
                pass
    return True

def process_image(input_path, output_path, colors=10):
    # Read and preprocess image
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError(f"Could not read image at {input_path}")
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.array(img, dtype=np.float64) / 255
    
    # Get image dimensions
    w, h, d = original_shape = tuple(img.shape)
    img_reshaped = np.reshape(img, (w * h, d))
    
    # Perform K-means clustering
    kmeans = KMeans(n_clusters=colors, random_state=0).fit(img_reshaped)
    labels = kmeans.predict(img_reshaped)
    mean_ = kmeans.cluster_centers_
    
    # Create edge image
    img_gray = cv2.imread(input_path, 0)
    edges = cv2.Canny(img_gray, 100, 200)
    
    # Invert edges
    edges = 255 - edges
    
    # Create color-clustered image
    img_kmean = np.zeros((w, h, d))
    label_idx = 0
    for i in range(w):
        for j in range(h):
            img_kmean[i][j] = mean_[labels[label_idx]]
            label_idx += 1
    
    # Sort colors by intensity
    mean_sort = sorted(mean_, key=lambda x: sum(x))
    
    # Create paint-by-numbers result
    size_x = 17
    size_y = 17
    copy_edge = edges.copy()
    color_edge = img_kmean.copy()
    
    # Add numbers to regions
    for round in range(len(mean_sort)):
        for y_ in range(0, w, size_y):
            for x_ in range(0, h, size_x):
                if sum(color_edge[y_][x_]) == sum(mean_sort[round]):
                    status = check_bool(x_, y_, size_x, size_y, copy_edge)
                    if status:
                        put_text(copy_edge, round+1, x_, y_)
                        break
    
    # Convert grayscale edge image to RGB
    copy_edge_rgb = cv2.cvtColor(copy_edge.astype(np.uint8), cv2.COLOR_GRAY2RGB)
    
    # Create color palette
    palette_height = 100
    palette_width = img.shape[1]
    color_palette = np.zeros((palette_height, palette_width, 3))
    
    # Fill color palette with the sorted colors
    segment_width = palette_width // len(mean_sort)
    for i, color in enumerate(mean_sort):
        start_x = i * segment_width
        end_x = start_x + segment_width
        color_palette[:, start_x:end_x] = color
        
        # Add number labels to the palette
        label_x = start_x + segment_width // 2 - 10
        cv2.putText(color_palette, str(i+1), (label_x, palette_height//2),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
    
    # Convert color palette to uint8 and ensure it's in the range [0, 255]
    color_palette = (color_palette * 255).astype(np.uint8)
    
    # Combine the paint-by-numbers image with the color palette
    final_image = np.vstack([copy_edge_rgb, color_palette])
    
    # Save the result
    cv2.imwrite(output_path, cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR))
    print(f"Paint-by-numbers image saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Create a paint-by-numbers image using clustering')
    parser.add_argument('input_path', type=str, help='Path to the input image')
    parser.add_argument('output_path', type=str, help='Path to save the output image')
    parser.add_argument('--colors', type=int, default=10, help='Number of colors to use (default: 10)')
    
    args = parser.parse_args()
    
    try:
        process_image(args.input_path, args.output_path, args.colors)
    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
    
# example usage: python main.py ./examples/example1.jpg ./results/output.jpg --colors 10