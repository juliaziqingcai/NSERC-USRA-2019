README:		For all files relating to the Coupon Collector's Problem, version 2.0 for testing (AKA C2)

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

C2 Directory:
	Contains:

	-C2.cc:
		A multiple-run tester version of the C1.cc program.
		Best used in conjunction with Linux file redirection commands for
		testing purposes, as no C++ file i/o has been directly implemented
		into the code.

	-in.txt:
		The intake file for C2.cc to test N = 1B

	-in2.txt:
		The intake file for C2.cc to test N = 100M

	-in3.txt:
		The intake file for C2.cc to test N = 10M

	-in4.txt:
		The intake file for C2.cc to test N = 10M

	-Makefile:
		The Makfile for the C2.cc file. Options chosen for max optimization of
		program perfomance.

	-results.ods:
		A compilation of all the C2.cc test results from all the other separate
		work sheets enumerated below for values of N = {1M, 10M, 100M, 1B} 
		orgranized by output terminal and N value

	-results01.ods -> results04.ods:
		Raw test output files for different terminal for N = 1B

	-results05.ods:
		Raw test output file for N = 100M

 	-results06.ods:
		Raw test output file for N = 10M

	-results05.ods:
		Raw test output file for N = 1M

	-README.txt:
		File gives a quick overview of directory contents.
