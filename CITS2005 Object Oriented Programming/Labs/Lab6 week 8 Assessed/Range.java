public class Range extends SetExpression{
    private int low;
    private int high;

    public Range(int low, int high) {
        this.low = low;
        this.high = high;
    }

    @Override
    public boolean contains(int elem) {
        // Check element is in between low and high ranges
        return elem >= low && elem <= high;
    }

    @Override
    public String describe() {
        // Description of a set containing low and upper bound, separated by '..'
        return "[" + low + ".." + high + "]";
    }
}
