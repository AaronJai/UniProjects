public class Union extends SetExpression {
    private SetExpression expressionA;
    private SetExpression expressionB;

    public Union(SetExpression expressionA, SetExpression expressionB) {
        this.expressionA = expressionA;
        this.expressionB = expressionB;
    }

    @Override
    public boolean contains(int elem) {
        // Check if the element is contained in EITHER of the expressions
        return expressionA.contains(elem) || expressionB.contains(elem);
    }

    @Override
    public String describe() {
        // Create the string representation of the union
        return "(" + expressionA.describe() + " U " + expressionB.describe() + ")";
    }
}
