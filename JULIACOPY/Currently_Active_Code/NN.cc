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
using std::cin;
using std::cout;
using std::endl;
using std::mt19937_64;



int main(){

    mt19937_64 rng;
    rng.seed(std::random_device()()); // 1st pair of parentheses to activate random_device, 2nd pair to all random_device
    return 0;
}