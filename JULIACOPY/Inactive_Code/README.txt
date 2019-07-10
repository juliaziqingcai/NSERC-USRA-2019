README:		For all currently in-active (not in use OR not of interest at the moment)
		Summer 2019 NSERC-USRA Folder Program files

AUTHORS:	Julia Cai, ALexa de Grandmont

LAST UPDATE:	June 12th, 2019

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

Coupon_Collector Directory:
	Contains:

	C1 Directory:
		Contains:

		-Makefile:
			The Makfile for the C1.cc file. Options chosen for max optimization of
			program perfomance.

		-C1.cc:
			An extension of the N1 and N2 estimating-n programs. The C series
			is our version of the coupon collector's problem, based on our
			approximations of n. C1 is the normal, single run program. 


	C2 Directory:
		Contains:

		-Makefile:
			The Makfile for the C2.cc file. Options chosen for max optimization of
					program perfomance.
		-C2.cc:
			A multiple-run tester version of the C1.cc program directly above.
			Best used in conjunction with Linux file redirection commands for
			testing purposes, as no C++ file i/o has been directly implemented
			into the code.

		-in.txt:
			The intake file for C1.cc


EstimateN Directory:
	Contains:

	Best_K_Test_Results.ods:
		Spreadsheet containing all test results from Binary Search for a Best K

	Binary_Search_Best_K.py:
		Searches for a k lower than a theoretical upper bound through Binary Search. 
		Contains many overnight test runs

	EstimateN.py:
		The culmination of all our work during the six weeks from May 1, 2019
		to June 10 2019. The function NewEstimateN is the final and most correct
		base version (no speed upgrades) of our algorithm to approximate n
		with only confirmation sampling. 

	N1 Directory:
		Contains:

		-Makefile:
			The Makfile for the N1.cc file. Options chosen for max optimization of
			program perfomance.

		-N1.cc:
			The C++ version of EstimateN.py, ported over for perfomance gains.
			This will run 125 times faster than the Python file.
			Should be run with the time command in terminal to really compare
			performance, with the following commands:
				make
				time /tmp/N1

		-N1_Commented.cc:
			A commented version of the file directly above sharing the same name.
			Since Luis created the upgrades to the original algorithm and
			introduced many new tricks from C++11, there was much learning to be done,
			which is shown in this file with lots of comments. This is a separate
			file intended for learning purposes about both N1.cc and the options
			used in the Makefile. It is not intended to run in any way shape or form.


	N2 Directory:
		Contains:
	
		-Makefile:
			The Makfile for the N1.cc file. Options chosen for max optimization of
			program perfomance.
	
		-N2.cc:
			The multi-threaded, C++ version of EstimateN (multi-threaded version of
			N1.cc) for even more speed performance. This file is (only) 250 times faster
			than the Python program, which may be due to the large amount of memory
			required of large N. Should be run with the following commands:
				make
				time /tmp/N2
	
		-N2_Commented.CC:
			A commented version of the file directly above sharing the same name.
			Since Luis created the upgrades to the original algorithm and
			introduced many new tricks from C++11, there was much learning to be done,
			which is shown in this file with lots of comments. This is a separate
			file intended for learning purposes about both N1.cc and the options
			used in the Makefile. It is not intended to run in any way shape or form.


	Original_Test_Results_Compilation.ods:
		A compilation of original test results from overnight tests without the analysis parts.

	Sampling_Until_Duplicate.py:
		Algorithm for duplicate confirmation sampling.


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

	Subprocess_Practice.py:
		A file for learning and practicing the module.
