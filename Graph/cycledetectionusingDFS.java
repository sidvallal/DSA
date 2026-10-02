// public class cycledetectionusingDFS {
    
// }

import java.util.*;

public class cycledetectionusingDFS {

    static boolean dfs(int node, int parent,
                       boolean[] visited,
                       List<List<Integer>> graph) {

        visited[node] = true;

        for (int neighbor : graph.get(node)) {

            if (!visited[neighbor]) {
                if (dfs(neighbor, node, visited, graph)) {
                    return true;
                }
            }

            else if (neighbor != parent) {
                return true;
            }
        }

        return false;
    }

    static boolean hasCycle(int V, List<List<Integer>> graph) {

        boolean[] visited = new boolean[V];

        for (int i = 0; i < V; i++) {
            if (!visited[i]) {
                if (dfs(i, -1, visited, graph)) {
                    return true;
                }
            }
        }

        return false;
    }

    public static void main(String[] args) {

        int V = 5;

        List<List<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < V; i++) {
            graph.add(new ArrayList<>());
        }

        addEdge(graph, 0, 1);
        addEdge(graph, 0, 2);
        addEdge(graph, 1, 3);
        addEdge(graph, 2, 3);
        addEdge(graph, 3, 4);

        System.out.println(hasCycle(V, graph));
    }

    static void addEdge(List<List<Integer>> graph, int u, int v) {
        graph.get(u).add(v);
        graph.get(v).add(u);
    }
}
