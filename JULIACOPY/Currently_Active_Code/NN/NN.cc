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

        1.  Pick a random unit vector u (line) by picking a random angle
            to form a line y = tan(angle)x
        2.  Project the points onto the unit vector line,
            giving a projected point and an original point.
        3.  Sort/order the points in terms of their projected x-values
        4.  For each point in the set, check other points
            based on their projected distance to p while keeping
            the minimum found Euclidean distance relative to p.
        5.  The search for NN terminates if either all points have
            been checked, OR the algorithm encounters a Euclidean distance
            larger than the minimum found.



    New tools learned in the writing of this code:
        std::set, std::pair, std::sort customization, when to use auto vs. auto&, 
        difficulty of implementing qsort,


*/


static double get_value(char const *prompt)
/*
    Function for getting numerical input from user to modularize
    and reduce repetition.

*/
{
    double value;

    cout << "\n" << prompt;
    cin >> value;
    return value;
}


struct point
/*
    Represents a point on a plane. Contains the (x, y) coordinates of the
    original point, as well as the (x', y') coordinates for the projected
    point onto a random unit vector/line, and a pointer to the nearest
    point/neighbour (NN).
*/
{
    double x;
    double y;
    double x_prime;
    double y_prime;
    struct point *NN; //pointer only after sorting
    //NOTE: in C++, it's type *ptr, whereas in C, it's type* ptr
    bool operator() (point p1, point p2) {return (p1.x_prime < p2.x_prime); }
};


template<typename RNG>
static void get_angles(int64_t num_angles, std::set<double>& angles, RNG& rng)
/*
    Generates a given number of unique angles.
*/
{
    const double pi = std::acos(-1);

    std::uniform_real_distribution<double> dist(-pi/2, pi/2); //get random angle

    while(angles.size() < num_angles){
        double angle = dist(rng);
        while(angle == (-pi/2))
            angle = dist(rng); //error-check against inclusive lower bound
        angles.insert(angle);
    }
}


static bool compare (point p1, point p2)
/*
    Comparison function for std::sort() to rank points by their
    x_prime values. Returns a boolean indicating if p1 should go
    before/after p2 in the sorted vector.

    true(1) = p1 goes first
    false(0) = p2 goes first
*/
{
    return (p1.x_prime < p2.x_prime);
}


static double euclidean_distance(point p1, point p2)
//Calculates and returns the square of the euclidean distance between two points
{
    double diff_x = p1.x - p2.x;
    double diff_y = p1.y - p2.y;

    return (diff_x * diff_x) + (diff_y * diff_y);
}


static double projected_distance(point p1, point p2)
//Calculates and returns the square of the projected distance between two points
{
    double diff_x_prime = p1.x_prime - p2.x_prime;
    double diff_y_prime = p1.y_prime - p2.y_prime;

    return (diff_x_prime * diff_x_prime) + (diff_y_prime * diff_y_prime);
}


static void get_NN(int64_t n, std::vector<point>& points, int64_t i, int64_t& counter)
/*
    Walks through the sorted vector of points to find the Nearest Neighbour (NN)
    of the point at index i. Checks through all edge cases for travelling
    in either direction.

    n = # of total points
    points = vector of point pointers sorted by x_prime value
    i = index of point of interest in the vector
*/
{
    // STEP 1: INITIALIZE
    // left, right, & current are indices for the sorted projected points
       
    int64_t left = i-1;
    int64_t right = i+1;
    int64_t current;
    if (left == -1)
        current = right;
    else{ // case where left >= 0
        if (right == n)
            current = left;
        else{ // case where (left >= 0) AND (right <= n-1)
            if(projected_distance(points[i], points[left]) <= projected_distance(points[i], points[right]))
                current = left;
            else
                current = right;
        }
    }
    double min_euclidean_distance = std::numeric_limits<double>::max(); // D = big; in pseudo-code notes
    // INITIALIZATION ENDS


    // STEP 2: GIANT SYMMETRIC WHILE LOOP TO HANDLE EDGE CASES

    while( ( (left >= 0) || (right <= (n-1)) ) && (projected_distance(points[i], points[current]) <= min_euclidean_distance) ){

        ++counter;

        // CHECK & UPDATE NN

        if (euclidean_distance(points[i], points[current]) < min_euclidean_distance){
            points[i].NN = &(points[current]); 
            min_euclidean_distance = euclidean_distance(points[i], points[current]);
        }

        //SYMMETRIC CHECKS TO UPDATE LEFT/RIGHT

        if (current == left){// GO LEFT
            --left;
            if (left == -1)
                current = right;
            else{ // case where left >= 0
                if ( right == n)
                    current = left;
                else{ // case where (left >= 0) AND (right <= n-1)
                    if (projected_distance(points[i], points[left]) <= projected_distance(points[i], points[right]))
                        current = left;
                    else
                        current = right;
                }
            }
        }

        else{// GO RIGHT
            ++right;
            if (right == n)
                current = left;
            else{ // case where right <= n-1
                if (left == -1)
                    current = right;
                else{// case where (left >= 0) AND (right <= n-1)
                    if (projected_distance(points[i], points[left]) <= projected_distance(points[i], points[right]))
                        current = left;
                    else
                        current = right;
                }
            }
        }

    }

} // THE GIANT FOR LOOP ENDS



