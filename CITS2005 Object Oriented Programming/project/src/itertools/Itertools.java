package itertools;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;

/**
 * A collection of useful methods for working with iterators.
 *
 * @see Iterator
 * @see DoubleEndedIterator
 */
public class Itertools {
    /**
     * Given an iterator and a number of elements, returns an iterator over that number of elements
     * taken from the iterator (or as many as it contains, if less than that number).
     *
     * <p>Elements are consumed from the given iterator only as needed.
     *
     * @param <T> The type of elements in the iterator.
     * @param it The iterator from which to take elements.
     * @param count The maximum number of elements to take.
     * @return An iterator over the first `count` elements of `it`.
     */
    public static <T> Iterator<T> take(Iterator<T> it, int count) {
        // TASK(1): Implement take
        return new Iterator<T>() {
            private int remaining = count; // track number of elements left to take

            @Override
            public boolean hasNext() {
                // check if theres still elements to be taken and if 'it' has more elements
                return remaining > 0 && it.hasNext(); 
            }

            @Override
            public T next() {
                if (remaining <= 0) {
                    throw new NoSuchElementException();
                }
                remaining--; // decrease remaining when an element is taken
                return it.next(); // returns next element from original iterator
            }
        };
    }

    /**
     * Returns a (double ended) iterator in the reverse order of the one given.
     *
     * <p>Elements are consumed from the given iterator only as needed.
     *
     * @param <T> The type of elements in the iterator.
     * @param it The (double ended) iterator to reverse.
     * @return The reverse of the given iterator.
     */
    public static <T> Iterator<T> reversed(DoubleEndedIterator<T> it) {
        // TASK(2): Implement reversed
        return new DoubleEndedIterator<T>() {
            @Override
            public boolean hasNext() {
                return it.hasNext();
            }
    
            @Override
            public T next() {
                return it.reverseNext(); // calls this on original iterator to reverse order
            }
    
            @Override
            public T reverseNext() {
                return it.next(); // does opposite of above; both methods give us the bi-directional ability
            }
        };
    }

    /**
     * Returns an iterator over the elements of a given iterator with those elements that do not
     * satisfy a given {@link Predicate} dropped.
     *
     * <p>Elements are consumed from the given iterator only as needed (though it may be necessary
     * to consume elements to determine whether there is a next element that satisfies the
     * predicate).
     *
     * <p>Java's {@link Predicate} interface can be used by calling `pred.test(x)`, and will return
     * `true` if and only if `x` satisfies the predicate.
     *
     * @param <T> The type of elements in the iterator.
     * @param it The iterator to filter.
     * @param pred The predicate to use to determine whether to keep or drop an element.
     * @return An iterator over the elements of `it` with elements not satisfying `pred` removed.
     */
    public static <T> Iterator<T> filter(Iterator<T> it, Predicate<T> pred) {
        // TASK(3): Implement filter

        // I.e., Iterator<T> processes elements if it satisfies condition defined by Predicate<T>
        return new Iterator<T>() {
            private T nextElement; // stores next element that matches predicate
            private boolean hasElementReady = false; // tracks if next element is ready
    
            @Override
            public boolean hasNext() {
                // If a matching element has already been found, return true immediately
                if (hasElementReady) {
                    return true;
                }
                while (it.hasNext()) {
                    T element = it.next();
                    // Apply the predicate to check if the element should be included
                    if (pred.test(element)) {
                        nextElement = element;  // stores the element that matches the predicate
                        hasElementReady = true; // set flag when next element meets the predicate
                        return true;
                    }
                }
                return false; // false when no more elements matching
            }
    
            @Override
            public T next() {
                if (!hasNext()) { // This will also check if the next element is already found
                    throw new NoSuchElementException();
                }
                hasElementReady = false; // reset flag after element is taken
                return nextElement;
            }
        };
    }

