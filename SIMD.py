import numpy as np
import time

# Demonstrating SIMD with NumPy, which uses SIMD under the hood
array1 = np.array([1, 2, 3, 4] * 250000, dtype=np.float32)
array2 = np.array([5, 6, 7, 8] * 250000, dtype=np.float32)

start = time.time()
result = array1 * array2  # Element-wise multiplication
print(f"Time taken for SIMD-like operation: {time.time() - start:.6f} seconds")
