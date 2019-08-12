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
using std::cin;
using std::cout;
using std::endl;
using std::mt19937_64;
using std::cos;
using std::sin;


/*
    (MODIFIED 3D CONJECTURE TESTING VERSION)
    Nearest-Neighbor Program based on a CCCG-2019 Paper:
    A Simple Randomized Algorithm for ALl Nearest Neighbors
    by Soroush Ebadian, Hamid Zarrabi-Zadeh

    Given a set P of n points in the plane, the all nearest neighbors
    problem asks for finding the closest poist in P for each point in the set.


    MODIFICATION TO ORIGINAL:   

        In this version, it is a tester to see the effects of delta and n^(5/3)
        as an extension to the regular 3D version (NN3). It includes the capability
        to generate multiple point sets, each which will have a number of angles
        generated. This allows for an average while loop counter to be output
        and there is also an average delta output. This program is best run with

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

        

    THINGS LEARNED AFTER TESTING:

        After much testing, it seems that the average while loop counter
        DOES NOT depend on delta. The constant in front of the n^(5/3) seems to be

            c = 1.0465
        
        from ~2.8 days of testing results, which can be found in the file
        results_compilation.ods. This test used 12 different N values, 
        generated 25 point sets for each N, and generated 10 angles per
        set.

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
    Represents a point in 3D. Contains the (x, y, z) coordinates of the
    original point, as well as the (x', y', z') coordinates for the projected
    point onto a random unit vector/plane, and a pointer to the nearest
    point/neighbour (NN).
*/
{
    double x;
    double y;
    double z;
    double x_prime;
    double y_prime;
    double z_prime;
    struct point *NN; //pointer only after sorting
    //NOTE: in C++, it's type *ptr, whereas in C, it's type* ptr
    bool operator() (point p1, point p2) {return (p1.x_prime < p2.x_prime); }
};


template<typename RNG>
static void get_angles(int64_t num_angles, std::set<std::tuple<double, double, double>>& angles, RNG& rng)
/*
    Generates a given number of unique angles.
*/
{
    const double pi = std::acos(-1);

    std::uniform_real_distribution<double> dist(-pi/2, pi/2); //get random angle

    while(angles.size() < num_angles){

        std::tuple<double, double, double> angle = std::make_tuple(dist(rng), dist(rng), dist(rng));

        while(std::get<0>(angle) == (-pi/2))
            std::get<0>(angle) = dist(rng);//error-check against inclusive lower bound
        while(std::get<1>(angle) == (-pi/2))
            std::get<1>(angle) = dist(rng);
        while(std::get<2>(angle) == (-pi/2))
            std::get<2>(angle) = dist(rng);

        angles.insert(angle);
    }
}


