# MyScheduler (v3.0) - CITS2002 Project 1


## AUTHOR:

AARON ZHENG JIE TAN, 22884212


## INTRODUCTION:

MyScheduler is a simple process scheduling simulator, designed to mimic the execution of processes with various system calls. 
It reads configuration data from two input files, sysconfig and command, and simulates the execution of commands by multiple processes on a virtual CPU.


## USAGE:

To compile MyScheduler, use the following command:

cc -std=c11 -Wall -Werror -o myscheduler myscheduler.c


To run the program, use the following command with the appropriate command line arguments:

./myscheduler sysconfig-file command-file

(NOTE: The file names can be changed, so long as its format is correct and data values consistent.)


## OUTPUT:

The program generates 5 distinct features.

1. Number of devices found
2. Time quantum
3. Number of commands found
4. Simulation of the commands executed
5. Measurements containing the total time taken (in microseconds) to complete the simulation of the command sequence in the system, 
and the CPU-utilisation (the percentage of the time, as an integer, that the CPU is executing processes)


# OTHER NOTES:

Device data-transfer rates measured in bytes/second,
All times measured in microseconds (usecs),
Total process completion time will not exceed 2000 seconds.