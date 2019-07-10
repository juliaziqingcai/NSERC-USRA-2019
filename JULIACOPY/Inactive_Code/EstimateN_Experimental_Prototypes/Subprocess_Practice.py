'''
FILE FOR PRACTICING THE SUBPROCESS MODULE
MUST BE RUN FROM TERMINAL
'''
import subprocess


# SIMPLE COMMANDS
# Will run the command described by args
'''
subprocess.call(['ls', '-al',], shell=True)
# By default shell=False, and it is DANGEROUS to set it to True with an                                   
subprocess.call(['df', '-h'])
'''


# RETURN CODES
'''
completed = subprocess.run(['ls', '-1'])
print('returncode:', completed.returncode)
# a return code of anything but 0 indicates an error
# Subprocess can be used to subpress return values this way
'''


# RUN COMMAND AND CAPTURE OUTPUT
'''
# run() returns a CompletedProcess object if it was successful
# errors in the created process are raised here too
process = subprocess.run(['ls','-lha'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout

while (True):# used to test simultaneous terminals running programs CPU usage
    print(output)
'''


# TEST WHAT REDIRECTED OUTPUT FROM STDOUT -> FILE LOOKS LIKE
import Binary_Search_Best_K
'''
process = subprocess.run(['python3', Binary_Search_Best_K.binary_search_best_k_original], check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout
print(output)
file = open('testing.ods', a)
file.write(output)
'''

def main():
    process = subprocess.run(['python3', 'Binary_Search_Best_K.py],/
     check=True, stdout=subprocess.PIPE, universal_newlines=True)


if __name__=='__main__':
    main()