static void rotate(std::tuple<double, double, double> angle, std::vector<point>& points)
/*
    Rotates all points based on 3 arbitrary angles
*/
{
    double a = std::get<0>(angle);
    double b = std::get<1>(angle);
    double c = std::get<2>(angle);

    for (auto& p: points){
        double x = p.x;
        double y = p.y;
        double z = p.z;

        double xx = cos(b) * cos(c);
        double xy = (-cos(b)) * sin(c);
        double xz = sin(b);

        double yx = (sin(a) * sin(b) * cos(c)) + (cos(a) * sin(c));
        double yy = ((-sin(a)) * sin(b) * sin(c)) + (cos(a) * cos(c));
        double yz = (-sin(a)) * cos(b);

        double zx = ((-cos(a)) * sin(b) * cos(c)) + (sin(a) * sin(c));
        double zy = (cos(a) * sin(b) * sin(c)) + (sin(a) * cos(c));
        double zz = cos(a) * cos(b);

        p.x = xx * x + xy * y + xz * z;
        p.y = yx * x + yy * y + yz * z;
        p.z = zx * x + zy * y + zz * z;
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
    double diff_z = p1.z - p2.z;

    return (diff_x * diff_x) + (diff_y * diff_y) + (diff_z * diff_z);
}


static double projected_distance(point p1, point p2)
//Calculates and returns the square of the projected distance between two points
{
    double diff_x_prime = p1.x_prime - p2.x_prime;
    double diff_y_prime = p1.y_prime - p2.y_prime;
    double diff_z_prime = p1.z_prime - p2.z_prime;

    return (diff_x_prime * diff_x_prime) + (diff_y_prime * diff_y_prime) + (diff_z_prime * diff_z_prime);
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


static double algorithm(double upper_bound, double lower_bound, int64_t n, int64_t num_angles, double& delta_sum)
/*
    One run of the overall NN algorithm for one generated point set.
*/
{
    //set up RNG
    mt19937_64 rng;
    rng.seed(std::random_device()()); 
    // 1st pair of parentheses to activate random_device, 2nd pair to all random_device
    std::vector<point> points; //vector of point structs (less error-prone than pointers)

    //POINT GENERATION STARTS
    std::set<std::tuple<double, double, double>> coordinates; //set made to check for duplicates

    /*
    // TEST COORDINATES N=8 (MAKE SURE TO ENTER 8 FOR N IN TERMINAL)
    std::tuple<double, double, double> p1 = std::make_tuple(4, 3, 0);
    coordinates.insert(p1);

    std::tuple<double, double, double> p2 = std::make_tuple(8,0,0);
    coordinates.insert(p2);
    
    std::tuple<double, double, double> p3 = std::make_tuple(1,1,0);
    coordinates.insert(p3);

    std::tuple<double, double, double> p4 = std::make_tuple(3, 2, 0);
    coordinates.insert(p4);

    std::tuple<double, double, double> p5 = std::make_tuple(0, 0, 0);
    coordinates.insert(p5);

    std::tuple<double, double, double> p6 = std::make_tuple(9, 1, 0);
    coordinates.insert(p6);

    std::tuple<double, double, double> p7 = std::make_tuple(1.5, 9, 0);
    coordinates.insert(p7);

    std::tuple<double, double, double> p8 = std::make_tuple(0.5, 8, 0);
    coordinates.insert(p8);*/

    
    
    std::uniform_real_distribution<double> dist(lower_bound, upper_bound);
    while(coordinates.size() < n)//fill the set
        coordinates.insert(std::make_tuple(dist(rng), dist(rng), dist(rng)));
        

    for(auto coor: coordinates){//put coordinates into points
        point p;
        p.x = std::get<0>(coor);
        p.y = std::get<1>(coor);
        p.z = std::get<2>(coor);
        points.push_back(p);
    }
    
    std::set<std::tuple<double, double, double>> angles;//picked a set due to only needing the values
    get_angles(num_angles, angles, rng);

    int64_t sum = 0;

    for(auto angle: angles){

        rotate(angle, points);
        

        for(auto& p : points){ //projecting onto the x-axis after some arbitrary rotations
            //way to calculate prime coordinates based on equation of the line by simple algebra proof
            p.x_prime = p.x;
            p.y_prime = 0;
            p.z_prime = 0;
        }

        std::sort(points.begin(), points.end(), compare);//sort the points by x_prime values

        int64_t counter = 0;//counter to compare # of while loop iterationx to E[X]


        for(int64_t i = 0; i<n; ++i) // THE GIANT FOR LOOP OF DOOM BEGINS
            get_NN(n, points, i, counter);
        
        
        //cout << "\n------------------------------------------------------\n";

        /*
        for(auto p: points){
            cout << "\nCurrent Point is: (" << p.x << ", " << p.y << ", " << p.z << ") \n";
            cout << "NN Point is     : (" << (*(p.NN)).x << ", " << (*(p.NN)).y << ", " << (*(p.NN)).z <<") \n";
        }*/

        //cout << "\nAngle used                      : " << angle << "\n";
        //cout << "\nTotal # of While Loop Iterations: " << counter << "\n";
        //cout << "E[# of While Loop Iteractions]  : " << std::cbrt(n * n * n * n * n) << "\n";
        //cout << "\nCounter : " << counter;
        sum += counter;
    }
    
    double min_nn_distance = std::numeric_limits<double>::max();  ; 
    double max_nn_distance = 0;

    for (int64_t i=0; i< points.size(); ++i ){
        if(euclidean_distance (points[i], *((points[i]).NN)) < min_nn_distance)
            min_nn_distance = euclidean_distance(points[i], *((points[i]).NN));
        if(euclidean_distance (points[i], *((points[i]).NN)) > max_nn_distance)
            max_nn_distance = euclidean_distance(points[i], *((points[i]).NN));
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
    Conjecture Testing in 3D

    */

    double upper_bound = 1;
    double lower_bound = 0; //upper/lower coordinate bounds

    //int64_t n;

    //int64_t n_array[6] = {1000000,2000000, 3000000, 4000000, 5000000, 6000000};
    int64_t n_array[12];

    for (int i=1; i<11; ++i)
        n_array[i-1] = i * 100000;
    
    n_array[10] = 1500000;
    n_array[11] = 2000000;
    //cout << "\nNumber of points to generate(int): "; // n = #points
    //cin >> n;

    int64_t num_angles = 10;
    //cout << "\nNumber of angles to generate(int): ";
    //cin >> num_angles;
    int64_t num_sets = 25;
    //cout << "\nNumber of point sets to generate(int): ";
    //cin >> num_sets;

    for(auto n: n_array){
        cout << "\n\n ----RUN REPORT----\n";
        //cout << "Coordinate Upper Bound: " << upper_bound << "\n";
        //cout << "Coordinate Lower Bound: " << lower_bound << "\n";
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
