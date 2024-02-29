#include <stdio.h>
#include <assert.h>
#include <curand_kernel.h>

const int numOfThreads = 1024;

inline cudaError_t checkCuda(cudaError_t result) {
  if (result != cudaSuccess) {
    fprintf(stderr, "CUDA Runtime Error: %s\n", cudaGetErrorString(result));
    assert(result == cudaSuccess);
  }
  return result;
}

__global__
void piApproximation(unsigned long long *inside, int N) {
    int index = threadIdx.x + blockDim.x * blockIdx.x;
    int stride = gridDim.x * blockDim.x;
    __shared__ unsigned long long counter[numOfThreads];
    double x, y;

    curandState_t rng;
	curand_init(clock64(), index, 0, &rng);

    for (int i=index; i<N; i+=stride) {
        x = curand_uniform_double(&rng);
        y = curand_uniform_double(&rng);
        if (x*x+y*y < 1) {
            counter[threadIdx.x] += 1;
        }
    }

    __syncthreads();

    if (threadIdx.x == 0) {
        inside[blockIdx.x] = 0;
        for (int i = 0; i<numOfThreads; i++) {
            inside[blockIdx.x] += counter[i];
        }
    }
}

int main() {
    int deviceId;
    int numberOfSMs;

    cudaGetDevice(&deviceId);
    cudaDeviceGetAttribute(&numberOfSMs, cudaDevAttrMultiProcessorCount, deviceId);

    int N = 100000000;
    unsigned long long *inside;
    size_t size = sizeof(unsigned long long);

    cudaMallocManaged(&inside, size);
    cudaMemPrefetchAsync(inside, size, deviceId);

    int threadsPerBlock = numOfThreads;
    int blocksPerGrid = numberOfSMs;

    piApproximation<<<blocksPerGrid, threadsPerBlock>>>(inside, N);

    checkCuda(cudaDeviceSynchronize());

    unsigned long long result = 0;

    for (int i=0; i<blocksPerGrid; i++) {
        result += inside[i];
    }

    cudaFree(inside);

    printf("%f", 4*(double)result/N);

    return 0;
}
