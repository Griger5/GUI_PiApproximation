#include <iostream>
#include <random>
#include <time.h>

double piApproximation(int N) {
    std::default_random_engine generator{static_cast<long unsigned int>(time(0))};
    std::uniform_real_distribution<double> distribution(-1, 1);
    double x, y, inside;

    for (int i=0; i<N; i++) {
        x = distribution(generator);
        y = distribution(generator);
        if (x*x + y*y < 1) {
            inside++;
        }
    }

    return 4*inside/N;
}

int main() {
    double result;
    int N = 100000000;
    result = piApproximation(N);
    std:: cout << result;
    return 0;
}