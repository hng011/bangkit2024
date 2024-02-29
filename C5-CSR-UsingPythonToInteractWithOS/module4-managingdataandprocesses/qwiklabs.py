#!/usr/bin/env python3
import sys
import os
import re


"""
34.125.239.247
student-03-d5e9b0904681
student-03-d5e9b0904681@34.125.239.247
"""

"""
we'll search for the CRON error that failed to start. 
To do this, we'll use a python script to search log files for a particular type of ERROR log. 
In this case, we'll search for a CRON error within the fishy.log file that failed 
to start by narrowing our search to "CRON ERROR Failed to start".
"""

"""
The sys module provides information about the Python interpreter's constants,
functions, and methods. The os module provides a portable way of using operating system dependent 
functionality with Python.

Regular Expression (RegEx) is a sequence of characters that defines a search pattern. 
We can use regular expressions using re module.

Define the error_search function and pass the log file to it as a parameter.
"""

"""
function error_search that takes log_file as a parameter and returns returned_errors. 
"""
def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors

  
def file_output(returned_errors):
    with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
        """
        expandsuer() returns the home directory of your system instance. 
        Then, we'll concatenate this path (to the home directory) 
        to the file errors_found.log in /data directory
        """
        for error in returned_errors:
            file.write(error)
        file.close()

if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)