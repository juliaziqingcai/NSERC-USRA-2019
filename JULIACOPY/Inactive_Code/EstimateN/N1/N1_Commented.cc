#include <iostream>
#include <vector>
#include <cmath>
#include <array>
#include <random>
#include <algorithm>
#include <fstream>
#include <string>
//using namespace std; DON'T DO THIS IT IS BAD PRACTICE
using std::cin;
using std::cout;
using std::endl;
using std::mt19937_64;
//Instead of constantly typeing out namespace::object/function,
//can declare using namespace::object at the top of the file and call directly in file


/*
    ORIGINAL VERSION IN C++ OF NewEstimateN 
    (Commented by Julia for learning purposes)

This copy of N1 is meant for LEARNING PURPOSES ONLY.
It contains all the code of N1.cc, along with Julia's comments
on how things work and why certain decisions were made.
It also includes a commentary on the Makefile of N1.cc at the bottom,
so this file is NOT meant to be run.

Ported to C++ for speed gains (faster by X100)
Credits of actual code go to Luis Fernando Schultz Xavier da Silveira (PhD)

The algorithm works as follows:

    1. 

*/

template<typename RNG>
//must declare template to pass the rng as identified properly
//else we get unidentified/undeclared issues
//defines a whole new type called RNG, that we can manipulate however
//we want despite not having specified literally anything about it
static int64_t SUD(int64_t N, std::vector<bool>& mark, RNG& rng)
//pass the array to operate on and the rng by reference to eliminate
//having to reinitialize every single time, is much faster
{
    std::uniform_int_distribution<int64_t> dist(0, N-1);
    //create a uniform distribution with a range of values of [0, N-1] for available indices
    //with integer values using a discrete probability function
    int64_t counter = 0;
    std::vector<int64_t> seen;
    //set up vector of already seen indices, faster than initializing new vector every time
    seen.reserve(1024);
    //a hack to automatically allocate enough room for at least 1024 elements,
    //gives speed boost 
    while(true){//for(;;) //alternate way of infinite loop
        int64_t index = dist(rng);
        //calls the initialized distribution to spit out a truly random number from range
        counter++;
        if(!mark[index]){
            seen.push_back(index);
            mark[index] = true;
        }else
            break;
    }
    for(auto s: seen) 
    //range-based for loop, iterates over a range for a more intuitive loop
    //available since C++11
    //the keyword auto does type inference so that you can delcare variables without
    //having to explicitly state the data type;
        mark[s] = false;
    seen.clear();
    //removes all elements from the vector, making it size 0
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

int main()
{
    const double pi = std::acos(-1);
    //pi must be set as it isn't defined in the math library
    //use arcos(-1) to calculate pi instead

    double epsilon;
    cout << "Epsilon Value: ";
    while (std::cin >> epsilon) {
        //while loop to allow for terminal testing
        int64_t n;
        //set as int64_t to prevent integer overflow, gives 64 bits of range
        double delta;
        cout << "Delta Value: ";
        cin >> delta;
        cout << "N Value: ";
        cin >> n;

        mt19937_64 rng; 
        //A Mersenne Twister pseudo-random generator of 32-bit numbers with a state size of 19937 bits.
        rng.seed(std::random_device()());
         //seed the RNG witht the random device to become a truly RANDOM rng
         //is a uniformly-distributed integer random number generator that 
         //produces non-deterministic random numbers.

        int64_t best_k = int64_t(ceil(1.2632/ pow(epsilon, 2)));
        int64_t l = int64_t(ceil( 12 * log(1/delta)));
        //the two above are typecast to ensure no possibilty of overflow or typing issues related to
        //later calculations

        std::vector<bool> mark(n, false);
        //declares a vector of booleans, initialized with n elements, each element is the boolean false
        //one can also declare such a vector's elements explicitly individually

        std::vector<double> counters(l);
        for (auto& counter: counters)
            counter = RSUD(n, best_k, mark, rng);

        std::nth_element(counters.begin(), counters.begin()+l/2, counters.end());
        //partial sorting algorithm that ensures that the nth element is pointed to correctly
        //as if all elements in the given range were sorted.
        //quickly finds nth element and shuffles it into place relative to all other elements
        // in a < or > relation only in the given range
        // parameters are (start, n-th element wanted, end)
        double median = counters[l/2];
        double m = median - 2.0/3;
        double approximate_n = 2 / pi * m * m;
        
        cout << approximate_n << endl;

        return 0;

    }
}

//*************************MAKEFILE PORITION***********************************
/*
N1:	N1.cc
	c++ -std=c++14 -o /tmp/N1 N1.cc -march=native -O2 -pipe -fomit-frame-pointer -fwhole-program



c++:
    The compiler chosen is c++ here because the lab machines and Julia's VMs are ALL run with Ubuntu.
    On Ubuntu specifically, the c++ compiler command IS THE SAME as the normal/usual g++ compiler.
    This is due to if one does 
        ls -l /usr/bin/c++
    then they will see that is it's a symbolic link to
        /etc/alternatives/c++ 
    which is a symbolic link to 
        /usr/bin/g++

/tmp/N1:
    Since the file is stored on a USB, along with the rest of the repositiory 
    ('cause Julia's a paranoid n00b who likes to carry everything, all the time), 
    there are access issues for execution on Linux systems, so the final output file 
    must be stored elsewhere and called from elsewhere, so we just stuck it in the 
    /tmp directory for giggles.

-march=native:
    Will customize the optimization to the specific machine/setup the program is compiled and run on,
    making the most of what each machine has, and requires a re-compilation for every new transfer of file

-O2:
    Level 02 optimization, between the -O and -O3 level options.
    The GCC will performs nearly all supported optimizations that do not involve a
    space-speed tradeoff. Increases both compilation time, and the performance of the
    generated code. There is a giant list of optimization flags that this options turns on,
    which includes all flags turned on by the -O option

-pipe:
    Use pipes rather than temporary files for communication between the various stages of compilation. 
    This fails to work on some systems where the assembler is unable to read from a pipe; 
    but the GNU assembler has no trouble. 

-fomit-frame-pointer:
    Don't keep the frame pointer in a register for functions that don't need one. 
    This avoids the instructions to save, set up and restore frame pointers; 
    it also makes an extra register available in many functions.
    NOTE: May make debugging IMPOSSIBLE on some machines (this is according to official documentation,
    not my personal words)
    Enabled at levels -o, o2, -o3, -os.

-fwhole-program:
    Forces the compiler to acknowledge this one file as the whole program, and therefore forces more
    aggressive optimization since there is nothing else to juggle/consider



clean:
	rm -f main

*/
