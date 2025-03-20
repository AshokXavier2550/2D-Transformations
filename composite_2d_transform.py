import numpy as np
import matplotlib.pyplot as plt  


def get_shape():
    print("\nChoose a shape:")
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Pentagon")
    print("4. Circle")
    print("5. Custom Shape")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:  # Triangle
        print("\nEnter 3 points for the triangle:")
        points = [tuple(map(float, input(f"Enter point {i+1} (x y): ").split())) for i in range(3)]
    
    elif choice == 2:  # Rectangle
        print("\nEnter 4 points for the rectangle:")
        points = [tuple(map(float, input(f"Enter point {i+1} (x y): ").split())) for i in range(4)]
    
    elif choice == 3:  # Pentagon
        print("\nEnter 5 points for the pentagon:")
        points = [tuple(map(float, input(f"Enter point {i+1} (x y): ").split())) for i in range(5)]
    
    elif choice == 4:  # Circle (approximated with 100 points)
        num_points = 100
        radius = float(input("Enter radius of the circle: "))
        points = [(radius * np.cos(2 * np.pi * i / num_points), 
                   radius * np.sin(2 * np.pi * i / num_points)) for i in range(num_points)]
    
    elif choice == 5:  # Custom shape
        num_points = int(input("Enter the number of points for your shape: "))
        points = [tuple(map(float, input(f"Enter point {i+1} (x y): ").split())) for i in range(num_points)]
    
    else:
        print("Invalid choice! Defaulting to a triangle.")
        points = [(0, 0), (1, 0), (0.5, 1)]
    
    return np.array(points)





def translate(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])
    return apply_transformation(points, translation_matrix)

def scale(points, sx, sy):
    centroid = np.mean(points, axis=0)
    points = translate(points, -centroid[0], -centroid[1])  # Move to origin
    scaling_matrix = np.array([[sx, 0, 0],
                               [0, sy, 0],
                               [0, 0, 1]])
    points = apply_transformation(points, scaling_matrix)
    return translate(points, centroid[0], centroid[1])  # Move back

def rotate(points, angle):
    centroid = np.mean(points, axis=0)
    points = translate(points, -centroid[0], -centroid[1])  # Move to origin
    rad = np.radians(angle)
    rotation_matrix = np.array([[np.cos(rad), -np.sin(rad), 0],
                                [np.sin(rad), np.cos(rad), 0],
                                [0, 0, 1]])
    points = apply_transformation(points, rotation_matrix)
    return translate(points, centroid[0], centroid[1])  # Move back

def apply_transformation(points, transformation_matrix):
    homogeneous_points = np.hstack((points, np.ones((points.shape[0], 1))))
    transformed_points = homogeneous_points.dot(transformation_matrix.T)
    return transformed_points[:, :2]

def plot_shapes(original, transformed):
    plt.clf()  # Clear the plot
    plt.figure(figsize=(6, 6))

    original_closed = np.vstack([original, original[0]])  
    plt.plot(original_closed[:, 0], original_closed[:, 1], 'bo-', label="Original")

    transformed_closed = np.vstack([transformed, transformed[0]])
    plt.plot(transformed_closed[:, 0], transformed_closed[:, 1], 'ro-', label="Transformed")

    plt.legend()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)

    filename = "output.png"
    plt.savefig(filename)
    print(f"Transformation plot saved as {filename}")  
    plt.show()

shape = get_shape()
original_shape = np.copy(shape)

while True:
    print("\nChoose a transformation:")
    print("1. Translation")
    print("2. Scaling")
    print("3. Rotation")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        tx = float(input("Enter translation in X (tx): "))
        ty = float(input("Enter translation in Y (ty): "))
        shape = translate(shape, tx, ty)
    elif choice == 2:
        sx = float(input("Enter scaling in X (sx): "))
        sy = float(input("Enter scaling in Y (sy): "))
        shape = scale(shape, sx, sy)
    elif choice == 3:
        angle = float(input("Enter rotation angle in degrees (θ): "))
        shape = rotate(shape, angle)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Try again.")

plot_shapes(original_shape, shape)
