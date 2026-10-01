import java.util.*;

public class bfs {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int vertex = sc.nextInt();
        int edges = sc.nextInt();

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

        // Create adjacency list
        for (int i = 0; i < vertex; i++) {
            graph.add(new ArrayList<>());
        }

        // Add edges
        for (int i = 0; i < edges; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();

            // Undirected graph
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        // BFS
        int start = sc.nextInt();

        boolean[] visited = new boolean[vertex];

        Queue<Integer> queue = new LinkedList<>();

        // Start BFS
        queue.add(start);
        visited[start] = true;

        while (!queue.isEmpty()) {

            int current = queue.poll();

            System.out.print(current + " ");

            // Visit all neighbors
            for (int neighbor : graph.get(current)) {

                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }

        sc.close();
    }
}