import numpy as np
import matplotlib.pyplot as plt

def translate(tx, ty):
    return np.array([[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]])

def scale(sx, sy):
    return np.array([[sx, 0, 0],
                     [0, sy, 0],
                     [0, 0, 1]])

def rotate(theta):
    rad = np.radians(theta)
    return np.array([[np.cos(rad), -np.sin(rad), 0],
                     [np.sin(rad), np.cos(rad), 0],
                     [0, 0, 1]])

def apply_transformation(points, transformation_matrix):
    transformed_points = []
    for point in points:
        homogeneous_point = np.array([point[0], point[1], 1])  # Convert to homogeneous coordinates
        transformed_point = np.dot(transformation_matrix, homogeneous_point)
        transformed_points.append((transformed_point[0], transformed_point[1]))
    return transformed_points

def plot_transformation(original, transformed):
    original_x, original_y = zip(*original)
    transformed_x, transformed_y = zip(*transformed)
    
    plt.figure()
    plt.plot(original_x + (original_x[0],), original_y + (original_y[0],), 'bo-', label='Original')
    plt.plot(transformed_x + (transformed_x[0],), transformed_y + (transformed_y[0],), 'ro-', label='Transformed')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True, linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    # Define a square as original shape
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    
    # Define composite transformation: Scale -> Rotate -> Translate
    composite_matrix = translate(2, 3) @ rotate(45) @ scale(1.5, 1.5)
    
    # Apply transformation
    transformed_square = apply_transformation(square, composite_matrix)
    
    # Plot original and transformed shapes
    plot_transformation(square, transformed_square)
