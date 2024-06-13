package maze;

import java.util.Random;

public class RandomMaze extends Maze {
    // Creates a random maze with the given number of rows and columns.
    // The wallProbability is the probability that a given cell will be a wall.
    public RandomMaze(int rows, int cols, double wallProbability) {
       // TODO
        super(rows, cols); // Call the super constructor to initialize rows and cols
        Random rand = new Random();

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (rand.nextDouble() < wallProbability) { // Check if the wall should be placed based on probability
                    try { 
                        setWall(row, col); // Attempt to place a wall
                    } catch (MazeBoundsException e) {
                        // Since we control the bounds, this should never happen
                        System.err.println("Error placing wall at " + row + ", " + col);
                    }
                }
            }
        }
    }
}