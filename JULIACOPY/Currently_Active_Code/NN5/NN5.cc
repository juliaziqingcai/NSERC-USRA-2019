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
#include <tuple>
#include <eigen3/Eigen/Core> // Eigen library version 3, light core version
using std::cin;
using std::cout;
using std::endl;
using std::mt19937_64;
using std::cos;
using std::sin;

//partial fixes for up to n=100
#define EIGEN_DONT_VECTORIZE 
#define EIGEN_DISABLE_UNALIGHNED_ARRAY_ASSERT


/*
    (MODIFIED 4D CONJECTURE VERSION)
    Nearest-Neighbor Program based on a CCCG-2019 Paper:
    A Simple Randomized Algorithm for ALl Nearest Neighbors
    by Soroush Ebadian, Hamid Zarrabi-Zadeh

    Given a set P of n points in the plane, the all nearest neighbors
    problem asks for finding the closest poist in P for each point in the set.

    Credits of the Eigen C++ Library application go to Luis Fernando Schultz Xavier da Silveira (PhD)


    MODIFICATION TO ORIGINAL:   

        In this version, it is a tester to see the effects of delta and n^(7/4)
        in 4D. It includes the capability to generate multiple point sets, 
        each which will have a number of angles generated. This allows for 
        an average while loop counter to be output and there is also an average 
        delta output. This program is best run with

            time /tmp/NN4 >> results.ods

        Make sure to look at the hard-coded N values.


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

        -By default libraries are installed in /usr/lib and
        header files will be in /usr/include

        -How to implement a matrix multiplcation function

        -Introduction to the Eigen library for C++, very powerful for
        matrix manipulation. It is overloaded for linear-algebraic operations,
        with regular arithmetic operators and special ones (such as dot(), cros(), << , etc.)
        View the Eigen Tutorial PDF in the PDFs directory

        -Must install eigen library to use on Ubuntu (do this in the
        /usr/include directory):

            sud apt install libeigen3-dev
        
        -How to check for location of installed library:

            dpkg -L packagename (WARNING: Only works for packed installed by dpkg)
        
        -How to check for all packages available by dpkg:

            dpkg --get-selections | grep <packagename>
        
        -How to check for available libraries by apt:

            apt-cache search . 
            apt-cache search keyword


    Debugging:

        -In Ubuntu 16.04, the Eigen library can be fragile with memory
        and matrix alignment issues. The 2 fixes to this are as follows:

        1) Use the macros #define EIGEN_DONT_VECTORIZE and
        #define EIGEN_DISABLE_UNALIGHNED_ARRAY_ASSERT in the program to
        correctly align all matrices and vectors. Even if your issue is not
        directly related to this, it is a good precaution to take. The only 
        issue is you want the absolute maximum performance out of the program.
        This solution will slightly decrease the speed of the program for
        highly complex computations, but for the purposes of NN4, the effect
        is completely negligible and unnoticeable.

        2) Where an STL container type (std::vector, std::map, etc.) 
        is used in the code, include an Eigen::aligned_allocator as a
        parameter. 

        ex. std::vector<T> name; => std::vector<T, Eigen::aligned_allocator<T>> name;


    THINGS LEARNED AFTER TESTING:

        After much testing, it seems that the average while loop counter
        DOES NOT depend on delta. The constant in front of the n^(7/3) seems to be

            c = 1.158 - 1.167
        
        The testing included values of N from 1k all the way up to 500k.

        It also seems that as N gets larger, the ratio gets smaller, which makes
        sense as the bounds for generating point values are confined and there are
        more points in the sam space. The delta also increases, which makes
        sense due to some points becoming arbitrarily close to one another while
        the largest distance remains sort of constant.

        In comparison to the 3D version (NN4), the ratios and delta are larger in 
        NN5 (4D) since there is an extra dimension along which to generate
        unique point values.


*/


