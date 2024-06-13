# SetExpression Implementation

This project is a Java implementation of various set operations on integers, inspired by the Expression class from Lecture 11. The goal is to create a series of classes that extend the abstract `SetExpression` class, providing functionality for different set operations such as union, intersection, and complement.

## Specifications

### Abstract Class: SetExpression

The base class for all set operations:

```java
public abstract class SetExpression {

    // Evaluates if the set resulting from the expression contains elem
    public abstract boolean contains(int elem);

    /* Returns a string representation of the expression
       For example:
         "{}"
         "{7}"
         "~{5}"
         "[4..8]"
         "({} U {7})"
         "([4..8] n ({} U {7}))" */
    public abstract String describe();
}

Subclasses
1. Empty
Represents the empty set, containing no elements.

Constructor: Takes no arguments.
describe(): Returns "{}".
2. Singleton
Represents a set containing a single element.

Constructor: Takes a single integer, the element this set contains.
describe(): Returns the element within braces, e.g., "{7}".
3. Range
Represents a set containing every integer between a lower and upper bound, inclusive.

Constructor: Takes two integers, the lower and upper bounds.
describe(): Returns the bounds within square brackets separated by two dots, e.g., "[13..19]".
4. Complement
Represents the complement of a set, containing every integer not in some other set.

Constructor: Takes a single SetExpression, the set to be negated.
describe(): Returns the negated set prefixed with a tilde (~), e.g., "~{7}".
5. Union
Represents the union of two sets, containing all elements that appear in either set.

Constructor: Takes two SetExpressions, the sets to be unioned.
describe(): Returns the two sets with a capital 'U' between them, all wrapped in parentheses, e.g., "({} U {7})".
6. Intersection
Represents the intersection of two sets, containing all elements that appear in both sets.

Constructor: Takes two SetExpressions, the sets to be intersected.
describe(): Returns the two sets with a lower-case 'n' between them, all wrapped in parentheses, e.g., "({} n {7})".

Directory Structure
Your project should be organized as follows:

Assessed_Lab/
├── Complement.java
├── Empty.java
├── Intersection.java
├── Range.java
├── SetExpression.java
├── SetExpressionTests.java
├── Singleton.java
└── Union.java

Compilation and Testing
To compile and run the tests, navigate to the project directory and run the following commands:
javac SetExpressionTests.java
java SetExpressionTests
