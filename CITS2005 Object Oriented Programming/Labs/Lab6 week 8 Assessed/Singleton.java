public class Singleton extends SetExpression {
    private int elem;
    
    // Constructor to initialize the singleton set with a single element
    public Singleton(int elem) {
        this.elem = elem;
    }

    @Override
    public boolean contains(int elem) {
        // Check if the provided element is the same as the one stored
        return this.elem == elem;
    }

    @Override
    public String describe() {
        // Description of a set containing one element
        return "{" + elem + "}";
    }
}