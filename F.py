import numpy as np

def euclidean_distances(A, B):
    A = np.array(A)
    B = np.array(B)

    if A.shape != B.shape:
        raise ValueError("Input vectors must have the same shape")

    # Calculate Euclidean distance
    distance = np.linalg.norm(A - B)

    return distance

if __name__ == '__main__':
    vector_A = np.array([81, 300])
    vector_B = np.array([100, 200])

    distance = euclidean_distances(vector_A, vector_B)
    print(f"Euclidean Distance: {distance}")
