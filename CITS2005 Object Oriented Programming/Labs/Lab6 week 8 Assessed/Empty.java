public class Empty extends SetExpression {

    // Constructor is not needed since it we don't need to initialise anything

    @Override
    public boolean contains(int elem) {
        // The empty set contains no elements, so we return false
        return false;
    }

    @Override
    public String describe() {
        // Description of an empty set
        return "{}";
    }
}
