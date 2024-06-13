public class Complement extends SetExpression {
    private SetExpression expression;

    public Complement(SetExpression expression) {
        this.expression = expression;
    }

    @Override
    public boolean contains(int elem) {
        // return true if the set does not contain the element, false if it does.
        return !expression.contains(elem);
    }

    @Override
    public String describe() {
        // Description of a set containing every integer NOT in some other set
        return "~" + expression.describe();
    }
}
