# Benchmarking different codes

All codes were tested with a N=100_000_000 sample size. The tests were run on a [local machine](#specifications).

### Timed using Jupyter Notebook's %%timeit magic command:
- MC_Pi.py (simple for-loop): **46.9 seconds**
- MC_Pi_numpy.py (Numpy arrays): **2.03 seconds**
- MC_Pi_NumbaCUDA.py (utilizes Numba's CUDA kernels): **8.87 milliseconds**

### Timed using %%timeit command in Jupyter Notebook with [xeus-cling](https://github.com/jupyter-xeus/xeus-cling) kernel:
- MC_Pi.cpp (simple for-loop): **24.1 seconds**

### Timed using _cudaEventElapsedTime_ in Jupyter Notebook with [nvcc4jupyter](https://github.com/andreinechaev/nvcc4jupyter) plugin:
- MC_Pi.cu (Grid-Stride loop): **11.227 milliseconds***

<sub>*It seemed a bit strange to me that a native CUDA code ran slower than a Numba code. It's possible that the difference is caused by different timing methods. _MC_Pi_NumbaCUDA.py_'s kernel was ran after CPU->GPU data migration, while the data migration of _MC_Pi.cu_ may not have finished when the kernel started running. As a test, I timed the _MC_Pi.cu_ kernel running once, and 10000 subsequent times. The former resulted in times around 14.5ms, while the latter gave averages as per above, which might suggest my theory. It's also possible that Numba is very well optimized, and even an amateur code can outperform an amateur code written in CUDA.</sub> 

<br></br>
<br></br>
### Specifications:
**CPU:** AMD Ryzen 7 6800H \
**GPU:** NVIDIA GeForce RTX 3050 Ti
