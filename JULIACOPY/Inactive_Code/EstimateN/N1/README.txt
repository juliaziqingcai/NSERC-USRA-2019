README:		For all files related to the original C++ ported version of
		the EstimateN algorithm for performance gains. (AKA N1)

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

	-README.txt:
		File gives a quick overview of directory contents.
