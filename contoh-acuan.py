import numpy as np

def simplex_method(c, A, b):
    m, n = A.shape
    c = np.array(c + [0] * m).astype(float)
    A = np.hstack([A, np.eye(m)]).astype(float)
    c_b = np.array(c[-m:]).astype(float)
    b = np.array(b).astype(float)
    
    while any(c > 0):
        pivot_column = np.argmax(c)
        ratios = []
        for i in range(m):
            if A[i, pivot_column] > 0:
                ratios.append(b[i] / A[i, pivot_column])
            else:
                ratios.append(np.inf)
        pivot_row = np.argmin(ratios)
        pivot_element = A[pivot_row, pivot_column]
        
        A[pivot_row, :] /= pivot_element
        b[pivot_row] /= pivot_element
        
        for i in range(m):
            if i != pivot_row:
                factor = A[i, pivot_column]
                A[i, :] -= factor * A[pivot_row, :]
                b[i] -= factor * b[pivot_row]
                
        factor = c[pivot_column]
        c -= factor * A[pivot_row, :]
    
    solution = {f'x{i + 1}': 0 for i in range(n)}
    for i in range(m):
        non_zero_indices = np.nonzero(A[i, :n])[0]
        if len(non_zero_indices) == 1 and b[i] != 0:
            index = non_zero_indices[0]
            solution[f'x{index + 1}'] = b[i]
    
    optimal_value = np.dot(c_b, b)
    return solution, optimal_value

# Contoh kasus pemrograman linier
c = [3, 2]  # Koefisien fungsi tujuan
A = np.array([[1, -1], [3, 1], [4, 3]])  # Matriks koefisien kendala
b = [2, 5, 7]  # Vektor batasan kendala

solution, optimal_value = simplex_method(c, A, b)
print("Solusi:", solution)
print("Nilai Optimal:", optimal_value)
