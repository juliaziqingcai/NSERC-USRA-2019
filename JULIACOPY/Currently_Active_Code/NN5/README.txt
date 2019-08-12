README:		For all files related to the modified 4D Conjecture 
		Testing Version of the Simple Randomized Algorithm 
		approach to the Nearest Neighbor Problem as presented 
		by the 2019 CCCG Paper.

AUTHORS:	Julia Cai, Alexa de Grandmont

LAST UPDATE:	August 12th, 2019

LANGUAGE:	PYTHON
VERSION:	3 and above

ISSUES:		1) Python2 causes float division to become integer division
		2) Python2 causes the terminal input to require quotation marks
			around user input or else it will cause a runtime error
		3) Python3/Ubuntu/Something/??? doesn't like having to import and
			use modules with '+' in the module/program/file name; causes
			syntax error during runtime

----------------------------------------FILES--------------------------------------------------	

NN5 directory:
	Contains:

	-Makefile:
		The Makefile for the NN5.cc file. Options for maximum perfomance
		optimization chosen.

	-NN5.cc:
		WARNING: Still under development and has implementation errors
		Program file based off a modified version of the CCCG-2019 paper 
		(also found in the PDFs folder) for a randomized algorithm to address
		the all nearest neighbors problem. Modified it to work for 4D as an
		extension of the original 2D(NN) and 3D(NN4) algorithms. Allows
		generation of multiple point sets and calculates averages for the while
		loop counter and the delta. Used for testing using the following 
		terminal command:
			
			time /tmp/NN5 >> results.ods
		

	-README.txt:
		Files gives a quick overview of directory contents.

	-results_compilation.ods:
		All test results compiled together along with their analyses.
		TBA when NN5.cc implementation is fixed.