struct point
/*
    Represents a point in 4D. Contains the (x, y, z, u) coordinates of the
    original point, as well as the (x', y', z', u') coordinates for the projected
    point onto a random unit vector/plane, and a pointer to the nearest
    point/neighbour (NN).
*/
{
    Eigen::Matrix<double, 4, 1> coords; // Make a matrix of doubles, 4 by 1
    Eigen::Matrix<double, 4, 1> coords_prime;
    struct point *NN; //pointer only after sorting
    //NOTE: in C++, it's type *ptr, whereas in C, it's type* ptr
    bool operator() (point const& p1, point const& p2) {return (p1.coords_prime(0, 0) < p2.coords_prime(0, 0)); }
};


typedef std::tuple<double, double, double, double, double, double> Angles; 
//Struct to represent collection of 6 random angles around which to rotate


template<typename RNG>
static void get_angles(int64_t num_angles, std::set<Angles>& angles, RNG& rng)
/*
    Generates a given number of unique angles.
*/
{
    const double pi = std::acos(-1);

    std::uniform_real_distribution<double> dist(-pi/2, pi/2); //get random angle

    while(angles.size() < num_angles){

        auto angle = std::make_tuple(dist(rng), dist(rng), dist(rng),dist(rng), dist(rng), dist(rng));

        while(std::get<0>(angle) == (-pi/2))
            std::get<0>(angle) = dist(rng);//error-check against inclusive lower bound
        while(std::get<1>(angle) == (-pi/2))
            std::get<1>(angle) = dist(rng);
        while(std::get<2>(angle) == (-pi/2))
            std::get<2>(angle) = dist(rng);
        while(std::get<3>(angle) == (-pi/2))
            std::get<3>(angle) = dist(rng);
        while(std::get<4>(angle) == (-pi/2))
            std::get<4>(angle) = dist(rng);
        while(std::get<5>(angle) == (-pi/2))
            std::get<5>(angle) = dist(rng);

        angles.insert(angle);
    }
}


static void rotate(Angles const& angle, std::vector<point, Eigen::aligned_allocator<point>>& points)
/*
    Rotates all points based in 4D
*/
{
    double a = std::get<0>(angle);
    double b = std::get<1>(angle);
    double c = std::get<2>(angle);
    double d = std::get<3>(angle);
    double e = std::get<4>(angle);
    double f = std::get<5>(angle);

    Eigen::Matrix<double, 4, 4> A, B, C, D, E, F;

    A << //Comma initializer syntax for matrices, can directly output matrix A with std::cout
    //Can also use << operator to fill block expressions
        cos(a), sin(a), 0, 0,
        -sin(a), cos(a), 0, 0,
        0, 0, 1, 0, 
        0, 0, 0, 1;

    B <<
        1, 0, 0, 0,
        0, cos(b), sin(b), 0,
        0, -sin(b), cos(b), 0,
        0, 0, 0, 1;

    C <<
        cos(c), 0, -sin(c), 0,
        0, 1, 0, 0,
        sin(c), 0, cos(c), 0,
        0, 0, 0, 1;

    D <<
        cos(d), 0, 0, sin(d),
        0, 1, 0, 0,
        0, 0, 1, 0,
        -sin(d), 0, 0, cos(d);

    E <<
        1, 0, 0, 0,
        0, cos(e), 0, -sin(e),
        0, 0, 1, 0,
        0, sin(e), 0, cos(e);

    F <<
        1, 0, 0, 0,
        0, 1, 0, 0,
        0, 0, cos(f), -sin(f),
        0, 0, sin(f), cos(f);
    
    auto M = A * B * C * D * E * F; //Look at this elegance

    for (auto& p: points)
        p.coords = M * p.coords; //matrix multiplication through overloaded Eigen library operator
}


static bool compare (point const& p1, point const& p2)
/*
    Comparison function for std::sort() to rank points by their
    x_prime values. Returns a boolean indicating if p1 should go
    before/after p2 in the sorted vector.

    true(1) = p1 goes first
    false(0) = p2 goes first
*/
{
    return (p1.coords_prime[0] < p2.coords_prime[0]); 
    //access elements through subscript operator, ONLY works because 
    //it is effectively a vector, use (row, col) syntax for regular matrices
}


static double euclidean_distance_squared(point const& p1, point const& p2)
//Calculates and returns the square of the euclidean distance between two points
{
    auto d = p2.coords - p1.coords;
    return d.transpose()*d; //special transpose() function for a matrix
}


