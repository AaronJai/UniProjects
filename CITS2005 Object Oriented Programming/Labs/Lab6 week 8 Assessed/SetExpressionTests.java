public class SetExpressionTests {
    public static int numPass = 0;
    public static int numTest = 0;
    public static int passMarks = 0;
    public static int fullMarks = 0;
    public static boolean pass = true;

    // Awards marks if no tests have failed since last call
    public static void awardMarks(int marks) {
        fullMarks += marks;
        if (pass) passMarks += marks;
        pass = true;
    }

    // Tests that arguments are equal and reports result
    public static void expect(Object expected, Object received) {
        numTest++;
        if (expected.equals(received)) {
            numPass++;
            System.out.println("  OK: " + expected);
        } else {
            pass = false;
            System.out.println("  ERROR:");
            System.out.println("    expected " + expected);
            System.out.println("    received " + received);
        }
    }

    public static void main(String[] args) {
        testEmpty();
        testSingleton();
        testRange();
        testComplement();
        testUnion();
        testIntersection();
        testCombined();
        testCustom();

        System.out.println();
        if (numPass == numTest) {
            System.out.println("Passed all tests!");
        } else {
            System.out.println("Passed " + numPass + "/" + numTest + " tests.");
        }

        System.out.print("Estimated mark for sample tests: ");
        System.out.println(passMarks + "/" + fullMarks);
    }

    public static void testEmpty() {
        System.out.println("testEmpty:");
        SetExpression expression;

        expression = new Empty();
        expect("{}", expression.describe());
        expect(false, expression.contains(7));

        awardMarks(1);
    }

    public static void testSingleton() {
        System.out.println("testSingleton:");
        SetExpression expression;

        expression = new Singleton(7);
        expect("{7}", expression.describe());
        expect(true, expression.contains(7));
        expect(false, expression.contains(17));

        awardMarks(1);
    }

    public static void testRange() {
        System.out.println("testRange:");
        SetExpression expression;

        expression = new Range(13, 19);
        expect("[13..19]", expression.describe());
        expect(false, expression.contains(7));
        expect(false, expression.contains(12));
        expect(true, expression.contains(13));
        expect(true, expression.contains(17));
        expect(true, expression.contains(19));
        expect(false, expression.contains(20));

        awardMarks(1);
    }

    public static void testComplement() {
        System.out.println("testComplement:");
        SetExpression expression;

        expression = new Complement(new Empty());
        expect("~{}", expression.describe());
        expect(true, expression.contains(-2005));

        expression = new Complement(new Singleton(7));
        expect("~{7}", expression.describe());
        expect(false, expression.contains(7));
        expect(true, expression.contains(-2005));

        expression = new Complement(new Range(13, 19));
        expect("~[13..19]", expression.describe());
        expect(true, expression.contains(7));
        expect(false, expression.contains(17));

        awardMarks(1);
    }

    public static void testUnion() {
        System.out.println("testUnion:");
        SetExpression expression;

        expression = new Union(new Empty(), new Singleton(7));
        expect("({} U {7})", expression.describe());
        expect(true, expression.contains(7));

        expression = new Union(new Singleton(7), new Range(13, 19));
        expect("({7} U [13..19])", expression.describe());
        expect(true, expression.contains(7));
        expect(true, expression.contains(17));
        expect(false, expression.contains(10));

        expression = new Union(new Range(5, 9), new Range(13, 19));
        expect("([5..9] U [13..19])", expression.describe());
        expect(true, expression.contains(7));
        expect(false, expression.contains(11));
        expect(true, expression.contains(17));

        awardMarks(1);
    }

    public static void testIntersection() {
        System.out.println("testIntersection:");
        SetExpression expression;

        expression = new Intersection(new Empty(), new Singleton(7));
        expect("({} n {7})", expression.describe());
        expect(false, expression.contains(7));

        expression = new Intersection(new Singleton(7), new Singleton(7));
        expect("({7} n {7})", expression.describe());
        expect(true, expression.contains(7));

        expression = new Intersection(new Singleton(17), new Range(13, 19));
        expect("({17} n [13..19])", expression.describe());
        expect(true, expression.contains(17));
        expect(false, expression.contains(7));

        expression = new Intersection(new Range(10, 15), new Range(13, 19));
        expect("([10..15] n [13..19])", expression.describe());
        expect(true, expression.contains(14));
        expect(false, expression.contains(12));
        expect(false, expression.contains(16));

        awardMarks(1);
    }

    public static void testCombined() {
        System.out.println("testCombined:");
        SetExpression expression;

        expression = new Intersection(
            new Range(13, 19),
            new Complement(new Singleton(17))
        );
        expect("([13..19] n ~{17})", expression.describe());
        expect(false, expression.contains(17));
        expect(true, expression.contains(15));

        expression = new Union(
            new Intersection(new Singleton(7), new Empty()),
            new Intersection(new Range(13, 19), new Singleton(17))
        );
        expect("(({7} n {}) U ([13..19] n {17}))", expression.describe());
        expect(false, expression.contains(7));
        expect(true, expression.contains(17));

        expression = new Complement(new Intersection(
            new Union(new Singleton(7), new Singleton(17)),
            new Union(new Range(13, 19), new Singleton(7))
        ));
        expect("~(({7} U {17}) n ([13..19] U {7}))", expression.describe());
        expect(false, expression.contains(7));
        expect(true, expression.contains(14));
        expect(false, expression.contains(17));

        expression = new Union(
            new Intersection(new Range(7, 15), new Range(13, 22)),
            new Complement(new Union(new Range(7, 15), new Range(13, 22)))
        );
        expect(
            "(([7..15] n [13..22]) U ~([7..15] U [13..22]))",
            expression.describe()
        );
        expect(true, expression.contains(6));
        expect(false, expression.contains(7));
        expect(false, expression.contains(12));
        expect(true, expression.contains(13));
        expect(true, expression.contains(15));
        expect(false, expression.contains(16));
        expect(false, expression.contains(22));
        expect(true, expression.contains(23));

        awardMarks(1);
    }

    // You are encouraged to write your own extra tests here
    public static void testCustom() {
        System.out.println("testCustom:");
        // Put your custom tests here!
    }
}