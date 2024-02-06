Author:

Aaron Tan, 22884212

mysync

mysync is a command-line utility to synchronize the contents of two or more directories. 
It ensures that the directories provided hold identical copies of the same files based 
on their contents and modification times.

Features:
- Synchronize multiple directories.
- Options to include/exclude hidden files.
- Specify patterns to include or exclude specific files.
- Preserve file modification times and permissions.
- Verbose mode to display actions taken.
- Simulation mode to show actions without actually copying files.

Compilation:
To compile the mysync utility, simply use the provided Makefile:

make

This will produce an executable named mysync.

Usage:
./mysync [options] directory1 directory2 [directory3 ...]

Options:
- -a: Include all files, including hidden ones.
- -i pattern: Ignore files matching the provided pattern.
- -n: Simulation mode. Show actions without actually copying files. This also sets the -v option.
- -o pattern: Only synchronize files matching the provided pattern.
- -p: Preserve file modification times and permissions.
- -r: Recursively process directories.
- -v: Verbose mode. Display actions taken.

Example:
./mysync -a -r ~/Documents /media/myUSB ~/backup/Documents
This command recursively synchronizes the contents of the ~/Documents directory with /media/myUSB 
and ~/backup/Documents, including hidden files.

