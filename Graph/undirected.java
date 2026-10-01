import java.util.*;

public class undirected {
    public static void main(String[] args) {
        Scanner s= new Scanner(System.in);

        int vertex = s.nextInt();
        int edges = s.nextInt();

        ArrayList<ArrayList<Integer>> graph = new ArrayList<>();

        for (int i = 0; i < vertex; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < edges; i++) {
            int u = s.nextInt();
            int v = s.nextInt();

            graph.get(u).add(v);
            graph.get(v).add(u);
        }

         for (int i = 0; i < vertex; i++) {
            System.out.print("Vertex " + i + " : ");

            for (int j : graph.get(i)) {
                System.out.print(j + " ");
            }

            System.out.println();
        }
    }
}
