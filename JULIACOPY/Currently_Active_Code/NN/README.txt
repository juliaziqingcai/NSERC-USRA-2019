README:		For all files related to the Simple Randomized Algorithm approach
		to the Nearest Neighbor Problem as presented by the 2019 CCCG Paper.

AUTHORS:	Julia Cai, Alexa de Grandmont

LAST UPDATE:	July 18th, 2019

LANGUAGE:	PYTHON
VERSION:	3 and above

ISSUES:		1) Python2 causes float division to become integer division
		2) Python2 causes the terminal input to require quotation marks
			around user input or else it will cause a runtime error
		3) Python3/Ubuntu/Something/??? doesn't like having to import and
			use modules with '+' in the module/program/file name; causes
			syntax error during runtime

----------------------------------------FILES--------------------------------------------------	

NN directory:
	Contains:

	-in.txt:
		Intake file for the NN program in terminal. Used for testing using
		the following terminal command:
			
			time /tmp/NN < in.txt >> results.ods
	
	-Makefile:
		The Makefile for the NN.cc file. Options for maximum perfomance
		optimization chosen.

	-NN.cc:
		Program file based off the CCCG-2019 paper (also found in the PDFs folder)
		for a randomized algorithm to address the all nearest neighbors problem.
		Currently in development.

	-README.txt:
		Files gives a quick overview of directory contents.

	-Results_Compilation.ods:
		Full compilation of all test results in multiple worksheets, along with
		an analysis of the spread of the values.
