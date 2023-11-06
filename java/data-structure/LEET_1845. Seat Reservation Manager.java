class SeatManager {
    private int last;
    private PriorityQueue<Integer> pq;

    public SeatManager(int n) {
        this.last = 0;
        this.pq = new PriorityQueue<>();
    }
    
    public int reserve() {
        if (pq.isEmpty()) return ++last;
        else return pq.poll();
    }
    
    public void unreserve(int seatNumber) {
        if (seatNumber == last) --last;
        else pq.offer(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */


/*
PREVIOUS METHOD
Time efficiency : 5%
Mem efficiency : 90%
*/

 /*
 class SeatManager {

    private boolean[] seats;
    int next_to_in = 0;

    public SeatManager(int n) {
        this.seats = new boolean[n];
    }
    
    public int reserve() {
        int temp = next_to_in;
        seats[next_to_in] = true;
        for (int i = next_to_in + 1; i < seats.length; ++i) {
            if (!seats[i]) {
                next_to_in = i;
                return temp + 1;
            }
        }
        next_to_in = seats.length;
        return temp + 1;
    }
    
    public void unreserve(int seatNumber) {
        seats[seatNumber - 1] = false;
        if (next_to_in > seatNumber - 1) next_to_in = seatNumber - 1;
    }
}

*/
