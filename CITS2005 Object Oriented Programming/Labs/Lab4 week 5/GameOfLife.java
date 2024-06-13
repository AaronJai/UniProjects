public class GameOfLife {
    private boolean[][] grid;

    public GameOfLife(boolean[][] initialGrid) {
        grid = initialGrid;
    }

    public void printGrid() {
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                System.out.print(grid[i][j] ? "O" : ".");
            }
            System.out.println();
        }
    }

    public void simulateStep() {
        boolean[][] nextGrid = new boolean[grid.length][grid[0].length];

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                int liveNeighbours = countLiveNeighbours(i, j);
                if (grid[i][j]) {
                    // A live cell
                    nextGrid[i][j] = liveNeighbours == 2 || liveNeighbours == 3;
                } else {
                    // A dead cell
                    nextGrid[i][j] = liveNeighbours == 3;
                }
            }
        }

        grid = nextGrid;
    }
    
    private int countLiveNeighbours(int row, int col) {
        int liveCount = 0;
        int[] directions = {-1, 0, 1};

        for (int i : directions) {
            for (int j : directions) {
                if (i == 0 && j == 0) continue; // Skip the cell itself
                int newRow = (row + i + grid.length) % grid.length;
                int newCol = (col + j + grid[0].length) % grid[0].length;
                if (grid[newRow][newCol]) liveCount++;
            }
        }

        return liveCount;
    }


    public static void main(String[] args) {
        boolean[][] initialGrid = new boolean[10][10];
        initialGrid[4][5] = true;
        initialGrid[4][6] = true;
        initialGrid[5][4] = true;
        initialGrid[5][5] = true;
        initialGrid[6][5] = true;
        GameOfLife game = new GameOfLife(initialGrid);
        for (int i = 0; i < 10; i++) {
            System.out.println("Before Step " + (i+1));
            game.printGrid();
            System.out.println();
            game.simulateStep();
        }
    }
}