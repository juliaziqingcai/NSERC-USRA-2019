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
    MULTI-THREADED VERSION IN C++ OF NewEstimateN

Ported to C++ for speed gains (faster by X100)
The multi-threading gives a speed boost of X2 (not X8, like the number
of cores in the machine promised, most probably due to large amount of
memory needed)

Meant to be used in terminal with the following commands:

    make

    time /tmp/N2

Credits of actual code go to Luis Fernando Schultz Xavier da Silveira (PhD)

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

struct Slave {
    std::thread thread;
    uint64_t result;
    std::vector<bool> mark;
    mt19937_64 rng;
};

static void task(int64_t N, int64_t rep, Slave& s) {
  uint64_t sum = 0;
  for (; rep != 0; --rep)
    sum+= SUD(N, s.mark, s.rng);
  s.result = sum;
}

static double RSUD(int64_t N,int64_t k, std::vector<Slave>& slaves)
{
    int64_t workload = k / slaves.size();
    bool first = true;
    for (Slave& s: slaves) {
      s.thread = std::thread(task, N, first ? workload + (k%slaves.size()) : workload, std::ref(s));
      first = false;
    }
    uint64_t grand_sum = 0;
    for (Slave& s: slaves) {
      s.thread.join();
      grand_sum+= s.result;
    }
    return double(grand_sum)/k;
}

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

        auto num_cores = std::thread::hardware_concurrency();
        assert((num_cores != 0));
            std::vector<Slave> slaves(num_cores);
        for (Slave& s: slaves) {
                    s.rng.seed(std::random_device()()); //seed the RNG
            s.mark.resize(n, false);
        }

        int64_t best_k = int64_t(ceil(1.2632/ pow(epsilon, 2)));
        int64_t l = int64_t(ceil( 12 * log(1/delta)));

        std::vector<double> counters(l);
        for (auto& counter: counters)
            counter = RSUD(n, best_k, slaves);

        std::nth_element(counters.begin(), counters.begin()+l/2, counters.end());
        double median = counters[l/2];
        double m = median - 2.0/3;
        double approximate_n = 2 / pi * m * m;
        
        cout << approximate_n << endl;

        return 0;

    }
}


