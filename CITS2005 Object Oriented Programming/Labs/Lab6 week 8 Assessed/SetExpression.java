// A "set arithmetic" version of the Expression class from lecture 11
public abstract class SetExpression {

    // Evaluates if the set resulting from the expression contains elem
    public abstract boolean contains(int elem);

    /* Returns a string representation of the expression
       For example:
         "{}"
         "{7}"
         "~{5}"
         "[4..8]"
         "({} U {7})"
         "([4..8] n ({} U {7}))" */
    public abstract String describe();
}