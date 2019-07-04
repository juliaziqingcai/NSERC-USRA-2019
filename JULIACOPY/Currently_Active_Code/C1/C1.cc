#include <iostream>
#include <vector>
#include <cmath>
#include <array>
#include <random>
#include <algorithm>
#include <fstream>
#include <string>
#include <thread>
#include <cassert>
//using namespace std; DON'T DO THIS IT IS BAD PRACTICE
using std::cin;
using std::cout;
using std::endl;
using std::mt19937_64;


/*
    ORIGINAL VERSION IN OF COUPON COLLECTOR PROBLEM (SINGLE RUN)

*/

template<typename RNG>
static int64_t SUD(int64_t N, std::vector<bool>& mark, RNG& rng) 
{
    std::uniform_int_distribution<int64_t> dist(0, N-1);
    int64_t counter = 0;
    std::vector<int64_t> seen;
    seen.reserve(1024);
    while(true){//for(;;)
        int64_t index = dist(rng);
        counter++;
        if(!mark[index]){
            seen.push_back(index);
            mark[index] = true;
        }else
            break;
    }
    for(auto s: seen)
        mark[s] = false;
    seen.clear();
    return counter;
}


template<typename RNG>
static double RSUD(int64_t N,int64_t k, std::vector<bool>& mark, RNG& rng)
{
    int64_t result = 0;
    for (int64_t i=0; i<k; ++i) 
        result += SUD(N, mark, rng);

    return double(result)/k;
}

// SINGLE RUN VERSION
int main()
{
    const double pi = std::acos(-1);

    double epsilon;
    cout << "Epsilon Value: ";
    while (std::cin >> epsilon) {
        int64_t n;
        double delta;
        cout << "Delta Value: ";
        cin >> delta;
        cout << "N Value: ";
        cin >> n;
        int c;
        cout << "C Value: ";
        cin >> c;

        mt19937_64 rng;
        rng.seed(std::random_device()()); //seed the RNG

        int64_t best_k = int64_t(ceil(1.2632/ pow(epsilon, 2)));
        int64_t l = int64_t(ceil( 12 * log(1/delta)));

        std::vector<bool> mark(n, false);

        std::vector<double> counters(l);
        for (auto& counter: counters)
            counter = RSUD(n, best_k, mark, rng);

        std::nth_element(counters.begin(), counters.begin()+l/2, counters.end());
        double median = counters[l/2];
        double m = median - 2.0/3;
        double approximate_n = 2 / pi * m * m;

        double m2 = approximate_n/(1-epsilon);
        int64_t samples = int64_t(m2 * log(m2) + c * m2);

        std::uniform_int_distribution<int64_t> dist(0, n-1);
        int64_t numSeen = 0;
        for (int64_t i=0; i<samples; ++i){
            int64_t index = dist(rng);
            if(!mark[index]){
                numSeen++;
                mark[index] = true;
            }
        }

        bool seenAll = false;
        if (numSeen == n){
            seenAll = true;
        }

        cout << endl;
        cout << "---RUN REPORT---" << endl;
        cout << "Epsilon            : " << epsilon << endl;
        cout << "Delta              : " << delta << endl;
        cout << "N                  : " << n << endl;
        cout << "N~                 : " << approximate_n << endl;
        cout << "C                  : " << c << endl;
        cout << "# Elements Seen    : " << numSeen << endl;
        cout << "Seen all elements? : " << seenAll << endl;
        cout << endl <<  "NOTE: 0 = false  !0 = true" << endl;


        return 0;

    }
}