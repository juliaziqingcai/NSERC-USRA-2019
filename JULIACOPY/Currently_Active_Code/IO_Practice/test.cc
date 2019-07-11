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
    std::string line;
    std::ofstream myfile;
    myfile.open("example.csv");
    myfile << "Writing this to a file.\n";
    std::ifstream file2("in.txt");
    if(file2.is_open()){
        while(getline(file2, line)){
            myfile << ", ";
            myfile << line;
            
            //myfile << "\n";
        }
        file2.close();
    }
    myfile.close();
    return 0;
}