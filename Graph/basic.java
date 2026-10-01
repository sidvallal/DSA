import java.util.*;

public class basic{
    public static void main(String[] args) {
        int vertex = 5;
        ArrayList<ArrayList<Integer>> arr = new ArrayList<>();

        for (int i = 0; i < vertex; i++) {
            arr.add(new ArrayList<>());
        }

        arr.get(0).add(1);

        arr.get(1).add(0);
        arr.get(1).add(1);
        arr.get(1).add(3);

        arr.get(2).add(1);
        arr.get(2).add(3);
        arr.get(2).add(4);

        arr.get(3).add(1);
        arr.get(3).add(2);

        arr.get(4).add(2);

        for (int i = 0; i < vertex; i++) {
            System.out.println("Vertex : "+i);
            for(int j: arr.get(i)){
                System.out.println(j+ " ");
            }
            System.out.println();
        }
    }
}