int main(){
    /*

    Main algorithm for A Simple Randomized Algorithm for All Nearest Neighbors

    */

    //ask user for range values 

    double upper_bound = get_value("Coordinate upper bound(real): ");
    double lower_bound = get_value("Coordinate lower bound(real): "); //upper/lower coordinate bounds
    int64_t n = (int64_t) std::round(get_value("Number of points to generate(int): ")); // n = #points
    int64_t num_angles = (int64_t) std::round(get_value("Number of angles to generate(int); "));

    cout << "\n\n ----RUN REPORT----\n";
    cout << "Coordinate Upper Bound: " << upper_bound << "\n";
    cout << "Coordinate Lower Bound: " << lower_bound << "\n";
    cout << "N                     : " << n << "\n";

    //set up RNG
    mt19937_64 rng;
    rng.seed(std::random_device()()); 
    // 1st pair of parentheses to activate random_device, 2nd pair to all random_device
    std::vector<point> points; //vector of point structs (less error-prone than pointers)

    //POINT GENERATION STARTS
    std::set<std::pair<double, double>> coordinates; //set made to check for duplicates

    /*
    // TEST COORDINATES N=8 (MAKE SURE TO ENTER 8 FOR N IN TERMINAL)
    std::pair<double, double> p1 = std::make_pair(4, 3);
    coordinates.insert(p1);

    std::pair<double, double> p2 = std::make_pair(8,0);
    coordinates.insert(p2);
    
    std::pair<double, double> p3 = std::make_pair(1,1);
    coordinates.insert(p3);

    std::pair<double, double> p4 = std::make_pair(3, 2);
    coordinates.insert(p4);

    std::pair<double, double> p5 = std::make_pair(0, 0);
    coordinates.insert(p5);

    std::pair<double, double> p6 = std::make_pair(9, 1);
    coordinates.insert(p6);

    std::pair<double, double> p7 = std::make_pair(1.5, 9);
    coordinates.insert(p7);

    std::pair<double, double> p8 = std::make_pair(0.5, 8);
    coordinates.insert(p8);*/

    
    
    std::uniform_real_distribution<double> dist(lower_bound, upper_bound);
    while(coordinates.size() < n){//fill the set
        std::pair<double, double> p;
        p = std::make_pair (dist(rng), dist(rng));
        coordinates.insert(p);
    }

    for(auto coor: coordinates){//put coordinates into points
        point p;
        p.x = coor.first;
        p.y = coor.second;
        points.push_back(p);
    }

    std::set<double> angles;//picked a set due to only needing the values
    get_angles(num_angles, angles, rng);

    for(auto angle: angles){
        
        double a = tan(angle); //random angle is y = tan(a)

        for(auto& p : points){
            //way to calculate prime coordinates based on equation of the line by simple algebra proof
            p.x_prime = (p.x + (p.y * a)) / ((a * a) + 1);
            p.y_prime = p.x_prime * a;
        }

        std::sort(points.begin(), points.end(), compare);//sort the points by x_prime values

        int64_t counter = 0;//counter to compare # of while loop iterationx to E[X]

        for(int64_t i = 0; i<n; ++i) // THE GIANT FOR LOOP OF DOOM BEGINS
            get_NN(n, points, i, counter);

        //cout << "\n------------------------------------------------------\n";

        /*
        for(auto p: points){
            cout << "\nCurrent Point is: (" << p.x << ", " << p.y << ") \n";
            cout << "NN Point is     : (" << (*(p.NN)).x << ", " << (*(p.NN)).y << ") \n";
        }*/

        //cout << "\nAngle used                      : " << angle << "\n";
        //cout << "Total # of While Loop Iterations: " << counter << "\n";
        //cout << "E[# of While Loop Iteractions]  : " << n * (std::sqrt(n)) << "\n";
        cout << "\n";
        cout << counter;

    }

    cout << "\n\n" << n* (std::sqrt(n)) << "\n";


    //TODO: Implement multiple angles for the same set of points (ask user for how many). Just a for loop with update primes and getNN calls
    //TODO: Update documentation & commenting & Makefile, the push to repo when completely done

    return 0;
}