static double projected_distance_squared(point const& p1, point const& p2)
//Calculates and returns the square of the projected distance between two points
{
    auto d = p2.coords_prime - p1.coords_prime;
    return d.transpose()*d;
}


static void get_NN(int64_t n, std::vector<point, Eigen::aligned_allocator<point>>& points, int64_t i, int64_t& counter)
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
            if(projected_distance_squared(points[i], points[left]) <= projected_distance_squared(points[i], points[right]))
                current = left;
            else
                current = right;
        }
    }
    double min_euclidean_distance = std::numeric_limits<double>::max(); // D = big; in pseudo-code notes
    // INITIALIZATION ENDS


    // STEP 2: GIANT SYMMETRIC WHILE LOOP TO HANDLE EDGE CASES

    while( ( (left >= 0) || (right <= (n-1)) ) && (projected_distance_squared(points[i], points[current]) <= min_euclidean_distance) ){

        ++counter;

        // CHECK & UPDATE NN

        if (euclidean_distance_squared(points[i], points[current]) < min_euclidean_distance){
            points[i].NN = &(points[current]); 
            min_euclidean_distance = euclidean_distance_squared(points[i], points[current]);
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
                    if (projected_distance_squared(points[i], points[left]) <= projected_distance_squared(points[i], points[right]))
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
                    if (projected_distance_squared(points[i], points[left]) <= projected_distance_squared(points[i], points[right]))
                        current = left;
                    else
                        current = right;
                }
            }
        }

    }

} // THE GIANT FOR LOOP ENDS


