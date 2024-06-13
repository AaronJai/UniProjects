# Project Information

# Overview
This project involves implementing several tasks in a Java project that works with iterators, student records API, and computing statistics from these records. The project is divided into three main packages:

itertools: A library of tools for working with iterators.
studentapi: Interfaces for accessing student records and handling paginated API responses.
studentstats: Computing statistics on student records using iterators for efficient data handling.

# Directory Structure

src
├── itertools
│   ├── DoubleEndedIterator.java
│   ├── Itertools.java
│   └── RangeIterator.java
├── studentapi
│   ├── QueryTimedOutException.java
│   ├── Student.java
│   └── StudentList.java
├── studentstats
│   ├── ApiUnreachableException.java
│   ├── StudentListIterator.java
│   └── StudentStats.java
└── test/...

# Tasks
itertools
TASK(1): Implement take

Implement the take method in Itertools.java. This method returns an iterator over a specified number of elements taken from the given iterator.
TASK(2): Implement reversed

Implement the reversed method in Itertools.java. This method returns an iterator in the reverse order of the given iterator.
TASK(3): Implement filter

Implement the filter method in Itertools.java. This method returns an iterator over the elements that satisfy a given predicate.
TASK(4): Implement map (single-ended)

Implement the single-ended map method in Itertools.java. This method returns an iterator over the elements with a given function applied to each element.
TASK(5): Implement map (double-ended)

Implement the double-ended version of the map method in Itertools.java.
TASK(6): Implement zip

Implement the zip method in Itertools.java. This method returns an iterator over the results of combining each pair of elements from two given iterators using a specified function.
TASK(7): Implement reduce

Implement the reduce method in Itertools.java. This method returns the result of combining all the elements from the given iterator using a specified function.


studentapi
No tasks to implement. This package provides interfaces to a simulated API for student records. It includes handling for paginated API responses and timeouts.


studentstats
TASK(8): Implement StudentListIterator

Implement the DoubleEndedIterator over the list of student records from the student API in StudentListIterator.java. Handle retries for QueryTimedOutException and raise an ApiUnreachableException if the API remains unreachable after the retry quota is exceeded.
TASK(9): Implement unitNewestStudents

Implement the unitNewestStudents method in StudentStats.java. This method returns an iterator over the students who have taken a given unit, from newest to oldest, using the StudentListIterator and tools from the itertools package.

# Compilation and Testing
cd src
javac **/*.java
java test.Test
