import numpy as np
import time

# Simulating vector operations using NumPy
vector_a = np.random.rand(1000000)
vector_b = np.random.rand(1000000)

start_time = time.time()
vector_c = vector_a + vector_b  # Vector addition
end_time = time.time()

print(f"Vector operation completed in {end_time - start_time:.6f} seconds.")