    /**
     * Returns an iterator over the elements of a given iterator with a given function applied to
     * each element.
     *
     * <p>That is, given a function `f` and an iterator over the elements `a, b, c, ...`, returns an
     * iterator over `f(a), f(b), f(c), ...`.
     *
     * <p>Elements are consumed from the given iterator only as needed.
     *
     * <p>Java's {@link Function} interface can be used by calling `f.apply(x)` and will return
     * `f(x)`.
     *
     * @param <T> The type of elements in the input iterator.
     * @param <R> The type of elements in the result iterator.
     * @param it The iterator to map over.
     * @param f The function to apply to each element.
     * @return An iterator over the results of applying `f` to each element in `it`.
     */
    public static <T, R> Iterator<R> map(Iterator<T> it, Function<T, R> f) {
        // TASK(4): Implement map
        return new Iterator<R>() {
            @Override
            public boolean hasNext() {
                return it.hasNext();
            }
    
            @Override
            public R next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                return f.apply(it.next()); // apply function to next element as described and returns result
            }
        };
    }

    /**
     * A double-ended overload of {@link #map}.
     *
     * @param <T> The type of elements in the input iterator.
     * @param <R> The type of elements in the result iterator.
     * @param it The iterator to map over.
     * @param f The function to apply to each element.
     * @return An iterator over the results of applying `f` to each element in `it`.
     */
    public static <T, R> DoubleEndedIterator<R> map(DoubleEndedIterator<T> it, Function<T, R> f) {
        // TASK(5): Implement map (double ended)
        return new DoubleEndedIterator<R>() {
            @Override
            public boolean hasNext() {
                return it.hasNext();
            }
            
            // next() and reverse() follows same concept as task 2 for bi-directional flow,
            // and pretty much same lines of code as previous task, just now with reverseNext()
            @Override
            public R next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                return f.apply(it.next());
            }
    
            @Override
            public R reverseNext() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                return f.apply(it.reverseNext());
            }
        };
    }

    /**
     * Returns an iterator over the results of combining each pair of elements from a pair of given
     * iterators using a given function.
     *
     * <p>That is, given a function `f` and iterators over the elements `a, b, c, ...` and `x, y, z,
     * ...` returns an iterator over `f(a, x), f(b, y), f(c, z), ...`.
     *
     * <p>The iterator ends when either input iterator ends.
     *
     * <p>Elements are consumed from the given iterators only as needed.
     *
     * <p>Java's {@link BiFunction} interface can be used by calling `f.apply(x, y)` and will return
     * `f(x, y)`.
     *
     * @param <T> The type of elements in the "left-hand" iterator.
     * @param <U> The type of elements in the "right-hand" iterator.
     * @param <R> The type of elements in the result iterator.
     * @param lit The "left-hand" iterator.
     * @param rit The "right-hand" iterator.
     * @param f A function to use to combine elements from `lit` and `rit`.
     * @return An iterator over the result of combining elements from `lit` and `rit` using `f`.
     */
    public static <T, U, R> Iterator<R> zip(
            Iterator<T> lit, Iterator<U> rit, BiFunction<T, U, R> f) {
        // TASK(6): Implement zip
        return new Iterator<R>() {
            @Override
            public boolean hasNext() {
                return lit.hasNext() && rit.hasNext();
            }
    
            @Override
            public R next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                return f.apply(lit.next(), rit.next()); // like task 4 but with elements from 2 lists
            }
        };
    }

    /**
     * Returns the result of combining all the elements from the given iterator using the given
     * function.
     *
     * <p>Each element is combined with the current value using the given function.
     *
     * <p>For example, given a function `f`, an initial value `x`, and an iterator over the elements
     * `a, b, c`, returns `f(f(f(x, a), b), c)`.
     *
     * <p>Java's {@link BiFunction} interface can be used by calling `f.apply(x, y)` and will return
     * `f(x, y)`.
     *
     * @param <T> The type of elements in the "left-hand" iterator.
     * @param <R> The type of the result.
     * @param it The iterator to reduce.
     * @param init The initial value.
     * @param f The function to use to combine each element into the reduction value.
     * @return The value after all elements have been combined.
     */
    public static <T, R> R reduce(Iterator<T> it, R init, BiFunction<R, T, R> f) {
        // TASK(7): Implement reduce
        R result = init;
        while (it.hasNext()) { // while loop helps apply function to each element and 'accumulates' as long there's elements in the list
            result = f.apply(result, it.next());
        }
        return result;
    }
}
