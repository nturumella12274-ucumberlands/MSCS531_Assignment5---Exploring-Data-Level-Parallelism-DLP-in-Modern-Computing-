from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time

# Function to simulate a computation-intensive task
def compute(x):
    return np.sin(x) ** 2 + np.cos(x) ** 2

data = np.random.rand(1000000)

start_time = time.time()
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(compute, data))
end_time = time.time()

print(f"Parallel loop execution completed in {end_time - start_time:.6f} seconds.")
