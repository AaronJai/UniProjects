// don't forget the package declaration here!
    package maze;

public class Maze {
    // Add fields here. They should all be private!
    private int rows;
    private int cols;
    private boolean[][] walls;

    public Maze(int rows, int cols) {
        // TODO
        this.rows = rows;
        this.cols = cols;
        this.walls = new boolean[rows][cols];
    }

    // Puts a wall at the given row and column.
    // Throws a MazeBoundsException if the row or column is invalid.
    public void setWall(int row, int col) throws MazeBoundsException {
        // TODO
        if (!isValidLocation(row, col)) {
            throw new MazeBoundsException("Invalid maze location: " + row + ", " + col);
        }

        walls[row][col] = true;
    }

    // Returns true if there is a wall at the given row and column.
    // Throws a MazeBoundsException if the row or column is invalid.
    public boolean isWall(int row, int col) throws MazeBoundsException {
        // TODO
        if (!isValidLocation(row, col)) {
            throw new MazeBoundsException("Invalid maze location: " + row + ", " + col);
        }

        return walls[row][col];
    }

    private boolean isValidLocation(int row, int col) {
        return row >= 0 && row < rows && col >= 0 && col < cols;
    }
}