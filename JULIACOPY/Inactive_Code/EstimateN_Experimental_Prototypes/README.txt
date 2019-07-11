README:		For all files related to the development and search for an
		algorithm that could reliably approximate set size
		only through duplicate confirmation sampling with replacement.
		They are all prototypes and only meant to show the journey to
		the files in the EstimateN directory.
		NOT MEANT TO BE RUN AS DEPENDENT FILES HAVE CHANGED.
		READ ONLY

AUTHORS:	Julia Cai, ALexa de Grandmont

LAST UPDATE:	July 11th, 2019

LANGUAGE:	PYTHON
VERSION:	3 and above

ISSUES:		1) Python2 causes float division to become integer division
		2) Python2 causes the terminal input to require quotation marks
			around user input or else it will cause a runtime error
		3) Python3/Ubuntu/Something/??? doesn't like having to import and
			use modules with '+' in the module/program/file name; causes
			syntax error during runtime
		4) BE CAREFUL of algorithm names, especially as new files get added to this
			folder from the Currently Active Code directory, since names may have
			been altered for clarity and multiple implementations, so old programs 
			may not immediately work.


----------------------------------------FILES--------------------------------------------------	

EstimateN_Experimental_Prototypes Directory:
	Contains:

	Approximating_N_With_Average_Counter.py: 
		Algorithm for approximating set size with duplicate confirmation sampling

	Approximating_N_With_Average_Counter_Test.py:
		A tester for the file immeditely above

	Approximating_N_With_2kPlus1_Samples.py:
		Gets an approximate n after 2k+1 runs of the duplicate confirmation sampling algorithm

	Approximating_N_With_Median_Counter.py:			
		Approximates a set size by returning the median of 2k+1 samples

	Comparing_Counter_To_Expected_Value.py:	
		Compares the actual returned counter value to the expected value of the counter using
		Sample Until Duplicate 

	Gradual_Buildup_Multiprocessing:
		File for learning the multiprocessing module

	May_14th_Luis_Homework.py:
		Luis' attempt to approximate the set size on May 14th, 2019

	Median_Counter_Vs_Average_Counter_Approximated_Ns.py:	
		Compares whether approximating the set size with the median counter OR the average counter 
		is more accurate

	Median_Of_Medians_Vs_Median_Of_Samples.py:
		Compares which method of obtaining the median is more accurate

	Modified_German_Tank_Problem.py:
		Algorithm and tester for our version of the German Tank Problem (we use the full set, with replacement)

	Multiprocess_Approximated_N.py:	
		A multiprocess version of the algorithm for approximating n with duplicate confirmation sampling.

	Multiprocess_Approximated_N_Test.py:
		A tester for the file immeditely above

	Multiprocessing_Practice.py:
		Practice file for the module

	Multiprocess_Number_Doubler:
		File to test multiprocessing using the Process class with a simple number doubler function.

	Multithreading_Practice01.py:
		Practice file for the module

	NewApproxN.py:
		Testing different methods and their ks. BASED ON A COMPLETE MISUNDERSTANDING OF INSTRUCTIONS
		DUE TO NAMING VARIABLES SAME NAME IN EXPLANATION FROM MICHIEL

	Not_In_Green_Interval_Bound_Inequality.py:
		Tests if the upper-bound for the probability that the approximated set size is NOT within the 
		acceptable interval (green) holds

	-README.txt:
		File gives a quick overview of directory contents.

	Subprocess_Practice.py:
		A file for learning and practicing the module.

