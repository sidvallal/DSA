// public class rotting_orange {
    
// }
import java.util.*;

public class rotting_orange {

    public static void main(String[] args) {

        int[][] grid = {
            {2, 1, 1},
            {1, 1, 0},
            {0, 1, 1}
        };

        int result = orangesRotting(grid);

        System.out.println("Minutes: " + result);
    }

    public static int orangesRotting(int[][] grid) {

        int rows = grid.length;
        int cols = grid[0].length;

        Queue<int[]> queue = new LinkedList<>();

        int fresh = 0;

        // Find all rotten and fresh oranges
        for (int i = 0; i < rows; i++) {

            for (int j = 0; j < cols; j++) {

                if (grid[i][j] == 2) {
                    // Add rotten orange to queue
                    queue.add(new int[]{i, j});
                }

                else if (grid[i][j] == 1) {
                    // Count fresh oranges
                    fresh++;
                }
            }
        }

        int minutes = 0;

        // Four directions
        int[][] directions = {
            {-1, 0},  // Up
            {1, 0},   // Down
            {0, -1},  // Left
            {0, 1}    // Right
        };

        // BFS
        while (!queue.isEmpty() && fresh > 0) {

            int size = queue.size();

            // Process one minute
            for (int i = 0; i < size; i++) {

                int[] current = queue.poll();

                int row = current[0];
                int col = current[1];

                // Check 4 directions
                for (int[] direction : directions) {

                    int newRow = row + direction[0];
                    int newCol = col + direction[1];

                    // Check boundary and fresh orange
                    if (newRow >= 0 && newRow < rows &&
                        newCol >= 0 && newCol < cols &&
                        grid[newRow][newCol] == 1) {

                        // Make it rotten
                        grid[newRow][newCol] = 2;

                        // One less fresh orange
                        fresh--;

                        // Add newly rotten orange
                        queue.add(new int[]{newRow, newCol});
                    }
                }
            }

            minutes++;
        }

        // If fresh oranges remain, impossible to rot them
        if (fresh > 0) {
            return -1;
        }

        return minutes;
    }
}
