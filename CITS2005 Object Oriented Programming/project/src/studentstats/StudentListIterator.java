package studentstats;

import itertools.DoubleEndedIterator;

import studentapi.*;

import java.util.NoSuchElementException; // used to indicate an element doesn't exist - useful for hasNext() seen later

/**
 * A (double ended) iterator over student records pulled from the student API.
 *
 * <p>This does not load the whole student list immediately, but rather queries the API ({@link
 * StudentList#getPage}) only as needed.
 */
public class StudentListIterator implements DoubleEndedIterator<Student> {
    // TASK(8): Implement StudentListIterator: Add any fields you require
    private StudentList list;       // Holds reference to the student API interface.
    private int retries;            // Number of retry attempts for API calls.

    private int frontIndex;         // Index of the next student to be retrieved in FORWARD iteration.
    private int backIndex;          // Index of the next student to be retrieved in REVERSE iteration.
    
    private int currentFrontPage;   // Index of the current FRONT page being accessed.
    private int currentBackPage;    // Index of the current BACK page being accessed.
    
    private Student[] frontPage;    // Stores the students of the current FRONT page.
    private Student[] backPage;     // Stores the students of the current BACK page.
    
    /**
     * Construct an iterator over the given {@link StudentList} with the specified retry quota.
     *
     * @param list The API interface.
     * @param retries The number of times to retry a query after getting {@link
     *     QueryTimedOutException} before declaring the API unreachable and throwing an {@link
     *     ApiUnreachableException}.
     */
    public StudentListIterator(StudentList list, int retries) {
        // TASK(8): Implement StudentListIterator
        this.list = list;                               // Assign student API interface to the local field.
        this.retries = retries;                         // Set number of retries for API calls in case of timeouts.

        this.frontIndex = 0;                            // Initialise front index to 0, starting iteration from the first student.
        this.backIndex = list.getNumStudents() - 1;     // Initialise back index to the last student in the list.
        
        this.currentFrontPage = 0;                      // Sets current front page index to the first page of the student data.
        this.currentBackPage = list.getNumPages() - 1;  // Sets current back page index to the last page of the student data.
        
        this.frontPage = null;                          // Initialises front page array to null since no page has been loaded yet.
        this.backPage = null;                           // Initialises back  page array to null since no page has been loaded yet.
    }

    /**
     * Construct an iterator over the given {@link StudentList} with a default retry quota of 3.
     *
     * @param list The API interface.
     */
    public StudentListIterator(StudentList list) {
        // TASK(8): Implement StudentListIterator
        this(list, 3);
    }

    @Override
    public boolean hasNext() {
        // TASK(8): Implement StudentListIterator
        return frontIndex <= backIndex; // using '<' would incorrectly skip last element.
    }

    /**
     * Loads a page of student records from the student API, allowing forward or reverse iteration.
     * Retry count specifies how much a page is loaded, otherwise an exception is thrown.
     *
     * @param isFront A boolean flag indicating the direction of page loading:
     *                true for loading next page at the front of the list,
     *                false for loading previous page at the back of the list.
     */
    private void loadPage(boolean isFront) {
        // ternary operator to see which page to load.
        int page = isFront ? currentFrontPage : currentBackPage;

        // try to load page based on specified retries
        for (int i = 0; i < retries; i++) {
            try {
                if (isFront) {
                    // If loading from the front, fetch the page using the current front page index.
                    frontPage = list.getPage(page);
                    // Increment the page index to move to the next page in subsequent calls.
                    currentFrontPage++;
                } else {
                    // If loading from the back, fetch the page using the current back page index.
                    backPage = list.getPage(page);
                    // Decrement the page index to move to the previous page in subsequent calls.
                    currentBackPage--;
                }
                return; // exit if it loads properly
            } catch (QueryTimedOutException e) {
                // If a timeout occurs, retry fetching the page until the retries limit is reached.
                // this catch block supposed to be intentionally left blank for retries.
            }
        }
        throw new ApiUnreachableException(); // throw exception if page not loaded and no more retries.
    }

    @Override
    public Student next() {
        // TASK(8): Implement StudentListIterator
        // throw exception if no next element.
        if (!hasNext()) {
            throw new NoSuchElementException();
        }

        // load next page if current page is null or we reached end of current page.
        if (frontPage == null || frontIndex >= (currentFrontPage - 1) * list.getPageSize() + frontPage.length) {
            loadPage(true); // true sets loadPage to go forward
        }

        // return student at current index, and increment for next call (using postfix).
        //  '%'  ensures the index wraps around the page size.
        return frontPage[frontIndex++ % list.getPageSize()];
    }

    @Override
    public Student reverseNext() {
        // TASK(8): Implement StudentListIterator
        // method stops when backIndex becomes less than frontIndex.
        if (!hasNext()) {
            throw new NoSuchElementException();
        }

        // similar to above but load previous page if current page null or reached start of current back page.
        if (backPage == null || backIndex < (currentBackPage + 1) * list.getPageSize()) {
            loadPage(false); // false sets loadPage to go backward.
        }

        // return student at current back index and decrement index for next reverse call (using postfix as well).
        // '%' ensures the index wraps around within the current page's size.
        return backPage[backIndex-- % list.getPageSize()];
    }
}
