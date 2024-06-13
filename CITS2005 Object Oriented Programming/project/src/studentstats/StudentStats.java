package studentstats;

import itertools.Itertools;

import studentapi.*;

import java.util.Iterator;
import java.util.function.BiFunction;
import java.util.function.Function;

import java.util.function.Predicate; // interface that checks a condition on an input argument, returning true or false.

/** A class for computing the average of a number of integer samples. */
class IntegerAverage {
    private int total = 0;
    private int count = 0;

    public void addSample(int sample) {
        total += sample;
        count++;
    }

    public int getAverage() {
        return total / count;
    }
}

/** A {@link BiFunction} adding an integer sample to an {@link IntegerAverage}. */
class IntegerAverageReduction implements BiFunction<IntegerAverage, Integer, IntegerAverage> {
    public IntegerAverage apply(IntegerAverage lhs, Integer rhs) {
        if (rhs == null) return lhs;
        lhs.addSample(rhs);
        return lhs;
    }
}

/** A {@link Function} retrieving the mark for a particular unit from a {@link Student} record. */
class GetUnitMark implements Function<Student, Integer> {
    String unit;

    public GetUnitMark(String unit) {
        this.unit = unit;
    }

    public Integer apply(Student student) {
        return student.getMark(unit);
    }
}

// TASK(9): Implement unitNewestStudents: You may want to declare a class here.

/**
 * The Predicate checking if a student has taken a given unit, & the mark is not null. ------------------------------------------------ MY ADDED CLASS
 */
class HasTakenUnit implements Predicate<Student> {
    private final String unit; // store unit code against student marks being checked

    /**
     * Constructor to initialize the HasTakenUnit predicate with a specific unit.
     * @param unit: unit code that will be checked against a students records.
     */
    public HasTakenUnit(String unit) {
        this.unit = unit;
    }

    /**
     * Evaluates this predicate on the given student to check if the student's mark for the specified unit is not null.
     * @param student The student object whose record is to be evaluated.
     * @return true if the student has a mark for the unit (meaning they took the unit); otherwise  false.
     */
    @Override
    public boolean test(Student student) {
        return student.getMark(unit) != null;
    }
}

/** A collection of statistical and analytical methods for working with the student API. */
public class StudentStats {
    /**
     * Returns the average mark (integer division) across all students who have completed a given
     * unit.
     *
     * @param list The student API interface.
     * @param unit The unit code.
     * @return The average mark for all students who have taken `unit`.
     */
    public static int unitAverage(StudentList list, String unit) {
        return Itertools.reduce(
                        Itertools.map(new StudentListIterator(list), new GetUnitMark(unit)),
                        new IntegerAverage(),
                        new IntegerAverageReduction())
                .getAverage();
    }

    /**
     * Returns an iterator over the students who have taken a given unit, from newest to oldest.
     *
     * @param list The student API interface.
     * @param unit The unit code.
     * @return An iterator over the students who have taken `unit`, from newest to oldest.
     */
    public static Iterator<Student> unitNewestStudents(StudentList list, String unit) {
        // TASK(9): Implement unitNewestStudents
        
        // Create a new StudentListIterator, which is a double ended iterator over the student records.
        StudentListIterator iterator = new StudentListIterator(list);

        // Use our Itertools.filter to filter students based on whether they have taken the given unit and have a non-null mark.
        // The filter operation is applied after reversing the iterator to process from newest to oldest students.
        // The reversal is done first, so the filtering happens on the reversed list.
        return Itertools.filter(Itertools.reversed(iterator), new HasTakenUnit(unit));
    }
}
