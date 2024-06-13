public class Intersection extends SetExpression {
    private SetExpression expressionA;
    private SetExpression expressionB;

    public Intersection(SetExpression expressionA, SetExpression expressionB) {
        this.expressionA = expressionA;
        this.expressionB = expressionB;
    }

    @Override
    public boolean contains(int elem) {
        // Check if the element is contained in BOTH of the expressions
        return expressionA.contains(elem) && expressionB.contains(elem);
    }

    @Override
    public String describe() {
        // Create the string representation of the intersection
        return "(" + expressionA.describe() + " n " + expressionB.describe() + ")";
    }
}
