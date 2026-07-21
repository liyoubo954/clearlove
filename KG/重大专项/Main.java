import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        
        int n = in.nextInt();
        
        int[] distances = new int[n];
        int totalDistance = 0;
        for (int i = 0; i < n; i++) {
            distances[i] = in.nextInt();
            totalDistance += distances[i];
        }
        
        int x = in.nextInt();
        int y = in.nextInt();
        
        int clockwiseDistance = 0;
        int start = x - 1;
        int end = y - 1;
        
        if (start == end) {
            System.out.println(0);
            return;
        }
        
        int current = start;
        while (current != end) {
            clockwiseDistance += distances[current];
            current = (current + 1) % n;
        }
        
        int counterClockwiseDistance = totalDistance - clockwiseDistance;
        
        System.out.println(Math.min(clockwiseDistance, counterClockwiseDistance));
        
        in.close();
    }
}