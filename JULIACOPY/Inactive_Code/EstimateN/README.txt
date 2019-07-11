README:		For all files related to the proper finalized version of the
		working EstimateN algorithm, including testing files, the original
		Python version, and the 2 versions implemented in C++.

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

EstimateN Directory:
	Contains:

	-Best_K_Test_Results.ods:
		Spreadsheet containing all test results from Binary Search for a Best K

	-Binary_Search_Best_K.py:
		Searches for a k lower than a theoretical upper bound through Binary Search. 
		Contains many overnight test runs

	-EstimateN.py:
		The culmination of all our work during the six weeks from May 1, 2019
		to June 10 2019. The function NewEstimateN is the final and most correct
		base version (no speed upgrades) of our algorithm to approximate n
		with only confirmation sampling. 


	N1 Directory:
		Contains:

		All files related to the original version of the algorithm ported to C++
		for perfomance improvements.


	N2 Directory:
		Contains:
	
		All files related to the multi-threaded version of the algorithm ported
		to C++ for maximum perfomance optimization.


	-Original_Test_Results_Compilation.ods:
		A compilation of original test results from overnight tests without the analysis parts.

	-README.txt:
		File gives a quick overview of directory contents.

	-Sampling_Until_Duplicate.py:
		Algorithm for duplicate confirmation sampling.
