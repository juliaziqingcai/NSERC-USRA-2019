README:		For all files relating to the Coupon Collector's Problem, version 1.0 (AKA C1)

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

C1 Directory:
	Contains:

	-C1.cc:
		An extension of the N1 and N2 estimating-n programs. The C series
		is our version of the coupon collector's problem, based on our
		approximations of n. C1 is the normal, single run program. 

	-Makefile:
		The Makfile for the C1.cc file. Options chosen for max optimization of
		program perfomance.

	-README.txt:
		File gives a quick overview of directory contents.
