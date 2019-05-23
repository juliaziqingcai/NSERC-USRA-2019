README:		For all currently in-active (not in use OR not of interest at the moment)
		Summer 2019 NSERC-USRA Folder Program files

AUTHORS:	Julia Cai, ALexa de Grandmont

LAST UPDATE:	May 23rd, 2019

LANGUAGE:	PYTHON
VERSION:	3 and above

ISSUES:		1) Python2 causes float division to become integer division
		2) Python2 causes the terminal input to require quotation marks
			around user input or else it will cause a runtime error
		3) Python3/Ubuntu/Something/??? doesn't like having to import and
			use modules with '+' in the module/program/file name; causes
			syntax error during runtime

FILES:		
	
	Approximating_N_With_2kPlus1_Samples.py:		Gets an approximate n after 2k+1 									runs of the duplicate confirmation 									sampling algorithm
		
	Approximating_N_With_Median_Counter.py:			Approximates a set size by 									returning the median of 2k+1 									samples
		
	Comparing_Counter_To_Expected_Value.py:			Compares the actual returned 									counter value to the expected 									value of the counter
		
	May_14th_Louis_Homework.py:				Louis' attempt to approximate the 									set size on May 14th, 2019

	Median_Counter_Vs_Average_Counter_Approximated_Ns.py:	Compares whether approximating the 									set size with the median counter 									OR the average counter is more 									accurate
	
	Median_Of_Medians_Vs_Median_Of_Samples.py:		Compares which median is more 									accurate

	Modified_German_Tank_Problem.py:			Algorithm and tester for our 									version of the German Tank Problem 									(we use the full set, with 									replacement)
		
	Not_In_Green_Interval_Bound_Inequality.py:		Tests if the upper-bound for the 									probability that the approximated 									set size is NOT within the 									acceptable interval (green) holds
