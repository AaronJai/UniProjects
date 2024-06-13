import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SetExpressionEdgeCasesTests {

    @Test
    public void testNestedOperations() {
        SetExpression expr1 = new Union(new Singleton(1), new Range(3, 5));
        SetExpression expr2 = new Intersection(new Range(1, 10), expr1);
        assertTrue(expr2.contains(3), "Nested operation failed to identify element in both sets");
        assertFalse(expr2.contains(2), "Nested operation incorrectly identified element not in both sets");

        SetExpression expr3 = new Complement(new Complement(new Singleton(10)));
        assertTrue(expr3.contains(10), "Double negation failed to preserve elements");
        assertFalse(expr3.contains(9), "Double negation failed to exclude outside elements");
    }

    @Test
    public void testLargeRangePerformance() {
        SetExpression largeRange = new Range(1, 1000000);
        assertTrue(largeRange.contains(999999), "Large range failed to include correct elements");
        assertFalse(largeRange.contains(1000001), "Large range incorrectly included elements out of bounds");

        long startTime = System.nanoTime();
        largeRange.contains(500000); // Mid-point check
        long endTime = System.nanoTime();
        assertTrue((endTime - startTime) < 1000000, "Performance check failed for large range operations");
    }

    @Test
    public void testRangeBoundaryConditions() {
        SetExpression boundaryRange = new Range(-10, 10);
        assertTrue(boundaryRange.contains(-10), "Boundary check failed at lower end");
        assertTrue(boundaryRange.contains(10), "Boundary check failed at upper end");
        assertFalse(boundaryRange.contains(-11), "Boundary check incorrectly included out of range elements");
        assertFalse(boundaryRange.contains(11), "Boundary check incorrectly included out of range elements");
    }

    @Test
    public void testLogicalCompletenessForComplements() {
        SetExpression union = new Union(new Singleton(5), new Singleton(10));
        SetExpression complementOfUnion = new Complement(union);
        assertFalse(complementOfUnion.contains(5), "Complement incorrectly included element from original set");
        assertTrue(complementOfUnion.contains(6), "Complement failed to include correct elements");

        SetExpression doubleNegation = new Complement(new Complement(new Range(1, 3)));
        assertTrue(doubleNegation.contains(2), "Double negation failed at including correct elements");
        assertFalse(doubleNegation.contains(4), "Double negation incorrectly included out of range elements");
    }

    @Test
    public void testEmptySetOperations() {
        SetExpression empty = new Empty();
        SetExpression num = new Singleton(7);
        SetExpression emptyUnion = new Union(empty, num);
        assertTrue(emptyUnion.contains(7), "Union with empty set failed to behave correctly");
        assertFalse(emptyUnion.contains(1), "Union with empty set incorrectly included elements");

        SetExpression emptyIntersection = new Intersection(empty, new Range(1, 10));
        assertFalse(emptyIntersection.contains(1), "Intersection with empty set should be empty");
    }

    @Test
    public void testIdempotentAndIdentityProperties() {
        SetExpression idempotentUnion = new Union(new Singleton(1), new Singleton(1));
        assertTrue(idempotentUnion.contains(1), "Idempotent property failed for union");
        assertFalse(idempotentUnion.contains(2), "Idempotent property incorrectly included elements");

        SetExpression identityUnion = new Union(new Empty(), new Singleton(7));
        assertTrue(identityUnion.contains(7), "Identity property failed for union with empty set");
        assertFalse(identityUnion.contains(8), "Identity property incorrectly included elements");
    }

    @Test
    public void testRangeBoundaries() {
        SetExpression range = new Range(Integer.MIN_VALUE, Integer.MAX_VALUE);
        assertTrue(range.contains(Integer.MIN_VALUE), "Range should include the minimum integer value.");
        assertTrue(range.contains(Integer.MAX_VALUE), "Range should include the maximum integer value.");
    }


    @Test
    public void testComplexNestedExpressions() {
        SetExpression complexExpression = new Complement(
            new Union(
                new Intersection(
                    new Singleton(10),
                    new Range(5, 15)
                ),
                new Singleton(20)
            )
        );
        assertFalse(complexExpression.contains(10), "Complex expression should handle nested operations correctly.");
        assertTrue(complexExpression.contains(0), "Complex expression should negate the result of union correctly.");
        assertTrue(complexExpression.contains(21), "Complex expression should include numbers outside the union.");
    }

    @Test
    public void testRangeAtBoundaries() {
        SetExpression range = new Range(1, 10);
        assertTrue(range.contains(1), "Range should include the lower boundary.");
        assertTrue(range.contains(10), "Range should include the upper boundary.");
        assertFalse(range.contains(0), "Range should not include numbers below the lower boundary.");
        assertFalse(range.contains(11), "Range should not include numbers above the upper boundary.");
    }

    @Test
    public void testUnionWithEmptySet() {
        SetExpression empty = new Empty();
        SetExpression seven = new Singleton(7);
        SetExpression union = new Union(empty, seven);
        assertTrue(union.contains(7), "Union of empty set and {7} should contain 7.");
        assertFalse(union.contains(8), "Union of empty set and {7} should not contain 8.");
    }

    @Test
    public void testComplementOfRange() {
        SetExpression range = new Range(1, 5);
        SetExpression complement = new Complement(range);
        assertFalse(complement.contains(3), "Complement of range 1 to 5 should not contain 3.");
        assertTrue(complement.contains(6), "Complement of range 1 to 5 should contain 6.");
    }
}
