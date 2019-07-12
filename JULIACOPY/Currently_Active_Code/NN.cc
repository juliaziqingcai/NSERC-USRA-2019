#include <iostream>
#include <vector>
#include <cmath>
#include <array>
#include <random>
#include <algorithm>
#include <fstream>
#include <string>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <set>
#include <utility>
using std::cin;
using std::cout;
using std::endl;
using std::mt19937_64;


/*
    Nearest-Neighbor Program based on a CCCG-2019 Paper:
    A Simple Randomized Algorithm for ALl Nearest Neighbors
    by Soroush Ebadian, Hamid Zarrabi-Zadeh

    Given a set P of n points in the plane, the all nearest neighbors
    problem asks for finding the closest poist in P for each point in the set.

    The algorithm presented works as follows:

    For each input point p in a set P = {p1, ..., pn}
        1. pick a random unit vector u (line)
        2. for i from 1
    


*/



struct point
{
    double x;
    double y;
    double x_prime;
    double y_prime;
    struct point* nn; //pointer only after sorting

};

template<typename RNG>
static void RPG(int64_t n, double upper_bound, double lower_bound, RNG& rng, std::vector<point *>& points)
{
    /*

    The Random Point Generator function generates an arbitrary n unique points
    stored into a vector. It starts off by creating pairs of (x,y) values in a set
    called coordinates to ensure no duplicates, and then puts them into the storage
    vector. It uses a Mersenne Prime Twister and a uniform real distribution to get
    coordinate values.

    */
    std::set<pair<double, double>> coordinates; //set made to check for duplicates
    std::uniform_real_distribution<double> dist(lower_bound, upper_bound);
    while(coordinates.size() < n){//fill the set
        std::pair<double, double> p;
        p = std::make_pair (dist(rng), dist(rng));
        coordinates.insert(p);
    }
    std::set<pair<double, double>>::iterator it = coordinates.begin();
    while( it != coordinates.end()){//must push into vector of actual point structs
        point p;
        p.x = (*it).first;
        p.y = (*it).second;
        point *ptr = &p;
        points.push_back(ptr);
    }

}

static int compar(const point *p1, const point *p2)//WARNING: MAY NOT WORK WITH POINT TYPE
/*
    The qsort() function requires the following function prototype:
        int compar (const void* p1, const void* p2)
    for the comparison function to be called.

    Return Value:       Meaning:
    -1                  p1 goes before p2
    0                   p1 = p2
    1                   p1 goes after p2

*/
{
    if ((*p1).x_prime < (*p2).x_prime)
        return -1;

    else
        return 1;
    
}

int main(){
    /*

    Main algorithm for A Simple Randomized Algorithm for All Nearest Neighbors

    */

    //ask user for range values 

    const double pi = std::acos(-1);

    double upper_bound, lower_bound; //upper/lower coordinate bounds
    int64_t n; // n = #points

    cout << "Number of points to generate(int): ";
    cin >> n;
    cout << "Coordinate upper bound(real): ";
    cin >> upper_bound;
    cout << "Coordinate lower bound(real): ";
    cin >> lower_bound;

    //set up RNG
    mt19937_64 rng;
    rng.seed(std::random_device()()); 
    // 1st pair of parentheses to activate random_device, 2nd pair to all random_device
    std::vector<point *> points; //vector of point struct pointers
    RPG(n, upper_bound, lower_bound, rng, points);

    std::uniform_real_distribution<double> dist(-pi/2, pi/2); //get random angle
    double angle = dist(rng);
    while(angle == (-pi/2))
        angle = dist(rng); //error-check against inclusive lower bound
    double a = tan(angle);

    for(auto p: points){ //must get NN for each p in input set
        (*p).x_prime = ((*p).x + (*p).y * a) / (a * a + 1);
        p.y_prime = p.x_prime * a;
    }

    qsort(points[0], n, sizeof(point), );
    // since qsort requires a function pointer as param
    // (*func_name) vs func_name

    return 0;
}
