class Pair {
    public int x;
    public int y;

    public Pair(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Pair pair = (Pair) obj;
        return x == pair.x && y == pair.y;
    }
}

class Solution {
    public boolean canMeasureWater(int jug1Capacity, int jug2Capacity, int targetCapacity) {
        if (jug1Capacity + jug2Capacity < targetCapacity) return false;
        
        Set<Pair> visited = new HashSet<>();
        Queue<Pair> queue = new LinkedList<>();
        
        queue.add(new Pair(0, 0));

        while (!queue.isEmpty()) {
            Pair cur = queue.poll();

            if (cur.x + cur.y == targetCapacity) return true;
            if (visited.contains(cur)) continue;
            visited.add(cur);

            queue.add(new Pair(cur.x, jug2Capacity));
            queue.add(new Pair(jug1Capacity, cur.y));
            queue.add(new Pair(cur.x, 0));
            queue.add(new Pair(0, cur.y));

            int water = cur.x + cur.y;
            queue.add(new Pair(Math.min(water, jug1Capacity), Math.max(0, water - jug1Capacity)));
            queue.add(new Pair(Math.max(0, water - jug2Capacity), Math.min(water, jug2Capacity)));
        }
        return false;
    }
}


// class Pair {
//     public int x;
//     public int y;

//     public Pair(int x, int y) {
//         this.x = x;
//         this.y = y;
//     }
// }

// class Solution {

//     public boolean canMeasureWater(int jug1Capacity, int jug2Capacity, int targetCapacity) {
//         if(jug1Capacity + jug2Capacity == targetCapacity) return true;
//         if(jug1Capacity + jug2Capacity < targetCapacity) return false;
//         if(jug1Capacity % 2 == 0 && jug2Capacity % 2 == 0 && targetCapacity % 2 != 0)
//             return false;

//         int[][] dp = new int[jug1Capacity + 1][jug2Capacity + 1];
//         Queue<Pair> queue = new LinkedList<>();
        
//         queue.add(new Pair(0, 0));

//         while (!queue.isEmpty()) {
//             Pair cur = queue.poll();

//             if (cur.x + cur.y == targetCapacity) return true;

//             if (dp[cur.x][cur.y] == 1) continue;
//             dp[cur.x][cur.y] = 1;

//             if (dp[jug1Capacity][cur.y] != 1)
//                 queue.add(new Pair(jug1Capacity, cur.y));
//             if (dp[cur.x][jug2Capacity] != 1)
//                 queue.add(new Pair(cur.x, jug2Capacity));

//             if (dp[cur.x][0] != 1)
//                 queue.add(new Pair(cur.x, 0));
//             if (dp[0][cur.y] != 1)
//                 queue.add(new Pair(0, cur.y));

//             Pair left = fillLeft(jug1Capacity, cur);
//             if (dp[left.x][left.y] != 1)
//                 queue.add(left);
            
//             Pair right = fillRight(jug2Capacity, cur);
//             if (dp[right.x][right.y] != 1)
//                 queue.add(right);
//         }
//         return false;
//     }

//     private Pair fillLeft(int jug1Capacity,Pair cur) {
//         int sum = cur.x + cur.y;
//         if (sum > jug1Capacity) return new Pair(jug1Capacity, sum - jug1Capacity);
//         return new Pair(sum, 0);
//     }

//     private Pair fillRight(int jug2Capacity,Pair cur) {
//         int sum = cur.x + cur.y;
//         if (sum > jug2Capacity) return new Pair(sum - jug2Capacity, jug2Capacity);
//         return new Pair(0, sum);
//     }
// }
