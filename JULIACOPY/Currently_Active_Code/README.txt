README:		For all currently active Summer 2019 NSERC-USRA Folder Program files

AUTHORS:	Julia Cai, Alexa de Grandmont

LAST UPDATE:	June 12th, 2019

LANGUAGE:	PYTHON
VERSION:	3 and above

ISSUES:		1) Python2 causes float division to become integer division
			2) Python2 causes the terminal input to require quotation marks
			around user input or else it will cause a runtime error
			3) Python3/Ubuntu/Something/??? doesn't like having to import and
			use modules with '+' in the module/program/file name; causes
			syntax error during runtime

----------------------------------------FILES--------------------------------------------------	

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


Makefile:
	The Makfile for the N1.cc file. Options chosen for max optimization of
	program perfomance.


N1.cc:
	The C++ version of EstimateN.py, ported over for perfomance gains.
	This will run 125 times faster than the Python file.
	Should be run with the time command in terminal to really compare
	performance, with the following commands:
		make
		time /tmp/N1


N1_Commented.cc:
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


README.txt:
	Files gives a quick overview of directory contents.


Sampling_Until_Duplicate.py:
	Algorithm for duplicate confirmation sampling.


Subprocess_Practice.py:
	A file for learning and practicing the module.
	
