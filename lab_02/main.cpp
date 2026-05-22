#include <iostream>
#include <ctime>
#include <fstream>
#include <string>

using namespace std;

int calculate() {
    int x = 10;
    return x * x - x * x + x * 4 - x * 5 + x + x;
}


int main() {
    long long n;
    double time;
    ofstream output_file("result_cpp.csv");
    output_file << "time,n\n";
    for (n == 1e3; n < 1e6; n += 1e3) {
        clock_t start = clock();

        for (long i = 0; i < n; i++)
        {
            int res = calculate();
        }

        clock_t end = clock();
        time = (double)(end - start) / CLOCKS_PER_SEC;
	output_file << time << "," << n << "\n";
    }
    output_file.close();
    return 0;
}