static double algorithm(double upper_bound, double lower_bound, int64_t n, int64_t num_angles, double& delta_sum)
/*
    One run of the overall NN algorithm for one generated point set.
*/
{
    //set up RNG
    mt19937_64 rng;
    rng.seed(std::random_device()()); 
    // 1st pair of parentheses to activate random_device, 2nd pair to all random_device
    std::vector<point, Eigen::aligned_allocator<point>> points; //,Eigen::aligned_allocator<point>> points; //vector of point structs (less error-prone than pointers)

    //POINT GENERATION STARTS
    std::set<std::tuple<double, double, double, double>> coordinates; //set made to check for duplicates

    /*
    // TEST COORDINATES N=8 (MAKE SURE TO ENTER 8 FOR N IN TERMINAL)
    std::tuple<double, double, double, double> p1 = std::make_tuple(4, 3, 0,0);
    coordinates.insert(p1);

    std::tuple<double, double, double, double> p2 = std::make_tuple(8,0,0,0);
    coordinates.insert(p2);
    
    std::tuple<double, double, double, double> p3 = std::make_tuple(1,1,0,0);
    coordinates.insert(p3);

    std::tuple<double, double, double, double> p4 = std::make_tuple(3, 2, 0,0);
    coordinates.insert(p4);

    std::tuple<double, double, double, double> p5 = std::make_tuple(0, 0, 0,0);
    coordinates.insert(p5);

    std::tuple<double, double, double, double> p6 = std::make_tuple(9, 1, 0,0);
    coordinates.insert(p6);

    std::tuple<double, double, double, double> p7 = std::make_tuple(1.5, 9, 0,0);
    coordinates.insert(p7);

    std::tuple<double, double, double, double> p8 = std::make_tuple(0.5, 8, 0,0);
    coordinates.insert(p8);*/
    
    
    std::uniform_real_distribution<double> dist(lower_bound, upper_bound);
    while(coordinates.size() < n)//fill the set
        coordinates.insert(std::make_tuple(dist(rng), dist(rng), dist(rng), dist(rng)));
        
    //cout << "Flag 01" << endl;
    for(auto coor: coordinates){//put coordinates into points
        point p;
        p.coords << std::get<0>(coor), std::get<1>(coor), std::get<2>(coor), std::get<3>(coor);
        points.push_back(p);
    }
    
    std::set<std::tuple<double, double, double, double, double, double>> angles;//picked a set due to only needing the values
    get_angles(num_angles, angles, rng);

    int64_t sum = 0;

    for(auto angle: angles){

        rotate(angle, points);
        
        for(auto& p : points){ //projecting onto the x-axis after some arbitrary rotations
            //way to calculate prime coordinates based on equation of the line by simple algebra proof
            p.coords_prime << p.coords(0, 0), 0, 0, 0;
        }

        std::sort(points.begin(), points.end(), compare);//sort the points by x_prime values

        int64_t counter = 0;//counter to compare # of while loop iterationx to E[X]

        for(int64_t i = 0; i<n; ++i) // THE GIANT FOR LOOP OF DOOM BEGINS
            get_NN(n, points, i, counter);
        
        /*
        cout << "\n======================================================\n";
        
        for(auto p: points){
            cout << "Current Point is: \n" << p.coords << "\n" << endl;
            cout << "NN is: \n" << p.NN->coords;
            cout << "\n------------------------------------------------------\n";
        }

        cout << "\nAngle used : " << "(" << std::get<0>(angle) << ", " << std::get<1>(angle) << ", " << std::get<2>(angle) << ", "
            << std::get<3>(angle) << ", " << std::get<4>(angle) << ", " << std::get<5>(angle) << ")\n";*/
        //cout << "\nTotal # of While Loop Iterations: " << counter << "\n";
        //cout << "E[# of While Loop Iteractions]  : " << std::cbrt(n * n * n * n * n) << "\n";
        //cout << "\nCounter : " << counter;
        sum += counter;
    }
    
    double min_nn_distance = std::numeric_limits<double>::max();
    double max_nn_distance = 0;

    for (int64_t i=0; i< points.size(); ++i ){
        if(euclidean_distance_squared (points[i], *((points[i]).NN)) < min_nn_distance)
            min_nn_distance = euclidean_distance_squared(points[i], *((points[i]).NN));
        if(euclidean_distance_squared (points[i], *((points[i]).NN)) > max_nn_distance)
            max_nn_distance = euclidean_distance_squared(points[i], *((points[i]).NN));
    }

    double delta = std::sqrt((max_nn_distance / min_nn_distance));
    delta_sum += delta;

    //cout << "\n\nDelta = " << delta << "\n";

    //cout << "\n\nE[# of while loop iterations] = " << std::cbrt(n * n * n * n) << "\n" ;//* std::pow((std::log(delta)), 2 ) << "\n";
    //cout << "Actual Average Counter =        " << (sum/angles.size());
    //cout << "\nRatio of E[x] to Actual =       " << (std::cbrt(n * n * n * n)) / (sum/angles.size()) << "\n";//* std::pow((std::log(delta)), 2)) / (sum/angles.size());

    return (sum/angles.size());
}



int main(){
    /*

    Main algorithm for A Simple Randomized Algorithm for All Nearest Neighbors
    Conjecture Testing in 4D

    */

    double upper_bound = 1;
    double lower_bound = 0; //upper/lower coordinate bounds

    //int64_t n_array[1] = {740};
    //int64_t n_array[1] = {40};
    //int64_t n_array[6] = {1000, 2000, 3000, 4000, 5000, 6000};
    //int64_t n = 100000;
    //cout << "\nNumber of points to generate(int): "; // n = #points
    //cin >> n;
    //int64_t n = 1000;

    int64_t n_array[5];

    for (int i=1; i<6; ++i)
        n_array[i-1] = i * 100000;//100000;

    int64_t num_angles = 10;
    //cout << "\nNumber of angles to generate(int): ";
    //cin >> num_angles;
    int64_t num_sets = 25;
    //cout << "\nNumber of point sets to generate(int): ";
    //cin >> num_sets;

    for(auto n: n_array){
        cout << "\n\n ----RUN REPORT----\n";
        cout << "N                     : " << n << "\n";

        double overall_sum = 0;
        double delta_sum = 0;
        
        for(int64_t i = 0; i<num_sets; ++i)
            overall_sum += algorithm(upper_bound, lower_bound, n, num_angles, delta_sum);
        
        cout << "\n Overall average: "; 
        cout << "\n" << overall_sum/num_sets;
        cout << "\n Overall Delta: ";
        cout << "\n" << delta_sum/num_sets; 
        }


    return 0;
}
