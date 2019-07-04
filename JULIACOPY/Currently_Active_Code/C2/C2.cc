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
#include <cstdio>
#include <ctime>
//using namespace std; DON'T DO THIS IT IS BAD PRACTICE
using std::cin;
using std::cout;
using std::endl;
using std::mt19937_64;


/*
    TESTING VERSION OF COUPON COLLECTOR'S PROBLEM (HAS LOOPS)

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


template<typename RNG>
static bool seenAll(int64_t N, std::vector<bool>& mark, RNG& rng, int64_t samples)
{
    std::uniform_int_distribution<int64_t> dist(0, N-1);
    int64_t counter = 0;
    //std::vector<int64_t> seen;
    //seen.reserve(1024);
    for(;samples > 0;--samples){
        int64_t index = dist(rng);
        if(!mark[index]){
            counter++;
            //seen.push_back(index);
            mark[index] = true;
        }
    }
    //for(auto s: seen)
        //mark[s] = false;
    //seen.clear();
    for (int64_t i=0; i<N; ++i)
        mark[i] = false;
    return (counter == N);
}



//MULTIPLE RUNS AND TESTING VERSION
int main()
{
    const double pi = std::acos(-1);

    cout << endl;
    double epsilon;
    cout << "Epsilon Value: ";
    while (std::cin >> epsilon) {
        int64_t n;
        double delta;
        cout << "Delta Value: ";
        cin >> delta;
        cout << "N Value: ";
        cin >> n;
        double c;
        cout << "C Value: ";
        cin >> c;
        int reps;
        cout << "Number of tests: ";
        cin >> reps;

        std::clock_t start;
        double duration;
        start = std::clock();

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
        //int64_t samples = int64_t(n * log(n) + c * n); //for actual n

        int64_t successes = 0;
        for (int64_t i=0; i<reps; ++i){
            bool result = seenAll(n, mark, rng, samples);
            if(result){
                successes++;
                //cout << successes << endl;
            }
        }

        double success_prob = double(successes) / double(reps);

        duration = (std::clock() - start) / (double) CLOCKS_PER_SEC;

        
        cout << endl;
        cout << "---RUN REPORT---" << endl;
        cout << "Epsilon            : " << epsilon << endl;
        cout << "Delta              : " << delta << endl;
        cout << "N                  : " << n << endl;
        cout << "N~                 : " << approximate_n << endl;
        cout << "M~                 : " << m2 << endl;
        cout << "C                  : " << c << endl;
        cout << "# of Repetitions   : " << reps << endl;
        cout << "# Successes        : " << successes << endl;
        cout << "Pr[Success]        : " << success_prob << endl;
        cout << "Seconds Taken      : " << duration << endl;



        return 0;

    }
}