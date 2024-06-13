import maze.*;
import java.util.*;

class MazeLocation {
    public int row, col;
    public MazeLocation(int row, int col) {
        this.row = row;
        this.col = col;
    }
}

public class MazeSolver {
    public static void main(String[] args) {
        int rows = 10, cols = 10;
        Maze maze = new RandomMaze(rows, cols, 0.2);
        MazeLocation[][] parent = new MazeLocation[rows][cols];
        parent[0][0] = new MazeLocation(-1, -1);
        Queue<MazeLocation> queue = new ArrayDeque<>();
        queue.add(new MazeLocation(0, 0));
        int[][] dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        try {
            while (!queue.isEmpty()) {
                MazeLocation loc = queue.remove();
                if (loc.row == rows - 1 && loc.col == cols - 1) {
                    break;
                }
                for (int[] dir : dirs) {
                    int row = loc.row + dir[0];
                    int col = loc.col + dir[1];
                    if (row >= 0 && row < rows && col >= 0 && col < cols && !maze.isWall(row, col) && parent[row][col] == null) {
                        parent[row][col] = loc;
                        queue.add(new MazeLocation(row, col));
                    }
                }
            }
            boolean[][] visited = new boolean[rows][cols];
            MazeLocation loc = parent[rows - 1][cols - 1];
            if (loc == null) {
                System.out.println("No solution");
            } else {
                visited[rows - 1][cols - 1] = true;
                while (loc.row != -1 && loc.col != -1) {
                    visited[loc.row][loc.col] = true;
                    loc = parent[loc.row][loc.col];
                }
            }
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    if (visited[r][c]) {
                        System.out.print("x");
                    } else if (maze.isWall(r, c)) {
                        System.out.print("#");
                    } else {
                        System.out.print(" ");
                    }
                }
                System.out.println();
            }
        } catch (MazeBoundsException e) {
            System.out.println(e.getMessage());
        }
    }
}