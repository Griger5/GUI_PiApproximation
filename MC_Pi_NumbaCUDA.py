import numpy as np
from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states, xoroshiro128p_uniform_float32

@cuda.jit
def piApproximation(rng_states, n, out):
    thread_id = cuda.grid(1)
    stride = cuda.gridsize(1)
    
    inside = 0
    for i in range(thread_id, n, stride):
        x = xoroshiro128p_uniform_float32(rng_states, thread_id)
        y = xoroshiro128p_uniform_float32(rng_states, thread_id)
        if (x**2 + y**2) < 1.0:
            inside += 1
    
    out[thread_id] = (4.0 * inside / n) * stride

n = 10**7
blocks_per_grid = 128
threads_per_block = 512

grid_size = threads_per_block * blocks_per_grid

rng_states = create_xoroshiro128p_states(grid_size, seed=1)
d_out = cuda.device_array(grid_size, dtype=np.float32)

piApproximation[blocks_per_grid, threads_per_block](rng_states, n, d_out)
result = d_out.copy_to_host().mean()
print(result)