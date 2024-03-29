README:		For all currently in-active (not in use OR not of interest at the moment)
		Summer 2019 NSERC-USRA Folder Program files

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

Coupon_Collector Directory:
	Contains:

	All directories and files related to the Coupon Collector's Problem


EstimateN Directory:
	Contains:

	All files related to the refinement of the final version of the EstimateN
	algorithm, including the original Python version, the test files related to
	discovery the exact relationship between epsilon and k (#samples), and the
	2 versions ported to C++ for perfomance optimization.


EstimateN_Experimental_Prototypes Directory:
	Contains:

	All files related to the development and search for an algorithm that
 	could reliably approximate set size only through duplicate confirmation 
	sampling with replacement. They are all prototypes and only meant to
	show the journey to algorithm in the files in the EstimateN directory.
	READ ONLY


	-README.txt:
		File gives a quick overview of directory contents.
