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
    (MODIFIED BOX VERSION) 
    Nearest-Neighbor Program based on a CCCG-2019 Paper:
    A Simple Randomized Algorithm for ALl Nearest Neighbors
    by Soroush Ebadian, Hamid Zarrabi-Zadeh

    Given a set P of n points in the plane, the all nearest neighbors
    problem asks for finding the closest poist in P for each point in the set.


    MODIFICATION TO ORIGINAL:

        The points must generated in boxes, with the condition that the
        NN of all the points within each box is also within the same box
        (distance between boxes > diagonal of boxes).

        The purpose is to test if this searching takes longer (more while
        loop iterations) than the E[x] = n * sqrt(n) due to some random
        lines causing all the projected points to fall very close
        together (eg. boxes arranged vertically with a hozontal line chosen).
        Theoretically, all the points would then have to be walked along due
        to the box constraints AND the closeness of the projected points.

        -Coordinate bounds are no longer asked for, as they are generated as
        [0, 3i) (lower left corner) to [1, 3i+1) (upper right corner)
        -Asks for number of boxes


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
        difficulty of implementing qsort, be careful of logic errors,
        managed to cause a double-free seg fault core dump by corrupting
        memory from overwriting and referencing non-existent data

    
    Things Learned from Box Experiment:

        The higher and narrower and more boxes we stack vertically, the closer to
        true horizontal angles we have to get in order to get many while loop iteration.
        This means that most angles are 'good' and can execute in much less time than
        the expected value, BUT when it does get a 'bad' angle (this range narrows the 
        higher we stack boxes, i.e. more boxes) the execution takes much, MUCH longer
        (# while loop iterations >>>> E[x]). This makes sense since projecting onto
        any random line will produce large distance differences for higher box stacks,
        so we have to check less neighbors (sometimes only the nearest!).


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
    point *NN; //pointer only after sorting
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


static void get_NN(std::vector<point>& points, int64_t i, int64_t& counter)
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
    size_t n = points.size();
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

    const double pi = std::acos(-1);

    //ask user for range values 

    int64_t num_boxes = 1000;
    int64_t points_per_box = (int64_t) std::round(get_value("Number of points per box to generate(int): ")); 
    int64_t num_angles = (int64_t) std::round(get_value("Number of angles to generate(int): "));
    int64_t n = num_boxes * points_per_box;

    //FIXED (CONSTANT) X-COORDINATE BOX BOUNDS
    double x_lower_bound = 0;
    double x_upper_bound = 0.01;

    cout << "\n\n ----RUN REPORT----\n";
    cout << "Number of Boxes : " << num_boxes << "\n";
    cout << "Points per box  : " << points_per_box << "\n";
    cout << "Number of Angles: " << num_angles << "\n";
    cout << "N               : " << n << "\n";
    cout << "E[# while loops]: " << n* std::sqrt(n) << "\n";
    
    
    mt19937_64 rng;
    rng.seed(std::random_device()()); 

    //POINT GENERATION STARTS

    std::set<std::pair<double, double>> coordinates; //set made to check for duplicates
    
    for(int64_t i=0; i<num_boxes; ++i){

        // SET Y-COORDINATE BOX BOUNDS TO ENSURE DISTANCE OUTSIDE BOXES > DISTANCE INSIDE BOXES
        double y_lower_bound = 3 * i;
        double y_upper_bound = (3 * i) + 0.01; 

        // SEPARATE DISTRIBUTIONS TO GENERATE X, Y VALUES
        std::uniform_real_distribution<double> get_x(x_lower_bound, x_upper_bound);
        std::uniform_real_distribution<double> get_y(y_lower_bound, y_upper_bound);

        while(coordinates.size() < ((i+1) * (points_per_box)))
        //LARGE ERROR HERE BEFORE FROM NOT CONSIDERING HOW TO UPDATE UPPER SIZE BOUND WITH EACH NEW BOX
        //DIFFERENT FROM SINGLE BOX VERSION BY A LOTTTT
        //ALSO THE SOURCE OF A DOUBLE FREE ERROR! ACHIEVEMENT!!
            coordinates.insert(std::make_pair(get_x(rng), get_y(rng)));

        //cout << "\nNumber of current coordinates generated: " << coordinates.size() << "\n";
        
    }

    std::vector<point> points;
    for(auto coor: coordinates){
        point p;
        p.x = coor.first;
        p.y = coor.second;
        p.NN = nullptr;
        points.push_back(p);
    
    }
    //cout << "Number of current points generated: " << points.size() << "\n";


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
            get_NN(points, i, counter);

        cout << "\n------------------------------------------------------\n";
        /*
        for(auto p: points){
            cout << "\nCurrent Point is: (" << p.x << ", " << p.y << ") \n";
            cout << "NN Point is     : (" << (*(p.NN)).x << ", " << (*(p.NN)).y << ") \n";
        }*/

        //cout << "\nAngle used                      : " << angle << "\n";
        //cout << "Total # of While Loop Iterations: " << counter << "\n";
        //cout << "E[# of While Loop Iteractions]  : " << n * (std::sqrt(n)) << "\n";

        cout << "\nAngle used      : " << (angle * 180 / pi) << "\n";
        cout << "Counter         : " << counter << "\n";

        /*
        //USED FOR TERMINAL TESTING
        cout << "\n";
        cout << counter;*/

    }

    //cout << "\n\n" << n* (std::sqrt(n)) << "\n";

    return 0;
}